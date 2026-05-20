import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException


class BinanceFuturesClient:
    def __init__(self, api_key: str = None, api_secret: str = None, testnet: bool = True):
        self.logger = logging.getLogger(__name__)
        
        api_key = api_key or os.getenv("BINANCE_API_KEY")
        api_secret = api_secret or os.getenv("BINANCE_API_SECRET")
        
        if not api_key or not api_secret:
            raise ValueError("API key and secret must be provided either as parameters or environment variables")
        
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            self.client.API_URL = "https://testnet.binancefuture.com/fapi"
        
        self.logger.info("Binance Futures client initialized (testnet: %s)", testnet)
    
    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        try:
            self.logger.info("Placing order: symbol=%s, side=%s, type=%s, quantity=%s, price=%s",
                           symbol, side, order_type, quantity, price)
            
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }
            
            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"
            
            order = self.client.futures_create_order(**params)
            
            self.logger.info("Order placed successfully: %s", order)
            return order
        
        except BinanceAPIException as e:
            self.logger.error("Binance API error: %s", e)
            raise
        except BinanceRequestException as e:
            self.logger.error("Network request error: %s", e)
            raise
        except Exception as e:
            self.logger.error("Unexpected error placing order: %s", e)
            raise
