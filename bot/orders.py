import logging
from typing import Optional
from .client import BinanceFuturesClient
from .validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    ValidationError
)


class OrderManager:
    def __init__(self, client: BinanceFuturesClient):
        self.client = client
        self.logger = logging.getLogger(__name__)
    
    def place_order(self, symbol: str, side: str, order_type: str, quantity: str, price: Optional[str] = None):
        try:
            validated_symbol = validate_symbol(symbol)
            validated_side = validate_side(side)
            validated_order_type = validate_order_type(order_type)
            validated_quantity = validate_quantity(quantity)
            validated_price = validate_price(price, validated_order_type)
            
            self.logger.info("Order request summary:")
            self.logger.info("  Symbol: %s", validated_symbol)
            self.logger.info("  Side: %s", validated_side)
            self.logger.info("  Type: %s", validated_order_type)
            self.logger.info("  Quantity: %s", validated_quantity)
            if validated_price is not None:
                self.logger.info("  Price: %s", validated_price)
            
            order = self.client.place_order(
                symbol=validated_symbol,
                side=validated_side,
                order_type=validated_order_type,
                quantity=validated_quantity,
                price=validated_price
            )
            
            print("\n" + "="*50)
            print("ORDER PLACED SUCCESSFULLY")
            print("="*50)
            print(f"Order ID: {order.get('orderId')}")
            print(f"Symbol: {order.get('symbol')}")
            print(f"Side: {order.get('side')}")
            print(f"Type: {order.get('type')}")
            print(f"Status: {order.get('status')}")
            print(f"Executed Qty: {order.get('executedQty')}")
            if 'avgPrice' in order:
                print(f"Avg Price: {order.get('avgPrice')}")
            print("="*50 + "\n")
            
            return order
        
        except ValidationError as e:
            self.logger.error("Validation error: %s", e)
            print(f"\nERROR: {e}\n")
            raise
        except Exception as e:
            self.logger.error("Failed to place order: %s", e)
            print(f"\nERROR: Failed to place order - {e}\n")
            raise
