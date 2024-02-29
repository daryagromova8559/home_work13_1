import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product.new_product('Samsung A54', '8+256GB', 33540, 20, 'lavender')


def test_init_product(product):
    assert product.name == 'Samsung A54'
    assert product.specification == '8+256GB'
    assert product.price == 33540
    assert product.amount == 20
    assert product.color == 'lavender'
    assert str(product) == "Samsung A54, 33540 руб. Остаток: 20 шт."

