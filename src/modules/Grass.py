from src.modules.Product import Product


class Grass(Product):
    """Класс для абстракции 'Газонная трава'"""
    def __init__(self, name, desc, price, count, color: str, made_in: str, germination: int):
        super().__init__(name, desc, price, count, color)
        self.__made_in = made_in
        self.__germination = germination
