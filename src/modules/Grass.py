from src.modules.AbstractProduct import AbstractProduct
from src.modules.Product import Product
from src.modules.MixinRepr import MixinRepr


class Grass(Product,  AbstractProduct, MixinRepr):
    """Класс для абстракции 'Газонная трава'"""
    made_in: str
    germination: int

    def __init__(self, name, desc, price, count, color: str, made_in: str, germination: int):
        super().__init__(name, desc, price, count, color)
        self.__made_in = made_in
        self.__germination = germination
