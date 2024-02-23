from src.product import Product


class Category:
    """Класс для представления категории продукта"""

    name: str
    specification: str
    products: list
    numbers_of_category = 0
    numbers_of_goods = 0

    def __init__(self, name, specification, products):
        self.name = name
        self.specification = specification
        self.__products = products

        Category.numbers_of_category += 1
        Category.numbers_of_products = len(products)

    @property
    def products(self):
        return self.__products

    def add_products(self, name, specification, price, amount):
        new_product = Product(name, specification, price, amount)
        self.__products.append(new_product)
        return self.__products


    @property
    def products_display(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result

