from src.modules.AbstractProduct import AbstractProduct


class SmartPhone(AbstractProduct):
    """Класс для абстракции 'Смартфон'"""
    performance: float
    model: str
    memory: float

    def __init__(self, name: str, desc: str, price: float, count: int, color: str, performance: float, model: str, memory: float):
        super().__init__(name, desc, price, count, color)
        self.__performance = performance
        self.__model = model
        self.__memory = memory

    def __str__(self):
        return f"Смартфон {self._name}, ценой {self._price} руб. Остаток: {self._count} шт."
