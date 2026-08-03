from promotions import Promotion


class Product:
    """
    Represents a product in the store.
    """

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int,
        promotion: Promotion | None = None,
    ):
        """
        Initializes a new Product instance.

        Parameters
        ----------
        name : str
            The name of the product.
        price : float
            The price of the product.
        quantity : int
            The initial quantity of the product in stock.

        Raises
        ------
        ValueError
            If name is empty, or price/quantity is negative.
        """
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("Invalid product parameters")

        self._name: str = name
        self._price: float = price
        self._quantity: int = quantity
        self._promotion: Promotion | None = promotion
        self._active: bool = True

    @property
    def name(self) -> str:
        """Returns the name of the product."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Sets the name of the product."""
        self._name = new_name

    @property
    def price(self) -> float:
        """Returns the price of the product."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Sets the price of the product."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    @property
    def quantity(self) -> int:
        """Returns the quantity of the product."""
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        """Sets the quantity of the product."""
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = new_quantity
        if self._quantity == 0:
            self.active = False

    @property
    def active(self) -> bool:
        """Returns whether the product is active."""
        return self._active

    @active.setter
    def active(self, new_active: bool) -> None:
        """Sets whether the product is active."""
        self._active = new_active

    @property
    def promotion(self) -> Promotion | None:
        """Returns the promotion of the product."""
        return self._promotion

    @promotion.setter
    def promotion(self, promotion: Promotion | None) -> None:
        """Sets the promotion of the product."""
        self._promotion = promotion

    @property
    def _promotion_info(self) -> str:
        """Returns the promotion info of the product."""
        return f", Promotion: {self._promotion.name}" if self._promotion else ""

    def buy(self, quantity: int) -> float:
        """
        Buys the given quantity and returns the total cost.
        Raises ValueError if not enough stock is available.
        """
        if quantity > self._quantity:
            raise ValueError("Not enough products available.")
        self.quantity = self._quantity - quantity
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self._price * quantity

    def __str__(self) -> str:
        """Displays the product information."""
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}{self._promotion_info}"

    def __gt__(self, other_product: "Product") -> bool:
        """Compares the price of this product with another product."""
        return self._price > other_product._price

    def __ge__(self, other_product: "Product") -> bool:
        """Compares the price of this product with another product."""
        return self._price >= other_product._price

    def __lt__(self, other_product: "Product") -> bool:
        """Compares the price of this product with another product."""
        return self._price < other_product._price

    def __le__(self, other_product: "Product") -> bool:
        """Compares the price of this product with another product."""
        return self._price <= other_product._price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float, promotion: Promotion | None = None):
        super().__init__(name, price, 0, promotion)

    def buy(self, quantity: int) -> float:
        """
        Buys the given quantity and returns the total cost.
        Non-stocked immaterial goods dont reduce the stock.
        """
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self._price * quantity

    def __str__(self) -> str:
        """Displays the product information."""
        return f"{self._name}, Price: {self._price}{self._promotion_info}"


class LimitedProduct(Product):
    def __init__(
        self,
        name: str,
        price: float,
        quantity: int,
        maximum: int,
        promotion: Promotion | None = None,
    ):
        super().__init__(name, price, quantity, promotion)
        self._maximum = maximum

    def buy(self, quantity: int) -> float:
        """Buys the given quantity and returns the total cost."""
        if quantity > self._maximum:
            raise ValueError(
                f"Limited products can only be bought in quantities of {self._maximum}."
            )
        return super().buy(quantity)

    def __str__(self) -> str:
        """Displays the product information."""
        return (
            f"{self._name}, Price: {self._price}, "
            f"Quantity: {self._quantity}, Maximum Quantity: {self._maximum}{self._promotion_info}"
        )


def main():
    """Main function to demonstrate product functionality."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.active)

    print(bose)
    print(mac)

    bose.quantity = 1000
    print(bose)


if __name__ == "__main__":
    main()
