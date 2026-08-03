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
        self.active: bool = True

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity

    def get_quantity(self) -> int:
        """Returns the quantity of the product."""
        return self._quantity

    def set_quantity(self, quantity: int) -> None:
        """Sets the quantity of the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Activates the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the product."""
        self.active = False

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
        self.set_quantity(self._quantity - quantity)
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self._price * quantity

    def show(self) -> None:
        """Displays the product information."""
        print(
            f"{self._name}, Price: {self._price}, Quantity: {self._quantity}{self._promotion_info}"
        )


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

    def show(self) -> None:
        """Displays the product information."""
        print(f"{self._name}, Price: {self._price}{self._promotion_info}")


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

    def show(self) -> None:
        """Displays the product information."""
        print(
            f"{self._name}, Price: {self._price}, "
            f"Quantity: {self._quantity}, Maximum Quantity: {self._maximum}{self._promotion_info}"
        )


def main():
    """Main function to demonstrate product functionality."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
