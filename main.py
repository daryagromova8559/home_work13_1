class Category:
    """Класс для представления категории продукта"""

    name: str
    specification: str
    product: list
    numbers_of_category = 0
    numbers_of_goods = 0

    def __init__(self, name, specification, goods):
        self.name = name
        self.specification = specification
        self.goods = goods

        Category.numbers_of_category += 1
        Category.numbers_of_goods += 1


class Product:
    """Класс для представления продукта"""

    name: str
    specification: str
    price: float
    amount: int

    def __init__(self, name, specification, price, amount):
        self.name = name
        self.specification = specification
        self.price = price
        self.amount = amount
