from src.modules.AbstractDescription import AbstractDescription
from src.modules.Product import Product


class Category(AbstractDescription):
    """Класс для абстракции 'Категория'"""
    products: list[Product]
    __category_amount = 0
    __products_amount = 0

    def __init__(self, name: str, desc: str, products: list[Product]):
        super().__init__(name, desc)
        self.__products = products

        Category.__category_amount += 1
        Category.__products_amount += len(self.__products)

    def __str__(self) -> str:
        return f"{self._name}, количество продуктов: {self.__len__()} шт."

    def __len__(self) -> int:
        return sum([product.count for product in self.__products])

    def get_products(self) -> list:
        """Возвращает значение поля 'products'"""
        return self.__products

    @classmethod
    def get_products_amount(cls) -> int:
        """Возвращает значение поля 'products_amount'"""
        return cls.__products_amount

    @classmethod
    def get_category_amount(cls) -> int:
        """Возвращает значение поля 'category_amount'"""
        return cls.__category_amount

    @property
    def products(self) -> list[str]:
        return [f"{product.__str__()}" for product in self.__products]

    def __add__(self, other) -> None:
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
