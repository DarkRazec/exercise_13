from src.modules.AbstractDescription import AbstractDescription


class Product(AbstractDescription):
    """Класс для абстракции 'Продукт'"""
    __instances = []

    def __init__(self, name: str, desc: str, price: float, count: int, color: str = None):
        super().__init__(name, desc)
        self.__price = price
        self.__count = count
        self.__color = color
        Product.__instances.append(self)

    def __str__(self):
        return f"{self.get_name()}, {self.price} руб. Остаток: {self.count} шт."

    def __len__(self):
        return self.__count

    def __add__(self, other):
        if isinstance(other, Product) or issubclass(type(other), Product):
            if isinstance(other, type(self)):
                return self.__price * self.__count + other.price * other.count
            raise TypeError('Складывать экземпляры разных классов (включая дочернии) нельзя')
        raise TypeError('Переданный параметр не является объектом класса "Product" или его дочернего класса')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print('Введена некорректная цена')
        if new_price < self.__price:
            user_input = input('Цена товара снизится! Вы уверены? (Y/n) ')
            if user_input.lower() in ('n', 'no', 'нет'):
                return
        self.__price = new_price

    @price.deleter
    def price(self):
        self.__price = None

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, new_count: float):
        self.__count = new_count

    @count.deleter
    def count(self):
        self.__count = None

    @classmethod
    def make_product(cls, name: str, desc: str, price: float, count: int):
        for instance in cls.__instances:
            if name.lower() == instance.get_name().lower():
                instance.__count += count
                if price > instance.price:
                    instance.__price = price
                break
        else:
            return cls(name, desc, price, count)
