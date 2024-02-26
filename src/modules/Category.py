from src.modules.AbstractDescription import AbstractDescription
from src.modules.AbstractProduct import AbstractProduct
from src.modules.MixinRepr import MixinRepr


class Category(AbstractDescription, MixinRepr):
    """Класс для абстракции 'Категория'"""
    __category_amount = 0
    __products_amount = 0
    products: list[AbstractProduct]

    def __init__(self, name: str, desc: str, products: list[AbstractProduct]):
        super().__init__(name, desc)
        self.__products = products

        Category.__category_amount += 1
        Category.__products_amount += len(self.__products)

    def __str__(self):
        return f"{self._name}, количество продуктов: {self.__len__()} шт."

    def __len__(self):
        """Возвращает общее число товаров в списке"""
        return sum([product.count for product in self.__products])

    def get_products(self):
        """Возвращает значение поля __products"""
        return self.__products

    @classmethod
    def get_products_amount(cls):
        """Возвращает значение поля __products_amount"""
        return cls.__products_amount

    @classmethod
    def get_category_amount(cls):
        """Возвращает значение поля __category_amount"""
        return cls.__category_amount

    @property
    def products(self):
        return [f"{product.__str__()}" for product in self.__products]

    def __add__(self, other: AbstractProduct):
        """Добавляет объект продуктового класса в __products. Если такой уже есть в списке, то добавляет введенное
        количество товара к уже существующему и спрашивает у пользователя, изменить ли цену на товар."""
        if isinstance(other, AbstractProduct):
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
            raise TypeError('Переданный аргумент не является объектом "продуктового" класса или его наследником')

    def avg_price(self):
        """Возвращает среднее арифметическое цены на все продукты категории"""
        try:
            return sum([product.price for product in self.__products])/len(self)
        except ZeroDivisionError:
            return 0
