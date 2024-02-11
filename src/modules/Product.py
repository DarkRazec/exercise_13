class Product:
    """Класс для абстракции 'Продукт'"""
    __instances = []

    def __init__(self, name: str, desc: str, price: float, count: int):
        self.__name = name
        self.__desc = desc
        self.__price = price
        self.__count = count
        Product.__instances.append(self)

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
            if name.lower() == instance.__name.lower():
                instance.__count += count
                if price > instance.price:
                    instance.__price = price
                break
        else:
            return cls(name, desc, price, count)
