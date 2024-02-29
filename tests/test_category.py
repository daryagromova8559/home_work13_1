import pytest

from src.category import Category


@pytest.fixture
def category():
    return Category('Смартфоны', 'Смартфоны', ["Iphone 13pro", "Samsung a54", "Honor 8a"])


def test_init_(category):
    assert category.name == 'Смартфоны'
    assert category.specification == 'Смартфоны'
    assert category.products == ["Iphone 13pro", "Samsung a54", "Honor 8a"]
    assert category.numbers_of_category == 1
    assert category.numbers_of_products == 3
