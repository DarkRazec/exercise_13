class Product:
    """Класс для абстракции 'Продукт'"""
    def __init__(self, name: str, desc: str, price: float, count: int):
        self.__name = name
        self.__desc = desc
        self.__price = price
        self.__count = count

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

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

    def get_count(self):
        return self.__count

    @staticmethod
    def make_product(name: str, desc: str, price: float, count: int):
        return Product(name, desc, price, count)
