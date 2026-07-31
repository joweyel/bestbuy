from typing import List, Tuple
from products import Product


class Store:

    def __init__(self, products: List[Product]):
        self.products: List[Product] = products

    def add_product(self, product: Product) -> None:
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns all products in the store that are active."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Processes an order and returns the total price."""
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total


def main():
    # bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    # mac = Product("MacBook Air M2", price=1450, quantity=100)

    # best_buy = Store([bose, mac])
    # price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    # print(f"Order cost: {price} dollars.")

    product_list: List[Product] = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()
