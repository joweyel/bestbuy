from products import Product
from store import Store


def start(store: Store) -> None:
    """Starts the store menu and handles user input.

    Parameters
    ----------
    store : Store
        The store object to interact with.
    """

    def parse_int(raw_input: str) -> int | None:
        """Parses string to integer if valid digit."""
        if raw_input.isdigit():
            return int(raw_input)
        return None

    while True:
        # Lists the available options.
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        if (choice := parse_int(input("Please choose a number: "))) is None:
            continue

        if choice == 1:
            print("------")
            for product in store.get_all_products():
                product.show()
            print("------")

        elif choice == 2:
            # Show total amount
            total_amount_products: int = sum(
                product.get_quantity() for product in store.get_all_products()
            )
            print(f"Total of {total_amount_products} items in store")

        elif choice == 3:
            # Make an order
            print("------")
            products_list = store.get_all_products()
            for idx, product in enumerate(products_list):
                print(f"{idx+1}.", end=" ")
                product.show()
            print("------")
            print("When you want to finish order, enter empty text.")

            # List of products
            shopping_list: list[tuple[Product, int]] = []
            while True:
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break

                if (
                    (index := parse_int(product_number)) is None
                    or index < 1
                    or index > len(products_list)
                ):
                    continue
                index -= 1  # Convert 1-based index to 0-based list index

                if (
                    amount := parse_int(input("What amount do you want? "))
                ) is None or amount <= 0:
                    continue
                shopping_list.append((products_list[index], amount))
                print("Product added to list!")

            # Purchasing everything in the shopping list
            if shopping_list:
                try:
                    total_price: float = store.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${total_price}")
                except ValueError as e:
                    print(f"Error making order: {e}")

        elif choice == 4:
            # Quit
            break

        else:
            continue


if __name__ == "__main__":

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)
