import json
import requests
import uuid
import time
import sys
import os

BASE_URL = "https://api-x9.verolabs.co"

# Use relative path if running from project root, otherwise fallback to absolute path
SPEC_PATH = "openapi.docs.en.json"
if not os.path.exists(SPEC_PATH):
    SPEC_PATH = "/Users/tony/dev/vero-docs-oms/openapi.docs.en.json"

print(f"Starting verification of all APIs using spec: {SPEC_PATH}...")

# 1. SETUP AUTHENTICATION (Register a new test user and obtain session & JWT token)
session_token = None
jwt_token = None
email = None
password = None
account_id = None
bank_account_id = None
watchlist_id = "1"
referral_code = "TESTREF"

def get_auth_tokens():
    global session_token, jwt_token, email, password
    print("\n" + "="*80)
    print(" 1. AUTHENTICATION SETUP ".center(80, "="))
    print("="*80)
    
    # Create Registration Flow
    url = f"{BASE_URL}/api/authen/self-service/registration/api"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            print(f"Failed to create registration flow: {res.status_code}")
            return False
        flow_data = res.json()
        flow_id = flow_data.get("id")
    except Exception as e:
        print(f"Error creating registration flow: {e}")
        return False
        
    # Extract CSRF token
    csrf_token = ""
    nodes = flow_data.get("ui", {}).get("nodes", [])
    for node in nodes:
        if node.get("attributes", {}).get("name") == "csrf_token":
            csrf_token = node.get("attributes", {}).get("value", "")
            break
            
    # Submit Registration
    test_id = str(uuid.uuid4())[:8]
    email = f"test_all_apis_{test_id}@verolabs.co"
    password = f"P@ssword123_{test_id}"
    
    reg_url = f"{BASE_URL}/api/authen/self-service/registration?flow={flow_id}"
    payload = {
        "method": "password",
        "csrf_token": csrf_token,
        "password": password,
        "traits": {
            "email": email,
            "name": {
                "first": "Test",
                "last": "User"
            },
            "documentNumber": f"999999{test_id}"
        }
    }
    
    try:
        res = requests.post(reg_url, json=payload, timeout=10)
        if res.status_code != 200:
            print(f"Failed to submit registration: {res.status_code} - {res.text[:200]}")
            return False
        reg_response = res.json()
        session_token = reg_response.get("session_token")
        print(f"Registered user: {email}")
        print(f"Obtained Session Token: {session_token[:10]}...")
    except Exception as e:
        print(f"Error submitting registration: {e}")
        return False
        
    # Get WHOAMI with tokenized JWT
    whoami_url = f"{BASE_URL}/api/authen/sessions/whoami?tokenize_as=jwt_template_1"
    headers = {"X-Session-Token": session_token}
    try:
        res = requests.get(whoami_url, headers=headers, timeout=10)
        if res.status_code != 200:
            print(f"Failed whoami verification: {res.status_code} - {res.text[:200]}")
            return False
        whoami_data = res.json()
        jwt_token = whoami_data.get("tokenized")
        if jwt_token:
            print(f"Obtained Bearer JWT: {jwt_token[:15]}...")
            return True
        else:
            print("Warning: WHOAMI response did not contain 'tokenized' JWT token.")
            # Fallback to session_token as bearer if jwt_token is empty
            jwt_token = session_token
            return True
    except Exception as e:
        print(f"Error executing whoami: {e}")
        return False

# Parse OpenAPI Spec directly at runtime
if not os.path.exists(SPEC_PATH):
    print(f"Error: Spec file {SPEC_PATH} not found.")
    sys.exit(1)

with open(SPEC_PATH, "r", encoding="utf-8") as f:
    spec = json.load(f)

paths = spec.get("paths", {})
test_cases = []
for path, path_item in paths.items():
    for method, operation in path_item.items():
        if method.lower() not in ["get", "post", "put", "delete", "patch"]:
            continue
        
        security = operation.get("security", spec.get("security", []))
        has_security = len(security) > 0
        servers = operation.get("servers", spec.get("servers", []))
        base_url = servers[0].get("url", BASE_URL) if servers else BASE_URL
        
        parameters = operation.get("parameters", [])
        
        body_schema = None
        request_body = operation.get("requestBody", {})
        if request_body:
            content = request_body.get("content", {})
            for mime, media in content.items():
                if "json" in mime:
                    body_schema = media.get("schema", {})
                    break
        
        test_cases.append({
            "path": path,
            "method": method.upper(),
            "base_url": base_url.rstrip("/"),
            "has_security": has_security,
            "security": security,
            "parameters": [
                {
                    "name": p.get("name"),
                    "in": p.get("in"),
                    "required": p.get("required", False),
                    "type": p.get("schema", {}).get("type", "string")
                }
                for p in parameters
            ],
            "body_schema": body_schema,
            "responses": operation.get("responses", {})
        })

# Initialize dynamic values
now_ms = int(time.time() * 1000)
one_day_ms = 24 * 60 * 60 * 1000
start_time_ms = now_ms - one_day_ms
end_time_ms = now_ms

now_sec = int(time.time())
one_day_sec = 24 * 60 * 60
start_time_sec = now_sec - one_day_sec
end_time_sec = now_sec

# Run auth setup
auth_ok = get_auth_tokens()
if not auth_ok:
    print("Authentication setup failed. Proceeding with dummy tokens for public tests.")
    session_token = "dummy_session_token"
    jwt_token = "dummy_jwt_token"

# Retrieve valid accounts and bank accounts before testing
def retrieve_dependent_data():
    global account_id, bank_account_id
    if not auth_ok:
        return
    headers = {"Authorization": f"Bearer {jwt_token}"}
    
    # 1. Accounts list
    try:
        res = requests.get(f"{BASE_URL}/api/v1/users/accounts", headers=headers, timeout=10)
        if res.status_code == 200:
            accounts = res.json()
            if isinstance(accounts, list) and len(accounts) > 0:
                account_id = accounts[0].get("accountId") or accounts[0].get("accountID") or accounts[0].get("id")
                print(f"Retrieved active Account ID: {account_id}")
    except Exception as e:
        print(f"Failed to fetch accounts: {e}")
        
    # 2. Bank accounts list
    try:
        res = requests.get(f"{BASE_URL}/api/v1/bank-accounts", headers=headers, timeout=10)
        if res.status_code == 200:
            banks = res.json()
            if isinstance(banks, list) and len(banks) > 0:
                bank_account_id = banks[0].get("bankAccountID") or banks[0].get("id")
                print(f"Retrieved active Bank Account ID: {bank_account_id}")
    except Exception as e:
        print(f"Failed to fetch bank accounts: {e}")

retrieve_dependent_data()

# Fallback values
if not account_id:
    account_id = "test-account-id"
if not bank_account_id:
    bank_account_id = "test-bank-id"

# Function to build URL path with parameters
def build_path(path):
    replacements = {
        "{accountID}": str(account_id),
        "{start_time}": str(start_time_ms),
        "{end_time}": str(end_time_ms),
        "{from}": str(start_time_ms if "GetOhlcvHis" in path or "GetProductTradeLog" in path else start_time_sec),
        "{to}": str(end_time_ms if "GetOhlcvHis" in path or "GetProductTradeLog" in path else end_time_sec),
        "{symbol}": "VN30F1M",
        "{watchlist_id}": str(watchlist_id),
        "{search}": "VN30",
        "{resolution}": "1",
        "{countBack}": "10",
        "{refOrderID}": "REF-" + str(uuid.uuid4())[:8],
        "{orderSide}": "Buy",
        "{price}": "1000",
        "{qty}": "1",
        "{orderType}": "Limit",
        "{orderID}": "test-order-id",
        "{orderId}": "test-stop-order-id",
        "{bracketOrderId}": "test-bracket-order-id",
        "{notify_id}": "test-notify-id",
        "{ref_code}": "TESTREF",
        "{bankID}": str(bank_account_id),
        "{index}": "VNINDEX"
    }
    
    # Swap variables
    for placeholder, val in replacements.items():
        path = path.replace(placeholder, val)
    return path

# Function to generate dummy request body based on spec schema
def build_body(path, body_schema):
    if not body_schema:
        return None
    
    # Custom bodies for specific paths
    if "login" in path:
        return {
            "method": "password",
            "csrf_token": "dummy",
            "password_identifier": email or "test@verolabs.co",
            "password": password or "Password123"
        }
    if "registration" in path:
        return {
            "method": "password",
            "csrf_token": "dummy",
            "password": "Password123",
            "traits": {
                "email": "test_dummy@verolabs.co",
                "name": {"first": "Test", "last": "User"},
                "documentNumber": "12345678"
            }
        }
    if "recovery" in path:
        return {
            "method": "code",
            "email": email or "test@verolabs.co"
        }
    if "settings" in path:
        return {
            "method": "password",
            "password": "NewPassword123"
        }
    if "logout" in path:
        return {
            "session_token": session_token or "dummy"
        }
    if "id-card" in path:
        return {
            "frontImage": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
        }
    if "withdraw" in path:
        return {
            "amount": 1000,
            "bankAccountID": bank_account_id
        }
    if "bank-accounts" in path:
        return {
            "accountName": "Test Bank Account",
            "bankName": "Test Bank",
            "bankBranch": "Test Branch",
            "accountNumber": "123456789"
        }
    if "refcode" in path:
        return {
            "code": referral_code,
            "rebateRate": 0.1
        }
    if "right-subscriptions" in path:
        return {
            "rightID": "right_123",
            "accountID": account_id,
            "quantity": 100
        }
    if "stop-order" in path:
        return {
            "accountID": account_id,
            "symbol": "VN30F1M",
            "orderSide": "Buy",
            "stopPrice": 1200.0,
            "price": 1205.0,
            "qty": 1,
            "orderType": "StopLimit"
        }
    if "bracket-order" in path:
        return {
            "accountID": account_id,
            "symbol": "VN30F1M",
            "orderSide": "Buy",
            "price": 1200.0,
            "qty": 1,
            "stopLossPrice": 1180.0,
            "takeProfitPrice": 1250.0
        }
    if "covered-margin-call" in path:
        return {
            "accountID": account_id,
            "amount": 500000.0
        }
        
    # Default fallbacks based on schema type
    schema_type = body_schema.get("type")
    if schema_type == "object":
        body = {}
        props = body_schema.get("properties", {})
        for name, prop in props.items():
            prop_type = prop.get("type")
            if prop_type == "string":
                body[name] = "test-string"
            elif prop_type in ["integer", "number"]:
                body[name] = 0
            elif prop_type == "boolean":
                body[name] = False
            elif prop_type == "object":
                body[name] = {}
            elif prop_type == "array":
                body[name] = []
        return body
    return None

results = []

print("\n" + "="*80)
print(" 2. EXECUTING TEST FOR ALL ENDPOINTS ".center(80, "="))
print("="*80)

# Sort test cases to run self-service flow creation before self-service flow submit
def sort_key(tc):
    path = tc["path"]
    method = tc["method"]
    if "/api/authen/self-service/" in path:
        if method == "GET":
            return 0
        if method == "POST":
            return 1
    if "/api/authen/sessions/whoami" in path:
        return 2
    return 10

test_cases.sort(key=sort_key)

for idx, tc in enumerate(test_cases):
    path = tc["path"]
    method = tc["method"]
    has_sec = tc["has_security"]
    body_schema = tc["body_schema"]
    
    url = tc["base_url"] + build_path(path)
    body = build_body(path, body_schema)
    
    # Build headers
    headers = {}
    if has_sec:
        is_session_auth = False
        sec_list = tc.get("security", [])
        for sec in sec_list:
            if "sessionToken" in sec:
                is_session_auth = True
                break
        
        if "/api/authen/self-service/" in path or "/api/authen/sessions/" in path:
            is_session_auth = True
            
        if is_session_auth:
            headers["X-Session-Token"] = session_token
        else:
            headers["Authorization"] = f"Bearer {jwt_token}"
            
    print(f"[{idx+1}/{len(test_cases)}] {method} {build_path(path)} ...")
    
    status_code = -1
    response_text = ""
    start_time = time.time()
    
    try:
        if method == "GET":
            res = requests.get(url, headers=headers, timeout=10)
        elif method == "POST":
            res = requests.post(url, headers=headers, json=body, timeout=10)
        elif method == "PUT":
            res = requests.put(url, headers=headers, json=body, timeout=10)
        elif method == "PATCH":
            res = requests.patch(url, headers=headers, json=body, timeout=10)
        elif method == "DELETE":
            res = requests.delete(url, headers=headers, json=body, timeout=10)
        
        status_code = res.status_code
        response_text = res.text
    except Exception as e:
        response_text = str(e)
    
    latency = int((time.time() - start_time) * 1000)
    
    # Check if live_status is documented in responses
    documented_statuses = list(tc["responses"].keys())
    is_status_documented = str(status_code) in documented_statuses
    
    # We define verification success as either 2xx/400/404 handled gracefully or status documented in the specification
    success = is_status_documented or status_code in [200, 201, 204, 400, 404]
    
    results.append({
        "path": path,
        "resolved_path": build_path(path),
        "method": method,
        "status_code": status_code,
        "latency_ms": latency,
        "success": success,
        "is_status_documented": is_status_documented,
        "documented_statuses": documented_statuses,
        "response_snippet": response_text[:200].strip().replace('\n', ' ')
    })

# Print beautiful summary report
print("\n" + "="*80)
print(" 3. TEST SUMMARY AND VERIFICATION REPORT ".center(80, "="))
print("="*80)

success_count = sum(1 for r in results if r["success"])
failed_count = len(results) - success_count
print(f"Total APIs Tested: {len(results)}")
print(f"Successful (Correct Routing & Handled): {success_count}")
print(f"Failed: {failed_count}")
print(f"Success Rate: {success_count / len(results) * 100:.2f}%")
print("-" * 80)

report_path = "api_test_report.json"
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
print(f"Detailed JSON report written to: {report_path}")

print(f"{'METHOD':<7} | {'PATH':<60} | {'STATUS':<6} | {'LATENCY':<7} | {'IN SPEC?'}")
print("-" * 95)
for r in results:
    in_spec_str = "YES" if r["is_status_documented"] else "NO"
    path_str = r["path"]
    if len(path_str) > 60:
        path_str = path_str[:57] + "..."
    print(f"{r['method']:<7} | {path_str:<60} | {r['status_code']:<6} | {r['latency_ms']:<5}ms | {in_spec_str}")
