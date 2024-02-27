from src.modules.AbstractProduct import AbstractProduct
from src.modules.ProductException import ProductNullCountException
from src.modules.Product import Product


class Order:
    """Класс для абстракции 'Заказ'"""
    product: AbstractProduct
    count: int

    def __init__(self, product: AbstractProduct, count: int):
        if product.count > 0:
            self.__product = product
        else:
            raise ProductNullCountException
        if count > 0:
            self.__count = count
        else:
            raise ValueError('Количество товаров в заказе должно быть больше 0')
        self.__cost = count * product.price

    def get_count(self):
        """Возвращает поле __count"""
        return self.__count

    def get_cost(self):
        """Возвращает поле __cost"""
        return self.__cost
