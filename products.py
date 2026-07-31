class Product:
    def __init__(
        self,
        name: str,
        price: float,
        quantity: int,
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

        self.name: str = name
        self.price: float = price
        self.quantity: float = quantity
        self.active: bool = True

    def get_quantity(self) -> int:
        """Returns the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity) -> None:
        """Sets the quantity of the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
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

    def show(self) -> None:
        """Displays the product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        Buys the given quantity and returns the total cost.
        Raises ValueError if not enough stock is available.
        """
        if quantity > self.quantity:
            raise ValueError("Not enough products available.")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity

def main():
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