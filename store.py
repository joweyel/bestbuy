from typing import List, Tuple
from products import Product


class Store:
    """Represents a store with a collection of products."""

    def __init__(self, products: List[Product]):
        self._products: List[Product] = products

    def add_product(self, product: Product) -> None:
        """Adds a product to the store."""
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        """Removes a product from the store."""
        self._products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum(product.quantity for product in self._products)

    def get_all_products(self) -> List[Product]:
        """Returns all products in the store that are active."""
        return [product for product in self._products if product.active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Processes an order and returns the total price."""
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total

    def __contains__(self, product: Product) -> bool:
        """Checks if a product is in the store."""
        return product in self._products

    def __add__(self, other_store: "Store") -> "Store":
        """Combines two stores."""
        return Store(self._products + other_store._products)


def main():
    """Main function to demonstrate store functionality."""
    product_list: List[Product] = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
    print(products[0] in best_buy)


if __name__ == "__main__":
    main()
