class Category:
    """Класс для абстракции 'Категория'"""
    __category_amount = []

    def __init__(self, name: str, desc: str, products: list):
        self.__name = name
        self.__desc = desc
        self.products = products
        self.__products_amount = len(self.products)
        self.__category_amount.append('')

    def get_name(self):
        return self.__name

    def get_desc(self):
        return self.__desc

    def get_products(self):
        return self.products

    def get_products_amount(self):
        return self.__products_amount

    def get_categories_amount(self):
        return len(self.__category_amount)

