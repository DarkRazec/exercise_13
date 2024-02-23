from src.modules.AbstractProduct import AbstractProduct


class Product(AbstractProduct):
    """Класс для абстракции 'Продукт'"""

    def __init__(self, name: str, desc: str, price: float, count: int, color: str = None):
        super().__init__(name, desc, price, count, color)

    def __str__(self):
        return f"Продукт {self._name}, ценой {self._price} руб. Остаток: {self._count} шт."
