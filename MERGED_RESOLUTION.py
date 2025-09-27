# Suggested merged resolution combining both features
# This is what the AI should aim to produce

def calculate_price(
    subtotal: float, 
    tax_rate: float, 
    discount_percent: float = 0.0, 
    quantity: int = 1,
    shipping_cost: float = 0.0, 
    loyalty_tier: str = "standard"
) -> float:
    """
    Calculate final total with bulk pricing, loyalty discounts, shipping, and tax.
    - subtotal: pre-tax amount per item
    - tax_rate: 0.08875 means 8.875%
    - discount_percent: 10 means 10% off
    - quantity: number of items for bulk pricing
    - shipping_cost: additional shipping fee
    - loyalty_tier: "standard", "premium", or "vip" for loyalty discounts
    """
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    if shipping_cost < 0:
        raise ValueError("shipping_cost cannot be negative")

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
    
    # Apply loyalty discount
    loyalty_discount = 0.0
    if loyalty_tier == "vip":
        loyalty_discount = 0.20  # 20% off for VIP
    elif loyalty_tier == "premium":
        loyalty_discount = 0.10  # 10% off for Premium
    # standard tier gets no loyalty discount

    # Apply loyalty discount
    loyalty_discounted = bulk_discounted * (1 - loyalty_discount)
    
    # Apply regular discount
    discounted = loyalty_discounted * (1 - discount_percent / 100.0)
    
    # Add shipping
    with_shipping = discounted + shipping_cost
    
    # Apply tax
    taxed = with_shipping * (1 + tax_rate)
    return round(taxed, 2)
