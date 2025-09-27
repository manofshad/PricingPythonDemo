# Resolved version of app/services/pricing.py
# This combines bulk pricing, loyalty discounts, shipping costs, and tax

def calculate_price(subtotal_per_item: float, quantity: int, tax_rate: float, discount_percent: float = 0.0, shipping_cost: float = 0.0, loyalty_tier: str = "standard") -> float:
    """
    Calculate final total with bulk pricing tiers, loyalty discounts, shipping, and tax.
    - subtotal_per_item: pre-tax amount for a single item
    - quantity: number of items for bulk pricing
    - tax_rate: 0.08875 means 8.875%
    - discount_percent: 10 means 10% off (applies before loyalty)
    - shipping_cost: additional shipping fee
    - loyalty_tier: "standard", "premium", or "vip" for loyalty discounts (applies after regular discount)
    """
    if subtotal_per_item < 0:
        raise ValueError("subtotal_per_item cannot be negative")
    if quantity < 1:
        raise ValueError("quantity must be at least 1")
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")
    if shipping_cost < 0:
        raise ValueError("shipping_cost cannot be negative")

    # 1. Calculate base subtotal
    base_subtotal = subtotal_per_item * quantity

    # 2. Apply bulk pricing tiers
    bulk_discount_rate = 0.0
    if quantity >= 100:
        bulk_discount_rate = 0.15  # 15% off for 100+ items
    elif quantity >= 50:
        bulk_discount_rate = 0.10  # 10% off for 50+ items
    elif quantity >= 10:
        bulk_discount_rate = 0.05  # 5% off for 10+ items
    
    subtotal_after_bulk = base_subtotal * (1 - bulk_discount_rate)

    # 3. Apply regular discount (e.g., promotional code)
    subtotal_after_regular_discount = subtotal_after_bulk * (1 - discount_percent / 100.0)

    # 4. Apply loyalty discount
    loyalty_discount_rate = 0.0
    if loyalty_tier == "vip":
        loyalty_discount_rate = 0.20  # 20% off for VIP
    elif loyalty_tier == "premium":
        loyalty_discount_rate = 0.10  # 10% off for Premium
    # standard tier gets no loyalty discount

    subtotal_after_loyalty = subtotal_after_regular_discount * (1 - loyalty_discount_rate)
    
    # 5. Add shipping costs
    cost_before_tax = subtotal_after_loyalty + shipping_cost
    
    # 6. Apply tax
    final_total = cost_before_tax * (1 + tax_rate)
    
    return round(final_total, 2)

