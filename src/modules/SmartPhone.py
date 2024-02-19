from src.modules.Product import Product


class SmartPhone(Product):
    """Класс для абстракции 'Смартфон'"""
    def __init__(self, name, desc, price, count, color: str, performance: float, model: str, memory: float):
        super().__init__(name, desc, price, count, color)
        self.__performance = performance
        self.__model = model
        self.__memory = memory
