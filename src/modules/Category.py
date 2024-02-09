class Category:
    """Класс для абстракции 'Категория'"""
    __category_amount = 0
    __products_amount = 0

    def __init__(self, name: str, desc: str, products: list):
        self.__name = name
        self.__desc = desc
        self.__products = products

        Category.__category_amount += 1
        Category.__products_amount += len(self.__products)

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def get_products(self):
        return self.__products

    @property
    def category_amount(self):
        return self.__category_amount

    @property
    def products(self):
        return [f"{product.get_name()}, {product.price} руб. Остаток: {product.get_count()} шт." for product in self.__products]

    def add_products(self, new_product: object):
        self.__products.append(new_product)
        Category.products_amount += 1
