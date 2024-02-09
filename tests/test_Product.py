import pytest
from src.modules.Product import Product


@pytest.fixture
def some_product():
    return Product('Box', 'This is the Box', 1.1, 5)


def test_getters(some_product):  # actually, this is __init__ parameters, so I made them in one test
    assert some_product.get_name() == 'Box'
    assert some_product.get_desc() == 'This is the Box'
    assert some_product.get_count() == 5
    assert some_product.price == 1.1


def test_set_price(some_product, monkeypatch):
    some_product.price = 1.2
    assert some_product.price == 1.2
    monkeypatch.setattr('builtins.input', lambda _: "no")
    some_product.price = 1.0
    assert some_product.price == 1.2
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    some_product.price = 0
    assert some_product.price == 0


def test_delete_price(some_product):
    del some_product.price
    assert some_product.price is None


def test_make_product(some_product):
    new_prod = some_product.make_product('NOTBox', 'This is NOT the Box', 0, 0)
    assert new_prod.get_name() == 'NOTBox'
