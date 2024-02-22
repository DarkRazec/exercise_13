from src.modules.Product import Product


class Grass(Product):
    """Класс для абстракции 'Газонная трава'"""
    made_in: str
    germination: int

    def __init__(self, name: str, desc: str, price: float, count: int, color: str, made_in: str, germination: int):
        super().__init__(name, desc, price, count, color)
        self.__made_in = made_in
        self.__germination = germination
