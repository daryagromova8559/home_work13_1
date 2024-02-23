import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def category_women_clothes():
    return Category('Женская одежда', 'Женская одежда на каждый день',
                    ["платье", "джинсы", "юбка"])


def test_init_(category_women_clothes):
    assert category_women_clothes.name == 'Женская одежда'
    assert category_women_clothes.specification == 'Женская одежда на каждый день'
    assert category_women_clothes.products == ["платье", "джинсы", "юбка"]
    assert category_women_clothes.numbers_of_category == 1
    assert category_women_clothes.numbers_of_products == 3


@pytest.fixture
def product_dress():
    return Product('Платье', 'вечернее', 6500, 4)


def test_init_product(product_dress):
    assert product_dress.name == 'Платье'
    assert product_dress.specification == 'вечернее'
    assert product_dress.price == 6500
    assert product_dress.amount == 4
