import argparse
import os
from dotenv import load_dotenv

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import get_logger
from bot.client import BinanceFuturesClient
from bot.orders import submit_order


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--order-type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price required for LIMIT orders")

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\nOrder Request Summary")
        print("---------------------")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Order Type : {order_type}")
        print(f"Quantity   : {quantity}")
        if order_type == "LIMIT":
            print(f"Price      : {price}")

        load_dotenv()
        logger = get_logger(__name__)

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        base_url = os.getenv("BINANCE_BASE_URL")

        client = BinanceFuturesClient(api_key, api_secret, base_url)
        result = submit_order(client, symbol, side, order_type, quantity, price)

        print("\nOrder Response")
        print("--------------")
        print(f"orderId     : {result['orderId']}")
        print(f"status      : {result['status']}")
        print(f"executedQty : {result['executedQty']}")
        print(f"avgPrice    : {result['avgPrice']}")
        print("\nSuccess: Order placed successfully.")

    except Exception as e:
        print(f"\nFailure: {e}")


if __name__ == "__main__":
    main()