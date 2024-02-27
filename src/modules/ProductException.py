class ProductException(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else 'Неизвестная ошибка'

    def __str__(self):
        return 'Ошибка при работе с объектом продуктового класса: ' + self.message if self.message \
            else f'{self.__class__.__name__} has been raised'


class ProductNullCountException(ProductException):
    def __init__(self, *args):
        self.message = args[0] if args else "Невозможно добавить продукт с нулевым количеством товара"
