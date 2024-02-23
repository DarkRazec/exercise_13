from src.modules.AbstractProduct import AbstractProduct


class Grass(AbstractProduct):
    """Класс для абстракции 'Газонная трава'"""
    made_in: str
    germination: int

    def __init__(self, name: str, desc: str, price: float, count: int, color: str, made_in: str, germination: int):
        super().__init__(name, desc, price, count, color)
        self.__made_in = made_in
        self.__germination = germination

    def __str__(self):
        return f"Газонная трава {self._name}, ценой {self._price} руб. Остаток: {self._count} шт."
