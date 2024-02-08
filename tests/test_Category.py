import pytest
from src.modules.Category import Category


@pytest.fixture
def some_category():
    return Category('Containers', 'This is containers. They contain objects inside themselves.', [1, 2])


@pytest.fixture
def some_category_2():
    return Category('Food', 'This is Food.', [3])


def test_getters(some_category):
    assert some_category.get_name() == 'Containers'
    assert some_category.get_desc() == 'This is containers. They contain objects inside themselves.'
    assert type(some_category.get_products()) == list
    assert some_category.get_products_amount() == 2
    assert some_category.get_categories_amount() == 1


def test_categories_amount(some_category_2):
    assert some_category_2.get_categories_amount() == 2
