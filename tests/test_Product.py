import pytest
from src.modules.Product import Product


@pytest.fixture
def some_product():
    return Product('Box', 'This is the Box', 1.1, 5)


def test_getters(some_product):  # actually, this is __init__ parameters, but they are private
    assert some_product.get_name() == 'Box'
    assert some_product.get_desc() == 'This is the Box'
    assert some_product.get_count() == 5
    assert some_product.get_price() == 1.1

