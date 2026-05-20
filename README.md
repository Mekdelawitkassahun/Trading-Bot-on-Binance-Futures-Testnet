# Binance Futures Testnet Trading Bot

A simplified trading bot for placing orders on Binance Futures Testnet (USDT-M).

## Setup

1. **Create a Binance Futures Testnet Account**:
   - Go to https://testnet.binancefuture.com
   - Register and activate your account

2. **Generate API Credentials**:
   - Log in to Binance Futures Testnet
   - Go to API Management
   - Create a new API key and secret

3. **Set Environment Variables**:
   ```powershell
   # Windows
   $env:BINANCE_API_KEY="your_api_key"
   $env:BINANCE_API_SECRET="your_api_secret"
   ```

   ```bash
   # Linux/Mac
   export BINANCE_API_KEY="your_api_key"
   export BINANCE_API_SECRET="your_api_secret"
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Interactive Menu Mode (Bonus Feature)
For a user-friendly interactive experience:
```bash
python cli.py --interactive
# or
python cli.py -i
```
This will guide you through a series of prompts to select your order parameters.

### Command-Line Arguments Mode

#### Market Order Example
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

#### Limit Order Example
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

## Project Structure
```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance client wrapper
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   └── logging_config.py
├── cli.py               # CLI entry point (with interactive mode)
├── README.md
└── requirements.txt
```

## Assumptions
- Using Binance Futures Testnet (USDT-M)
- Orders are placed with GTC (Good Till Cancel) time in force for LIMIT orders
- API credentials are provided via environment variables
- Symbol, side, order type, and quantity are required parameters
- Price is required only for LIMIT orders

## Logs
Logs are stored in the `logs/` directory with the filename `trading_bot.log`.
