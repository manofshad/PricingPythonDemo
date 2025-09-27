from app.services.pricing import calculate_price

def test_basic():
    assert calculate_price(100, 0.1, 0) == 110.00

def test_with_discount():
    assert calculate_price(100, 0.1, 10) == 99.00
