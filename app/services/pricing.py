# Bob's version of app/services/pricing.py
# This adds shipping costs and loyalty discount tiers

def calculate_price(subtotal: float, tax_rate: float, discount_percent: float = 0.0, shipping_cost: float = 0.0, loyalty_tier: str = "standard") -> float:
    """
    Calculate final total with shipping costs and loyalty discounts.
    - subtotal: pre-tax amount
    - tax_rate: 0.08875 means 8.875%
    - discount_percent: 10 means 10% off
    - shipping_cost: additional shipping fee
    - loyalty_tier: "standard", "premium", or "vip" for loyalty discounts
    """
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")
    if shipping_cost < 0:
        raise ValueError("shipping_cost cannot be negative")

    # Apply loyalty discount
    loyalty_discount = 0.0
    if loyalty_tier == "vip":
        loyalty_discount = 0.20  # 20% off for VIP
    elif loyalty_tier == "premium":
        loyalty_discount = 0.10  # 10% off for Premium
    # standard tier gets no loyalty discount

    # Apply loyalty discount first
    loyalty_discounted = subtotal * (1 - loyalty_discount)
    
    # Apply regular discount
    discounted = loyalty_discounted * (1 - discount_percent / 100.0)
    
    # Add shipping
    with_shipping = discounted + shipping_cost
    
    # Apply tax
    taxed = with_shipping * (1 + tax_rate)
    return round(taxed, 2)
