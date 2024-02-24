from src.modules.AbstractDescription import AbstractDescription
from abc import abstractmethod


class AbstractProduct(AbstractDescription):
    """Абстрактный класс для всех 'продуктовых' классов"""
    __instances = []

    def __init__(self, name: str, desc: str, price: float, count: int, color: str = None):
        super().__init__(name, desc)
        self._price = price
        self._count = count
        self._color = color
        AbstractProduct.__instances.append(self)

    @abstractmethod
    def __str__(self):
        pass

    def __len__(self):
        return self._count

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self._price * self._count + other.price * other.count
        raise TypeError('Складывать экземпляры разных классов (включая дочернии) нельзя')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print('Введена некорректная цена')
        if new_price < self._price:
            user_input = input('Цена товара снизится! Вы уверены? (Y/n) ')
            if user_input.lower() in ('n', 'no', 'нет'):
                return
        self._price = new_price

    @price.deleter
    def price(self):
        self._price = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, new_count: float):
        self._count = new_count

    @count.deleter
    def count(self):
        self._count = None

    @classmethod
    def make_product(cls, name: str, desc: str, price: float, count: int):
        for instance in cls.__instances:
            if name.lower() == instance.get_name().lower():
                instance.count += count
                if price > instance.price:
                    instance.price = price
                break
        else:
            return cls(name, desc, price, count)
