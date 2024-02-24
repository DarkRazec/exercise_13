import pytest
from src.modules.ThroughCategorysProducts import ThroughCategorysProducts
from src.modules.Category import Category
from src.modules.Product import Product


def test_through_categorys_product():
    new_cat = Category('new', 'new', [Product('Apple', 'This is Apple', 0, 0),
                                      Product('Box', 'This is the Box', 1.1, 5)])
    assert [i.get_name() for i in ThroughCategorysProducts(new_cat)] == ['Apple', 'Box']
