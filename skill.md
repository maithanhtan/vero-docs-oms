---
name: vero-oms-api
description: Implement integrations against the Vero OMS REST and Streaming APIs using the published OpenAPI and documentation.
license: Proprietary
compatibility: Works with HTTP clients, OpenAPI-aware tools, and AI agents that can read Vero OMS API docs, OpenAPI JSON, or MCP search results.
metadata:
  version: "1.0"
  source: "Vero OMS API documentation"
---

# Vero OMS API Integration Skill

Use this skill when implementing a client, test, workflow, or debugging flow for the Vero OMS API.

## Source of truth

- REST API specification: `/openapi.docs.en.json` or `/openapi.docs.vi.json`
- REST docs contain 47 unique HTTP operations.
- Streaming docs describe WebSocket channel patterns for market, order, account, and notification events.

## Rules for agents

1. Use the OpenAPI operation method and path exactly.
2. Do not invent request or response fields.
3. Treat every documented parameter type, required flag, enum, and response field description as authoritative.
4. Use `Authorization: Bearer <token>` for protected REST endpoints unless the endpoint explicitly documents `x-session-token`.
5. Use `x-session-token` for session endpoints that require a browser/session.
6. Parse documented success responses and also handle JSON error bodies, Problem Details, and plain text errors.
7. Do not use removed endpoints such as account commissions and fees.
8. For order placement responses, treat `data` as the service-generated system id:
   - normal order: `ORDER-...`
   - stop order: `STOP-...`
   - bracket order: `BRACKET-...`
9. For market data responses, do not treat `data` as `any`; use the typed schema under each endpoint.

## Common workflow

1. Identify the endpoint by operationId, method, path, or user goal.
2. Read all parameters and request body schema.
3. Build the HTTP request with the documented auth header.
4. Validate input types before sending.
5. Parse the response into typed objects using the documented schema.
6. If live behavior differs from the spec, report the mismatch and include method, URL, status, and response body.

## MCP and AI context

The Vero OMS API docs MCP server is available at:

```text
https://docs.oms.verolabs.co/mcp
```

Use MCP for searching and retrieving documentation context. Use OpenAPI JSON for exact implementation details.
