def calculate_price(subtotal: float, tax_rate: float, discount_percent: float = 0.0) -> float:
    """
    Calculate final total with a simple percent discount and tax.
    - subtotal: pre-tax amount
    - tax_rate: 0.08875 means 8.875%
    - discount_percent: 10 means 10% off
    """
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")

    discounted = subtotal * (1 - discount_percent / 100.0)
    taxed = discounted * (1 + tax_rate)
    return round(taxed, 2)
