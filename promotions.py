from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from products import Product


class Promotion(ABC):
    def __init__(self, name: str):
        self.__name = name

    @abstractmethod
    def apply_promotion(self, product: "Product", quantity: int) -> float:
        pass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name


class PercentageDiscountPromotion(Promotion):
    def __init__(self, name: str, percentage: float):
        super().__init__(name)
        self.__percentage: float = percentage

    @property
    def percentage(self) -> float:
        return self.__percentage

    @percentage.setter
    def percentage(self, new_percentage: float) -> None:
        self.__percentage = new_percentage

    @override
    def apply_promotion(self, product: "Product", quantity: int) -> float:
        """Apply percentage discount promotion."""
        discount_factor: float = 1 - self.percentage / 100.0
        return product.price * quantity * discount_factor


class SecondHalfPricePromotion(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    @override
    def apply_promotion(self, product: "Product", quantity: int) -> float:
        """Apply second half price promotion."""
        pairs: int = quantity // 2
        remainder: int = quantity % 2
        full_price_items: int = pairs + remainder
        discounted_items: int = pairs
        return full_price_items * product.price + discounted_items * product.price / 2


class BuyTwoOneFreePromotion(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    @override
    def apply_promotion(self, product: "Product", quantity: int) -> float:
        """Apply buy 2 get 1 free promotion.For every 3 items, pay for 2."""
        quantity_free_product: int = quantity // 3
        reduced_quantity: int = quantity - quantity_free_product
        return product.price * reduced_quantity
