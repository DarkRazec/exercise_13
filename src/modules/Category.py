from src.modules.AbstractDescription import AbstractDescription
from src.modules.Product import Product


class Category(AbstractDescription):
    """Класс для абстракции 'Категория'"""
    __category_amount = 0
    __products_amount = 0

    def __init__(self, name: str, desc: str, products: list[Product]):
        super().__init__(name, desc)
        self.__products = products

        Category.__category_amount += 1
        Category.__products_amount += len(self.__products)

    def __str__(self):
        return f"{self._name}, количество продуктов: {self.__len__()} шт."

    def __len__(self):
        return sum([product.count for product in self.__products])

    def get_products(self):
        return self.__products

    @classmethod
    def get_products_amount(cls):
        return cls.__products_amount

    @classmethod
    def get_category_amount(cls):
        return cls.__category_amount

    @property
    def products(self):
        return [f"{product.__str__()}" for product in self.__products]

    def __add__(self, other):
        if isinstance(other, Product) or issubclass(type(other), Product):
            for product in self.__products:
                if other.get_name().lower() == product.get_name().lower():
                    product.count += other.count
                    user_input = input('Сменить цену товара на новую? (Y/n) ')
                    if user_input.lower() in ('y', 'yes', 'да'):
                        product.price = other.price
                    break
            else:
                self.__products.append(other)
                Category.__products_amount += 1
        else:
            raise TypeError('Переданный параметр не является объектом класса "Product" или его дочернего класса')
