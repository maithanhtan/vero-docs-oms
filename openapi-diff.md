# OpenAPI diff: openapi_new.json vs openapi.json

Comparison uses effective paths: server base paths are applied, and path parameter names are normalized so `{orderID}` and `{orderId}` are treated as the same shape.

## Summary

| File | Operations |
|---|---:|
| openapi.json | 44 |
| openapi_new.json | 219 |
| Common after normalization | 26 |
| In openapi_new.json only | 193 |
| In openapi.json only | 18 |

## New-only count by tag

- Admin: 36
- Basket: 27
- Strategy: 20
- NeutralMM: 16
- Algo: 13
- Hedger: 13
- Market Data: 12
- OAuth2 Proxy: 9
- Orders: 8
- Broker: 6
- Connections: 6
- Accounts: 5
- Insight: 5
- Strategy Chat: 5
- Watchlist: 4
- Metrics: 3
- Micro Market Data: 3
- External: 2

## Old-only count by tag

- Auth: 10
- Static Assets: 3
- History: 2
- Market Data: 2
- Diagnostics: 1

## In openapi_new.json but not in openapi.json (193)

### Accounts (5)
- `GET /api/v1/bank-accounts/{bankId}` — Get bank account by ID
- `GET /api/v1/users/right-subscriptions` — List current user right subscription requests
- `PATCH /api/v1/users/covered-margin-call` — Adjust covered margin call amount
- `POST /api/v1/users/accounts/{accountId}/equity` — Increase account equity
- `POST /api/v1/users/right-subscriptions` — Subscribe to a right offering

### Admin (36)
- `DELETE /api/v1/admin/dividends/{id}` — Admin delete dividend
- `DELETE /api/v1/admin/margin-ratios/product-group/{productGroup}` — Admin delete product group margin ratio
- `DELETE /api/v1/admin/margin-ratios/symbol/{symbol}` — Admin delete symbol margin ratio
- `DELETE /api/v1/admin/short-sell-stock/{symbol}` — Admin delete short sell stock inventory
- `GET /api/v1/admin/accounts` — Admin list accounts
- `GET /api/v1/admin/dividends` — Admin list dividends
- `GET /api/v1/admin/margin-ratios` — Admin get all margin ratios
- `GET /api/v1/admin/orders/{startTimeMs}/{endTimeMs}` — Admin get orders in range
- `GET /api/v1/admin/positions` — Admin get all positions
- `GET /api/v1/admin/right-subscriptions` — Admin list right subscription rules
- `GET /api/v1/admin/right-subscriptions/requests` — Admin list right subscription requests
- `GET /api/v1/admin/settings` — Admin get settings
- `GET /api/v1/admin/short-sell-stock` — Admin list short sell stock inventory
- `GET /api/v1/admin/short-sell-stock/{symbol}` — Admin get short sell stock inventory by symbol
- `GET /api/v1/admin/short-sell-stock/audit` — Admin get short sell lend audit
- `GET /api/v1/admin/trades/{startTimeMs}/{endTimeMs}` — Admin get trades in range
- `GET /api/v1/admin/transactions/{startTimeMs}/{endTimeMs}` — Admin get transactions in range
- `GET /api/v1/admin/users/{userId}/accounts` — Admin get accounts for user
- `GET /api/v1/admin/users/{userId}/refcode` — Admin get user ref code
- `GET /api/v1/admin/users/search` — Admin search users
- `PATCH /api/v1/admin/transactions-update/{transactionId}/complete` — Admin mark transaction complete
- `POST /api/v1/admin/account-analytics` — Admin get account analytics with filters
- `POST /api/v1/admin/demo/accounts/{demoUserId}/trading-power` — Admin deposit demo trading power
- `POST /api/v1/admin/dividends` — Admin create dividend
- `POST /api/v1/admin/dividends/execute` — Admin execute pending dividends
- `POST /api/v1/admin/force-close-all` — Admin force close all open positions
- `POST /api/v1/admin/positions/close` — Admin close all positions for a symbol at a price
- `POST /api/v1/admin/right-subscriptions` — Admin create right subscription rule
- `POST /api/v1/admin/right-subscriptions/requests/{id}/approve` — Admin approve right subscription request
- `POST /api/v1/admin/right-subscriptions/requests/{id}/reject` — Admin reject right subscription request
- `POST /api/v1/admin/short-sell-stock/process-releases` — Admin process pending short-sell stock releases
- `PUT /api/v1/admin/margin-ratios/product-group/{productGroup}` — Admin upsert margin ratio for product group
- `PUT /api/v1/admin/margin-ratios/symbol/{symbol}` — Admin upsert margin ratio for symbol
- `PUT /api/v1/admin/settings` — Admin update settings
- `PUT /api/v1/admin/short-sell-stock/{symbol}` — Admin upsert short sell stock inventory
- `PUT /api/v1/admin/users/{userId}/refcode` — Admin set user ref code

### Algo (13)
- `GET /api/v1/admin/Algo/GetAlgoLogByName/{algoInstanceId}/{userId}` — Admin get algo logs for a user
- `GET /api/v1/admin/Algo/GetAlgoPositionOrderByName/{algoInstanceId}/{algoPosition}/{userId}` — Admin get algo position orders for a user
- `GET /api/v1/admin/Algo/GetAllAlgoMaster/{userId}` — Admin get all algo masters for a user
- `GET /api/v1/Algo/GetAlgoLogByName/{algoInstanceId}` — Get algo logs
- `GET /api/v1/Algo/GetAlgoMasterByID/{algoInstanceId}` — Get algo master by ID
- `GET /api/v1/Algo/GetAlgoPositionOrderByName/{algoInstanceId}/{algoPosition}` — Get algo position orders
- `GET /api/v1/Algo/GetAllAlgoMaster` — Get all algo masters for current user
- `POST /api/v1/Algo/CancelOrder/{algoInstanceId}/{orderId}` — Cancel order inside an algo
- `POST /api/v1/Algo/CreateAndStartNewAlgo` — Create and start execution algo
- `POST /api/v1/Algo/HoldAlgo/{algoId}` — Hold/pause algo
- `POST /api/v1/Algo/StopAlgo/{algoId}` — Stop algo
- `POST /api/v1/Algo/UnHoldAlgo/{algoId}` — Resume held algo
- `POST /api/v1/Algo/UpdateAlgoOptions/{algoId}` — Update algo options

### Basket (27)
- `DELETE /api/v1/Basket/RemoveBasketLeg/{basketName}/{symbol}` — Remove basket leg
- `GET /api/v1/Basket/GetArbBubbleDataCsv` — Get all arbitrage bubble data as CSV
- `GET /api/v1/Basket/GetArbBubbleDataCsv/{basketName}` — Get arbitrage bubble data as CSV by basket
- `GET /api/v1/Basket/GetArbitrageDetections` — Get all arbitrage detections
- `GET /api/v1/Basket/GetArbitrageDetections/{basketName}` — Get arbitrage detections by basket
- `GET /api/v1/Basket/GetArbitrageDetections/{basketName}/{fromDate}` — Get arbitrage detections by basket and date
- `GET /api/v1/Basket/GetArbitrageDetectionsCsv/{basketName}` — Get arbitrage detections CSV
- `GET /api/v1/Basket/GetArbitrageDetectionsWithDate/{basketName}/{fromDate}` — Get arbitrage detections history from DB
- `GET /api/v1/Basket/GetArbitrageStats/{basketName}` — Get arbitrage stats
- `GET /api/v1/Basket/GetBasket` — Get all baskets
- `GET /api/v1/Basket/GetBasket/{basketName}` — Get basket by name
- `GET /api/v1/Basket/GetBubbleData` — Get all basket bubble data
- `GET /api/v1/Basket/GetBubbleData/{basketName}` — Get bubble data by basket
- `GET /api/v1/Basket/GetBubbleData/{basketName}/{type}/{way}` — Get basket bubble data by type and side
- `GET /api/v1/Basket/GetBubbleDataByBasket/{basketName}` — Get bubble data by basket (alternate endpoint)
- `GET /api/v1/Basket/GetBubbleDataCsv` — Get all bubble data as CSV
- `GET /api/v1/Basket/GetBubbleDataCsv/{basketName}` — Get basket bubble data as CSV
- `GET /api/v1/Basket/GetIndex` — Get all basket indices
- `GET /api/v1/Basket/GetIndex/{basketName}` — Get basket index
- `GET /api/v1/Basket/GetRoundingPerf` — Get all basket rounding performance
- `GET /api/v1/Basket/GetRoundingPerf/{basketName}` — Get basket rounding performance
- `GET /api/v1/Basket/TestDatabaseConnection` — Test basket DB connection
- `POST /api/v1/Basket/CreateBasket` — Create basket
- `POST /api/v1/Basket/ImportBasketFromCsv` — Import basket from CSV file
- `POST /api/v1/Basket/UpdateBasketComponentWeight/{basketName}/{symbol}/{newWeight}` — Update basket component weight
- `POST /api/v1/Basket/UpdateBasketComponentWeightV2/{basketName}/{symbol}/{newWeight}/{bidWeight}/{askWeight}` — Update basket component weight with bid/ask weights
- `POST /api/v1/Basket/UpdateCashComponent/{basketName}/{newCash}/{bidCash}/{askCash}/{ytdCash}` — Update basket cash component

### Broker (6)
- `DELETE /api/v1/broker/{brokerId}/accounts/{accountId}` — Remove account from broker
- `GET /api/v1/broker` — List brokers
- `GET /api/v1/broker/{brokerId}/accounts` — Get accounts managed by broker
- `GET /api/v1/broker/{brokerId}/accounts/{accountId}` — Get broker account by ID
- `POST /api/v1/broker/{brokerId}/accounts/{accountId}` — Add account to broker
- `POST /api/v1/broker/user/{userId}` — Set user as broker

### Connections (6)
- `DELETE /api/v1/{connectionType}/{connectionId}` — Delete a token connection
- `GET /api/v1/{connectionType}/{connectionId}/validate` — Validate a token connection
- `GET /api/v1/connections` — List current user token connections
- `POST /api/v1/{connectionType}/refresh` — Refresh token for a broker connection
- `POST /api/v1/connections` — Create a new token connection
- `POST /api/v1/connections/verify-otp` — Verify OTP and complete connection creation

### External (2)
- `GET /api/news_info` — Get latest Vietcap news by ticker
- `GET /cross/https:/query1.finance.yahoo.com/v8/finance/chart/{symbol}` — Fetch Yahoo Finance chart data through static CORS proxy

### Hedger (13)
- `GET /api/v1/Hedger/config` — Get hedger config
- `GET /api/v1/Hedger/executions` — Get hedger executions
- `GET /api/v1/Hedger/logs` — Get hedger logs
- `GET /api/v1/Hedger/report` — Get hedger aggregate report
- `POST /api/v1/Hedger/{algoId}/pause` — Pause hedger algo
- `POST /api/v1/Hedger/{algoId}/resume` — Resume hedger algo
- `POST /api/v1/Hedger/{algoId}/start` — Start hedger algo
- `POST /api/v1/Hedger/config/{algoId}` — Update hedger config using query parameters
- `POST /api/v1/Hedger/config/custom-delta/{algoId}` — Set custom delta for hedger config
- `POST /api/v1/Hedger/delta` — Calculate hedger delta history
- `POST /api/v1/Hedger/manual/hedge-trade` — Add manual hedge trade
- `POST /api/v1/Hedger/manual/warrant-trade/{algoId}` — Add manual warrant trade for hedger
- `POST /api/v1/Hedger/reload-config` — Reload hedger config

### Insight (5)
- `GET /api/v1/Insight/GetAllInsightReportLiquidation` — Get all insight liquidation reports
- `GET /api/v1/Insight/GetOpenTrades/{symbol}` — Get open trades by symbol
- `GET /api/v1/Insight/GetSymbolInsight/{symbol}/{startTime}/{endTime}/{breakOut}/{tradeSide}` — Get symbol insight signals
- `GET /api/v1/Insight/GetSymbolInsightReport/{symbol}/{startTime}/{endTime}/{breakOut}/{tradeSide}` — Get symbol insight report
- `GET /api/v1/trade-insights/{timeframe}/{startTime}/{endTime}` — Get trade insights

### Market Data (12)
- `GET /api/v1/MarketData/GetAllProductPTDeal/{symbol}` — Get all product put-through deals
- `GET /api/v1/MarketData/GetCompanyProfile/{symbol}` — Get company profile
- `GET /api/v1/MarketData/GetFutureCode/{futureType}` — Get futures codes
- `GET /api/v1/MarketData/GetMoneyFlow/{from}/{to}` — Get market money flow
- `GET /api/v1/MarketData/GetProductTradeLog/{symbol}/{startUnixTime}/{endUnixTime}` — Get product trade log in range
- `GET /api/v1/MarketData/GetProductTradeLogRange/{range}/{symbol}/{from}/{to}/{countBack}` — Get product trade log bars for TradingView
- `GET /api/v1/MarketData/GetProductTrend/{symbol}` — Get product trend
- `GET /api/v1/MarketData/GetTopVal/{maxDepth}/{exchange}/{productType}/{minVol}` — Get top value symbols
- `GET /api/v1/MarketData/GetTopVol/{maxDepth}/{exchange}/{productType}/{minVol}` — Get top volume symbols
- `GET /api/v1/MarketData/GetVNIndex/{index}` — Get VN index data
- `GET /api/v1/MarketData/HeatMap` — Get market heat map
- `POST /api/v1/MarketData/AddPriceAlert` — Add a price alert

### Metrics (3)
- `GET /api/v1/metrics/{metricType}/{symbol}/{country}` — Get metrics by type, symbol, and country
- `GET /api/v1/metrics/metrics_fundamental/all/vietnam` — Get Vietnam fundamental screener metrics
- `GET /api/v1/metrics/vero_insight/all/all` — Get Vero Insight metrics for all symbols

### Micro Market Data (3)
- `GET /GetGapValue/{symbol}/{type}/{from}` — Get gap value for a symbol
- `GET /GetOhlcvHis/{symbol}/{resolution}/{from}/{to}` — Get OHLCV history
- `GET /GetOhlcvHis/{symbol}/{resolution}/{from}/{to}/{countBack}` — Get OHLCV history with countBack

### NeutralMM (16)
- `DELETE /api/v1/NeutralMM/AlgoLifecycle/DeleteAlgo/{algoId}` — Delete NeutralMM algo
- `GET /api/v1/NeutralMM/AlgoExecutor/GetAlgoLogByName/{algoInstanceId}` — Get NeutralMM algo logs
- `GET /api/v1/NeutralMM/AlgoExecutor/GetAlgoMasterByID/{algoId}` — Get NeutralMM algo master by ID
- `GET /api/v1/NeutralMM/AlgoExecutor/GetAlgoPositionOrderByName/{algoInstanceId}/{algoPosition}` — Get NeutralMM algo position orders
- `GET /api/v1/NeutralMM/AlgoExecutor/GetAlgoPositionTradeByName/{algoInstanceId}/{algoPosition}` — Get NeutralMM algo position trades
- `GET /api/v1/NeutralMM/AlgoExecutor/GetRealtimeData/{algoInstanceId}` — Get NeutralMM realtime data
- `GET /api/v1/NeutralMM/AlgoQuery/GetAllAlgoMaster` — Get all NeutralMM algo masters
- `POST /api/v1/NeutralMM/AlgoConfig/CalculateIV` — Calculate implied volatility and greeks
- `POST /api/v1/NeutralMM/AlgoConfig/CheckTheoPrice` — Check theoretical price
- `POST /api/v1/NeutralMM/AlgoConfig/UpdateAlgoOptions/{algoId}` — Update NeutralMM algo options
- `POST /api/v1/NeutralMM/AlgoLifecycle/CreateAndStartNewAlgo` — Create and start NeutralMM/MarketMaking algo
- `POST /api/v1/NeutralMM/AlgoLifecycle/HoldAlgo/{algoId}` — Hold NeutralMM algo
- `POST /api/v1/NeutralMM/AlgoLifecycle/StartStoppedAlgo/{algoId}` — Start stopped NeutralMM algo
- `POST /api/v1/NeutralMM/AlgoLifecycle/StopAlgo/{algoId}` — Stop NeutralMM algo
- `POST /api/v1/NeutralMM/AlgoLifecycle/UnHoldAlgo/{algoId}` — Resume NeutralMM algo
- `POST /api/v1/NeutralMM/Order/CancelOrder/{algoId}/{internalOrderId}` — Cancel NeutralMM internal order

### OAuth2 Proxy (9)
- `GET /api/oauth2/auth` — Build Hydra OAuth2 authorization URL
- `GET /api/oauth2/consent` — Get or auto-accept Hydra consent request
- `GET /api/oauth2/login` — Get or auto-accept Hydra login request
- `GET /api/v1/oauth2-token` — Get stored OAuth2 token metadata for the current user
- `POST /api/oauth2/consent` — Accept Hydra consent request
- `POST /api/oauth2/exchange` — Exchange authorization code for OAuth2 tokens via Hydra
- `POST /api/oauth2/login` — Accept Hydra login request for authenticated identity
- `POST /api/oauth2/token` — Proxy OAuth2 token request to Hydra public token endpoint
- `POST /api/v1/oauth2-token` — Save OAuth2 access and refresh tokens for the current user

### Orders (8)
- `GET /api/v1/orders/bracket-order` — Get bracket orders with optional filters
- `GET /api/v1/orders/bracket-order/{bracketOrderId}` — Get bracket order by ID
- `GET /api/v1/orders/stop-order` — Get stop orders with optional filters
- `GET /api/v1/orders/stop-order/{orderId}` — Get stop order by ID
- `POST /api/v1/NeutralMM/Order/PlaceOrder` — Place a market-making order through NeutralMM
- `POST /api/v1/orders/bracket-order` — Place a bracket order
- `POST /api/v1/orders/stop-order` — Place a stop order
- `PUT /api/v1/orders/stop-order/{orderId}/modify` — Modify a stop order

### Strategy (20)
- `DELETE /api/v1/strategies/{strategyId}` — Delete a strategy
- `GET /api/v1/algo-mgt/health` — Check algo management service health
- `GET /api/v1/strategies` — List strategies for current user
- `GET /api/v1/strategies/{strategyId}` — Get a strategy by ID
- `GET /api/v1/strategies/{strategyId}/settings` — Get strategy runtime settings
- `GET /api/v1/strategies/events/{strategyId}` — Get callback events for a strategy
- `GET /api/v1/strategy-control/{strategyId}/logs` — Get strategy logs
- `GET /api/v1/strategy-control/{strategyId}/orders` — Get strategy orders
- `GET /api/v1/strategy-control/{strategyId}/progress` — Get strategy execution progress
- `GET /api/v1/strategy-control/{strategyId}/report` — Get strategy backtest/performance report
- `GET /api/v1/strategy-control/{strategyId}/sdk-status` — Get SDK status from running strategy
- `GET /api/v1/strategy-control/{strategyId}/status` — Get strategy execution status
- `GET /api/v1/strategy-control/{strategyId}/trades` — Get strategy trades
- `GET /api/v1/strategy-control/user` — List current user running strategy instances
- `POST /api/v1/strategies` — Create a strategy
- `POST /api/v1/strategies/{strategyId}/start` — Start a strategy in backtest or live mode
- `POST /api/v1/strategies/{strategyId}/stop` — Stop a running strategy
- `POST /api/v1/strategy-control/{strategyId}/sdk-stop` — Stop strategy through SDK internal API
- `PUT /api/v1/strategies/{strategyId}/name` — Rename a strategy
- `PUT /api/v1/strategies/{strategyId}/settings` — Update strategy runtime settings

### Strategy Chat (5)
- `GET /api/v1/chat/strategy/{sessionId}` — Get chat history for a session
- `GET /api/v1/strategy/chat/{strategyId}` — Get chat history by strategy ID
- `POST /api/tuning-algo-execution-settings` — Tune algorithm execution settings with chat service
- `POST /api/v1/chat/strategy` — Generate strategy code via chat (non-streaming)
- `POST /api/v1/chat/strategy/stream` — Stream strategy chat events as SSE

### Watchlist (4)
- `DELETE /api/v1/watchlist/{watchlistId}/{userId}` — Delete user watchlist
- `GET /api/v1/watchlist/user/{userId}` — Get user watchlists
- `GET /watchlists/{watchlistId}` — Fetch watchlist from legacy store endpoint
- `POST /api/v1/watchlist` — Create AI-generated user watchlist


## In openapi.json but not in openapi_new.json (18)

### Auth (10)
- `GET /api/authen/self-service/login/api` — Create a native login flow
- `GET /api/authen/self-service/recovery/api` — Create a recovery flow
- `GET /api/authen/self-service/registration/api` — Create a native registration flow
- `GET /api/authen/self-service/settings/api` — Create a settings flow for password change
- `GET /api/authen/sessions/whoami` — Get current session or tokenized JWT session
- `POST /api/authen/self-service/login` — Submit password credentials to a login flow
- `POST /api/authen/self-service/recovery` — Send or verify a recovery code
- `POST /api/authen/self-service/registration` — Submit registration data to a registration flow
- `POST /api/authen/self-service/settings` — Update password in a settings flow
- `POST /api/v1/auth/logout` — Logout current app session

### Diagnostics (1)
- `GET /api/v1/health` — Check backend health

### History (2)
- `GET /api/v1/users/accounts/{accountId}/commissions` — List account commissions
- `GET /api/v1/users/accounts/{accountId}/fees` — List account fees

### Market Data (2)
- `GET /api/v1/GetOhlcvHis/{symbol}/{resolution}/{fromMs}/{toMs}` — Get OHLCV history
- `GET /api/v1/GetOhlcvHis/{symbol}/{resolution}/{fromMs}/{toMs}/{countBack}` — Get OHLCV history with countBack

### Static Assets (3)
- `GET /api/v1/contract_customer_yixin.pdf` — Download customer contract PDF
- `GET /api/v1/logos/{symbol}.svg` — Get symbol SVG logo
- `GET /api/v1/user_guide_yixin.pdf` — Download user guide PDF

