# Best Buy

A small command-line store simulation, written to practice OOP concepts in Python (inheritance, polymorphism, abstract classes, magic methods, properties).

## Structure

- `products.py`: `Product` base class (name, price, quantity, active state, promotion) plus two subclasses:
  - `NonStockedProduct`: quantity always stays 0 (e.g. digital licenses)
  - `LimitedProduct`: capped at a maximum quantity per order (e.g. shipping fees)
- `promotions.py`: abstract `Promotion` base class and three implementations:
  - `PercentageDiscountPromotion`, `SecondHalfPricePromotion`, `BuyTwoOneFreePromotion`
- `store.py`: the `Store` class, holds a list of products and handles orders; supports `in` (product lookup) and `+` (combining two stores)
- `main.py`: command-line menu to list products, show stock, and place orders
- `test_product.py`: pytest unit tests for the product classes

## Usage

```bash
uv run python main.py
```

You'll get a menu:

```text
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

Choose "Make an order" to buy one or more products. Enter an empty line to finish and see the total price.

## Development

```bash
uv run pytest test_product.py   # run unit tests
uv run ruff check .             # lint / PEP-8 checks
uv run mypy .                   # type checks
```
