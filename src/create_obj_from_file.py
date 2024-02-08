from json import load
from src.modules.Category import Category
from src.modules.Product import Product


def create_obj_from_file(path="../data/products.json"):
    """
    Создает объекты класса 'Category', в которых находятся объектами класса 'Product'
    :param path: путь к JSON файлу
    :return: Объект класса 'Category'
    """
    with open(path, encoding='utf-8') as f:
        category_data = load(f)

    categories = []
    for category in category_data:
        name = category['name']
        desc = category['description']
        products = [Product(product['name'], product['description'], product['price'], product['quantity']) for product in category['products']]

        categories.append(Category(name, desc, products))
    return categories
