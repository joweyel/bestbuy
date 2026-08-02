import pytest
from products import Product

def test_create_product():
    """Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() == True
    
    
def test_create_product_with_invalid_details():
    """Test that creating a product with invalid details (empty name, negative price) 
    invokes an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-1, quantity=100)

def test_product_becomes_inactive_when_quantity_reaches_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    product.set_quantity(0)
    assert product.is_active() == False
    
def test_product_purchase_modifies_quantity_and_returns_right_output():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.buy(10) == 14500
    assert product.quantity == 90
    
def test_buy_larger_quantity_than_exists():
    """Test that buying a larger quantity than exists invokes exception."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(101)
    
    