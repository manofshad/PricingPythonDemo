# Resolved version of app/services/pricing.py
# This combines features from both Bob's and Alice's versions.
# It includes shipping costs, loyalty discount tiers, bulk pricing tiers, and quantity validation.

def calculate_price(subtotal: float, tax_rate: float, discount_percent: float = 0.0, 
                    quantity: int = 1, shipping_cost: float = 0.0, loyalty_tier: str = "standard") -> float:
    """
    Calculate final total with bulk pricing, loyalty discounts, regular discount, shipping, and tax.
    - subtotal: pre-tax amount per item
    - tax_rate: 0.08875 means 8.875%
    - discount_percent: 10 means 10% off (applies after loyalty and bulk)
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

    # Calculate total subtotal based on quantity
    total_subtotal_before_discounts = subtotal * quantity

    # Apply loyalty discount
    loyalty_discount_rate = 0.0
    if loyalty_tier == "vip":
        loyalty_discount_rate = 0.20  # 20% off for VIP
    elif loyalty_tier == "premium":
        loyalty_discount_rate = 0.10  # 10% off for Premium
    # standard tier gets no loyalty discount

    # Apply loyalty discount first
    loyalty_discounted_amount = total_subtotal_before_discounts * (1 - loyalty_discount_rate)

    # Apply bulk pricing tiers (after loyalty, as loyalty is customer-specific, bulk is order-specific)
    bulk_discount_rate = 0.0
    if quantity >= 100:
        bulk_discount_rate = 0.15  # 15% off for 100+ items
    elif quantity >= 50:
        bulk_discount_rate = 0.10  # 10% off for 50+ items
    elif quantity >= 10:
        bulk_discount_rate = 0.05  # 5% off for 10+ items

    bulk_discounted_amount = loyalty_discounted_amount * (1 - bulk_discount_rate)
    
    # Apply regular discount (after loyalty and bulk)
    discounted_total = bulk_discounted_amount * (1 - discount_percent / 100.0)
    
    # Add shipping
    with_shipping = discounted_total + shipping_cost
    
    # Apply tax
    taxed_total = with_shipping * (1 + tax_rate)
    return round(taxed_total, 2)