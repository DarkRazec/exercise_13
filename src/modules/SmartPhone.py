from src.modules.Product import Product


class SmartPhone(Product):
    """Класс для абстракции 'Смартфон'"""
    performance: float
    model: str
    memory: float

    def __init__(self, name: str, desc: str, price: float, count: int, color: str, performance: float, model: str, memory: float):
        super().__init__(name, desc, price, count, color)
        self.__performance = performance
        self.__model = model
        self.__memory = memory
