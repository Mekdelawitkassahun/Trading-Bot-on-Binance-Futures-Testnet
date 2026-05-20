import argparse
import sys
from bot.logging_config import setup_logging
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager


def interactive_menu():
    print("=" * 50)
    print("BINANCE FUTURES TESTNET TRADING BOT")
    print("=" * 50)
    
    import inquirer
    
    questions = [
        inquirer.Text("symbol", message="Enter trading symbol", default="BTCUSDT"),
        inquirer.List("side", message="Select order side", choices=["BUY", "SELL"]),
        inquirer.List("order_type", message="Select order type", choices=["MARKET", "LIMIT"]),
        inquirer.Text("quantity", message="Enter order quantity"),
    ]
    
    answers = inquirer.prompt(questions)
    
    price = None
    if answers["order_type"] == "LIMIT":
        price_question = [inquirer.Text("price", message="Enter order price")]
        price_answer = inquirer.prompt(price_question)
        price = price_answer["price"]
    
    return {
        "symbol": answers["symbol"],
        "side": answers["side"],
        "order_type": answers["order_type"],
        "quantity": answers["quantity"],
        "price": price
    }


def main():
    logger = setup_logging()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive menu mode")
    parser.add_argument("--symbol", help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side (BUY or SELL)")
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], dest="order_type", help="Order type (MARKET or LIMIT)")
    parser.add_argument("--quantity", help="Order quantity")
    parser.add_argument("--price", help="Order price (required for LIMIT orders)")
    
    args = parser.parse_args()
    
    try:
        client = BinanceFuturesClient()
        order_manager = OrderManager(client)
        
        if args.interactive:
            order_data = interactive_menu()
            order_manager.place_order(**order_data)
        else:
            if not all([args.symbol, args.side, args.order_type, args.quantity]):
                parser.error("All required arguments (--symbol, --side, --type, --quantity) must be provided when not using --interactive mode")
            order_manager.place_order(
                symbol=args.symbol,
                side=args.side,
                order_type=args.order_type,
                quantity=args.quantity,
                price=args.price
            )
        return 0
    except Exception as e:
        logger.error("Application error: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
