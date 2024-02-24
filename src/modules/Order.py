from src.modules.AbstractProduct import AbstractProduct


class Order:
    """Класс для абстракции 'Заказ'"""
    product: AbstractProduct
    count: int

    def __init__(self, product: AbstractProduct, count: int):
        self.__product = product
        self.__count = count
        self.__cost = count * product.price

    def get_count(self):
        """Возвращает поле __count"""
        return self.__count

    def get_cost(self):
        """Возвращает поле __cost"""
        return self.__cost
