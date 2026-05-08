def submit_order(client, symbol, side, order_type, quantity, price=None):
    return client.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )