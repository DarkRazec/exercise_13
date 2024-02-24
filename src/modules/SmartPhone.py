from src.modules.Product import Product
from src.modules.AbstractProduct import AbstractProduct
from src.modules.MixinRepr import MixinRepr


class SmartPhone(Product, AbstractProduct, MixinRepr):
    """Класс для абстракции 'Смартфон'"""
    performance: float
    model: str
    memory: float

    def __init__(self, name, desc, price, count, color: str, performance: float, model: str, memory: float):
        super().__init__(name, desc, price, count, color)
        self.__performance = performance
        self.__model = model
        self.__memory = memory
