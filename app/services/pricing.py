def calculate_price(subtotal: float, tax_rate: float, discount_percent: float = 0.0, quantity: int = 1) -> float:
    """
    Calculate final total with bulk pricing tiers, discount and tax.
    - subtotal: pre-tax amount per item
    - tax_rate: 0.08875 means 8.875%
    - discount_percent: 10 means 10% off
    - quantity: number of items for bulk pricing
    """
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")
    if quantity < 1:
        raise ValueError("quantity must be at least 1")

    # Apply bulk pricing tiers
    if quantity >= 100:
        bulk_discount = 0.15  # 15% off for 100+ items
    elif quantity >= 50:
        bulk_discount = 0.10  # 10% off for 50+ items
    elif quantity >= 10:
        bulk_discount = 0.05  # 5% off for 10+ items
    else:
        bulk_discount = 0.0

    # Calculate total with bulk discount
    total_subtotal = subtotal * quantity
    bulk_discounted = total_subtotal * (1 - bulk_discount)
    
    # Apply regular discount
    discounted = bulk_discounted * (1 - discount_percent / 100.0)
    
    # Apply tax
    taxed = discounted * (1 + tax_rate)
    return round(taxed, 2)
