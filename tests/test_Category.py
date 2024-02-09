import pytest
from src.modules.Category import Category
from src.modules.Product import Product


@pytest.fixture
def some_category():
    return Category('Containers', 'This is containers. They contain objects inside themselves.', [1, 2])


@pytest.fixture
def some_category_2():
    return Category('Food', 'This is Food.', [Product('NOTBox', 'This is NOT the Box', 0, 0)])


def test_getters(some_category):
    assert some_category.get_name() == 'Containers'
    assert some_category.get_desc() == 'This is containers. They contain objects inside themselves.'
    assert type(some_category.get_products()) == list


def test_products(some_category_2):
    assert some_category_2.products == ['NOTBox, 0 руб. Остаток: 0 шт.']


def test_products_amount():
    assert Category.products_amount == 3


def test_categories_amount():
    assert Category.category_amount == 2

