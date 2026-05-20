from typing import Optional


class ValidationError(Exception):
    pass


def validate_symbol(symbol: str) -> str:
    symbol = symbol.strip().upper()
    if not symbol:
        raise ValidationError("Symbol cannot be empty")
    return symbol


def validate_side(side: str) -> str:
    side = side.strip().upper()
    if side not in ["BUY", "SELL"]:
        raise ValidationError("Side must be either BUY or SELL")
    return side


def validate_order_type(order_type: str) -> str:
    order_type = order_type.strip().upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValidationError("Order type must be either MARKET or LIMIT")
    return order_type


def validate_quantity(quantity: str) -> float:
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValidationError("Quantity must be greater than 0")
        return qty
    except ValueError:
        raise ValidationError("Quantity must be a valid number")


def validate_price(price: Optional[str], order_type: str) -> Optional[float]:
    if order_type == "LIMIT":
        if not price:
            raise ValidationError("Price is required for LIMIT orders")
        try:
            p = float(price)
            if p <= 0:
                raise ValidationError("Price must be greater than 0")
            return p
        except ValueError:
            raise ValidationError("Price must be a valid number")
    return None
