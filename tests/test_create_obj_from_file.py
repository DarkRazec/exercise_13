import pytest
from src.create_obj_from_file import create_obj_from_file


@pytest.fixture
def category_list():
    return create_obj_from_file('../exercise_13_1/data/products.json')  # Путь указан так, чтобы тесты запускались через команду pytest


def test_create_obj(category_list):
    assert category_list[0].get_name() == "Смартфоны"
    assert category_list[1].get_products()[0].get_name() == "55\" QLED 4K"
