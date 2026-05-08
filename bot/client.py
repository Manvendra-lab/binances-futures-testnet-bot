import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.logging_config import get_logger


class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str, base_url: str):
        self.logger = get_logger(__name__)
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = base_url

    def place_order(self, symbol, side, order_type, quantity, price=None):
        payload = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            payload["price"] = price
            payload["timeInForce"] = "GTC"

        self.logger.info(f"Placing order: {payload}")

        try:
            response = self.client.futures_create_order(**payload)
            self.logger.info(f"API response: {response}")

            return {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice", "N/A")
            }

        except (BinanceAPIException, BinanceRequestException) as e:
            self.logger.error(f"Binance error: {str(e)}")
            raise Exception(f"Binance error: {str(e)}")

        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            raise Exception(f"Unexpected error: {str(e)}")