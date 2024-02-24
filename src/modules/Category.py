class Category:
    """Класс для абстракции 'Категория'"""
    category_amount = 0
    products_amount = 0

    def __init__(self, name: str, desc: str, products: list):
        self.__name = name
        self.__desc = desc
        self.__products = products

        Category.category_amount += 1
        Category.products_amount += len(self.__products)

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def get_products(self):
        return self.__products
