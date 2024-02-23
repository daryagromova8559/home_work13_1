from src.product import Product


class Category:
    """Класс для представления категории продукта"""

    name: str
    specification: str
    goods: list
    numbers_of_category = 0
    numbers_of_goods = 0

    def __init__(self, name, specification, goods):
        self.name = name
        self.specification = specification
        self.__goods = goods

        Category.numbers_of_category += 1
        Category.numbers_of_goods = len(goods)

    @property
    def goods(self):
        return self.__goods

    def add_goods(self, name, specification, price, amount):
        new_product = Product(name, specification, price, amount)
        self.__goods.append(new_product)
        return self.__goods
