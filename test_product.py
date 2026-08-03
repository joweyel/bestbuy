import pytest
from products import Product, NonStockedProduct, LimitedProduct


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


# ======================== #
# NonStockedProduct Tests  #
# ======================== #


def test_nonstocked_product_quantity_is_zero():
    """Test that NonStockedProduct has quantity 0 by default."""
    product = NonStockedProduct("Windows License", price=125)
    assert product.quantity == 0


def test_nonstocked_product_quantity_stays_zero():
    """Test that NonStockedProduct quantity stays 0 after purchase."""
    purchase_quantity: int = 2
    product = NonStockedProduct("Windows License", price=125)
    assert product.buy(purchase_quantity) == product.price * purchase_quantity
    assert product.quantity == 0


def test_nonstocked_product_remains_active():
    """Test that NonStockedProduct remains active after purchase."""
    product = NonStockedProduct("Windows License", price=125)
    assert product.is_active() == True
    product.buy(1)
    assert product.is_active() == True


def test_nonstocked_product_returns_correct_total_price():
    """4. buy(quantity) gibt den korrekten Gesamtpreis zurück (price * quantity)."""
    purchase_quantity: int = 2
    product = NonStockedProduct("Windows License", price=125)
    assert product.buy(purchase_quantity) == purchase_quantity * product.price


# ============================ #
# LimitedProduct Tests         #
# ============================ #


def test_limited_product_creation_sets_quantity_and_maximum():
    """Test that LimitedProduct sets quantity and maximum correctly."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.quantity == 250
    assert product._maximum == 1


def test_limited_product_buy_within_maximum_reduces_quantity_and_returns_correct_price():
    """Test that LimitedProduct buy within maximum reduces quantity and returns correct price."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.buy(1) == 10
    assert product.quantity == 249


def test_limited_product_buy_over_maximum_raises_exception():
    """Test that LimitedProduct buy over maximum raises exception."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError):
        product.buy(2)


def test_limited_product_buy_exceeding_stock_raises_exception():
    """Test that LimitedProduct buy exceeding stock (but within maximum) raises exception."""
    product = LimitedProduct("Shipping", price=10, quantity=1, maximum=5)
    with pytest.raises(ValueError):
        product.buy(2)
