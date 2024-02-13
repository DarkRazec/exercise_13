from src.modules.ABCDescription import ABCDescription


class Category(ABCDescription):
    """Класс для абстракции 'Категория'"""
    __category_amount = 0
    __products_amount = 0

    def __init__(self, name: str, desc: str, products: list):
        super().__init__(name, desc)
        self.__products = products

        Category.__category_amount += 1
        Category.__products_amount += len(self.__products)

    def __str__(self):
        return f"{self._name}, количество продуктов: {sum([product.count for product in self.__products])} шт."

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
        return [f"{product.get_name()}, {product.price} руб. Остаток: {product.count} шт." for product in
                self.__products]

    def add_products(self, new_product):
        for product in self.__products:
            if new_product.get_name().lower() == product.get_name().lower():
                product.count += new_product.count
                user_input = input('Сменить цену товара на новую? (Y/n) ')
                if user_input.lower() in ('y', 'yes', 'да'):
                    product.price = new_product.price
                break
        else:
            self.__products.append(new_product)
            Category.__products_amount += 1
