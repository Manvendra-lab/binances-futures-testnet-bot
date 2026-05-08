# Binance Futures Testnet Trading Bot (CLI)

A simple Python 3.x command-line trading bot for **Binance USDT-M Futures Testnet**.  
The bot places **MARKET** and **LIMIT** orders (BUY and SELL) using validated CLI input, with a clean structure, logging of API calls, and basic error handling. [file:1]

---

## Features

- Place **MARKET** and **LIMIT** orders on **Binance Futures Testnet (USDT-M)**. [file:1]  
- Support both **BUY** and **SELL** sides. [file:1]  
- Accept and validate user input via CLI:
  - `symbol` (e.g. `BTCUSDT`)
  - `side` (`BUY` / `SELL`)
  - `order type` (`MARKET` / `LIMIT`)
  - `quantity`
  - `price` (required for `LIMIT`) [file:1]  
- Print clear output:
  - order request summary
  - order response details (`orderId`, `status`, `executedQty`, `avgPrice` if available)
  - success / failure message [file:1]  
- Log API requests, responses, and errors to `bot.log`. [file:1]

---

## Project Structure

```text
binance-futures-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # CLI input validation
│   └── logging_config.py  # Logging to file
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── .env                   # Local API keys (not committed)
└── README.md
```

This matches the suggested separation of **client/API layer** and **CLI layer** in the assignment. [file:1]

---

## Prerequisites

- Python 3.x installed. [file:1]  
- A **Binance Futures Testnet** account with an **API key** and **secret** (USDT-M Futures). [file:1]  

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>.git
cd binance-futures-bot
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Dependencies:

- `python-binance` – Binance Futures client. [file:1]  
- `python-dotenv` – load API keys from `.env`.

### 4. Configure API credentials

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
BINANCE_BASE_URL=https://testnet.binancefuture.com
```

- Keys must be from **Binance Futures Testnet**, not mainnet. [file:1]  
- `.env` is ignored by Git for safety.

---

## How to Run

All commands below assume your virtual environment is activated and you are in the project root.

### 1. MARKET order example

Place a **MARKET BUY** order:

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

Expected behavior:

- Input is validated.
- Request summary printed.
- MARKET order sent to Binance Futures Testnet.
- Response details (`orderId`, `status`, `executedQty`, `avgPrice`) printed if available. [file:1]

### 2. LIMIT order example

Place a **LIMIT SELL** order:

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 90000
```

Expected behavior:

- Input is validated (price required for LIMIT). [file:1]  
- Request summary printed including `price`.
- LIMIT order sent to Binance Futures Testnet.
- Response details printed.

### 3. Error handling examples

Invalid inputs show clean error messages, for example:

- Missing `--price` for `--order-type LIMIT`  
- Negative `--quantity`  
- Invalid `--side` (must be `BUY` or `SELL`) [file:1]

---

## Logging

The bot writes logs to `bot.log` in the project root using `logging_config.py`. [file:1]

Each order attempt logs:

- request payload (symbol, side, type, quantity, price if LIMIT)  
- HTTP/API response
- any exceptions or errors encountered [file:1]

These logs can be used to provide the required evidence of at least:

- one **MARKET** order
- one **LIMIT** order [file:1]

---

## Assumptions

- Only **USDT-Margined Futures** (USDT-M) on Binance Testnet are supported. [file:1]  
- Symbols are assumed to be valid Binance Futures symbols (e.g., `BTCUSDT`). Minimal symbol validation is performed; unknown symbols may result in Binance API errors. [file:1]  
- Only basic order types are implemented:
  - `MARKET`
  - `LIMIT`  
  Other optional order types (Stop-Limit, OCO, TWAP, Grid) mentioned as bonus in the assignment are not implemented. [file:1]  
- Quantity and price validation is limited to positive numeric checks; exchange-level rules (min step size, etc.) are enforced by Binance itself and may produce API errors. [file:1]  
- The bot is intended for **testnet only**, not for real-money trading.

---

## Notes

- This project is built for an application task and is intentionally minimal and focused on:
  - correctness of orders on Binance Futures Testnet,
  - input validation and error handling,
  - logging quality,
  - clear structure and CLI UX. [file:1]