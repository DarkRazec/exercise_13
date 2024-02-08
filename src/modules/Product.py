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

    def get_price(self):
        return self.__price

    def get_count(self):
        return self.__count
