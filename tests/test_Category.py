import pytest
from src.modules.Category import Category
from src.modules.Product import Product
from src.modules.ProductException import ProductException


def test_getters():
    food = Category('Food', 'This is Food.', [Product('NOTNOTBox', 'This is NOTNOT the Box', 0, 0)])
    assert food.get_name() == 'Food'
    assert food.get_desc() == 'This is Food.'
    assert food.get_products()[0].get_name() == 'NOTNOTBox'
    assert food.products == ['NOTNOTBox, 0 руб. Остаток: 0 шт.']
    assert len(food) == 0


def test_products_amount():
    assert Category.get_products_amount() == 1


def test_add_products(monkeypatch):
    new_cat = Category('new', 'new', [Product('Apple', 'This is Apple', 0, 0)])
    new_cat + Product('Box', 'This is the Box', 1, 1)
    assert Category.get_products_amount() == 3
    assert new_cat.products == ['Apple, 0 руб. Остаток: 0 шт.', 'Box, 1 руб. Остаток: 1 шт.']
    monkeypatch.setattr('builtins.input', lambda _: "y")
    new_cat + Product('Box', 'This is the Box', 2, 2)
    assert new_cat.products == ['Apple, 0 руб. Остаток: 0 шт.', 'Box, 2 руб. Остаток: 3 шт.']
    with pytest.raises(TypeError):
        assert new_cat + 'TESTING ERROR'
    with pytest.raises(ProductException):
        new_cat + Product('TEST_ProductException', 'TEST', 2, 0)


def test_categories_amount():
    assert Category.get_category_amount() == 2
