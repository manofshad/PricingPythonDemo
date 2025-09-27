from services.pricing import calculate_price

if __name__ == "__main__":
    total = calculate_price(subtotal=100.0, tax_rate=0.08875, discount_percent=10)
    print(f"Total: {total:.2f}")
