#!/bin/bash
set -e

# Download nlohmann/json single header if not present
if [ ! -f json.hpp ]; then
    echo "Downloading nlohmann/json..."
    curl -sLo json.hpp https://github.com/nlohmann/json/releases/download/v3.11.3/json.hpp
fi

# Clone and compile ixwebsocket locally
if [ ! -d IXWebSocket ]; then
    echo "Cloning IXWebSocket..."
    git clone --depth 1 https://github.com/machinezone/IXWebSocket.git
fi

if [ ! -f libixwebsocket.a ]; then
    echo "Building IXWebSocket..."
    mkdir -p IXWebSocket/build
    cd IXWebSocket/build
    cmake -DUSE_TLS=ON -DOPENSSL_ROOT_DIR=/opt/homebrew/opt/openssl@3 ..
    make -j4
    cd ../..
    cp IXWebSocket/build/libixwebsocket.a .
fi

# Create test code file (copying from snippets/streaming/product-info-samples.mdx)
cat << 'EOF' > main.cpp
#include <ixwebsocket/IXWebSocket.h>
#include <ixwebsocket/IXNetSystem.h>
#include "json.hpp"
#include <iostream>
#include <sstream>
#include <string>
#include <thread>
#include <chrono>

using json = nlohmann::json;

int main() {
    // Required on Windows, no-op on other systems
    ix::initNetSystem();

    std::string stream_url = "wss://streaming.verolabs.co/connection/websocket";
    std::string channel = "mkt:productInfo:VN30F1M-G1";

    ix::WebSocket webSocket;
    webSocket.setUrl(stream_url);

    int request_id = 1;
    bool connected = false;
    bool subscribed = false;

    auto send_command = [&webSocket](const json& command) {
        if (command.empty()) {
            webSocket.send("\n");
        } else {
            webSocket.send(command.dump() + "\n");
        }
    };

    webSocket.setOnMessageCallback([&](const ix::WebSocketMessagePtr& msg) {
        if (msg->type == ix::WebSocketMessageType::Open) {
            std::cout << "[TEST] Connection opened, sending connect handshake..." << std::endl;
            send_command({
                {"id", request_id++},
                {"connect", json::object()}
            });
        }
        else if (msg->type == ix::WebSocketMessageType::Message) {
            std::stringstream ss(msg->str);
            std::string raw;
            while (std::getline(ss, raw, '\n')) {
                if (raw.empty()) continue;

                try {
                    json reply = json::parse(raw);
                    std::cout << "[TEST] Received payload: " << reply.dump() << std::endl;

                    if (reply.empty()) {
                        send_command(json::object());
                        continue;
                    }

                    if (reply.contains("connect") && !reply.contains("error")) {
                        std::cout << "[TEST] Handshake success! Subscribing to channel: " << channel << std::endl;
                        connected = true;
                        send_command({
                            {"id", request_id++},
                            {"subscribe", {{"channel", channel}}}
                        });
                        continue;
                    }

                    if (reply.contains("subscribe") && !reply.contains("error")) {
                        std::cout << "[TEST] Subscription success!" << std::endl;
                        subscribed = true;
                        std::cout << "[TEST] SUCCESS! Exiting in 1 second..." << std::endl;
                        std::this_thread::sleep_for(std::chrono::seconds(1));
                        exit(0);
                    }

                    if (reply.contains("push")) {
                        auto push = reply["push"];
                        if (push.value("channel", "") == channel && push.contains("pub")) {
                            auto pub = push["pub"];
                            if (pub.contains("data")) {
                                std::cout << "[TEST] Push Data: " << pub["data"].dump() << std::endl;
                                exit(0);
                            }
                        }
                    }
                } catch (const std::exception& e) {
                    std::cerr << "[TEST] Parse error: " << e.what() << std::endl;
                }
            }
        }
        else if (msg->type == ix::WebSocketMessageType::Error) {
            std::cerr << "[TEST] Error: " << msg->errorInfo.reason << std::endl;
            exit(1);
        }
    });

    webSocket.start();

    // Loop for max 10 seconds, then fail if no success
    for (int i = 0; i < 10; ++i) {
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    std::cerr << "[TEST] Timeout waiting for connection/subscription" << std::endl;
    webSocket.stop();
    return 1;
}
EOF

# Compile
echo "Compiling main.cpp..."
clang++ -std=c++17 -O2 main.cpp libixwebsocket.a \
    -IIXWebSocket \
    -I. \
    -I/opt/homebrew/opt/openssl@3/include \
    -L/opt/homebrew/opt/openssl@3/lib \
    -lssl -lcrypto -lz \
    -framework Security -framework CoreFoundation \
    -lpthread -o wss_test

echo "Running test binary..."
./wss_test
