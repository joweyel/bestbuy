# Best Buy

A small command-line store simulation, written to practice basic OOP concepts in Python (classes, composition, encapsulation).

## Structure

- `products.py`: the `Product` class (name, price, quantity, active state)
- `store.py`: the `Store` class, holds a list of products and handles orders
- `main.py`: command-line menu to list products, show stock, and place orders

## Usage

```bash
python main.py
```

You'll get a menu:

```text
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

Choose "Make an order" to buy one or more products. Enter an empty line to finish and see the total price.
