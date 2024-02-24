

class Category:
    """Класс для представления категории продукта"""

    name: str
    specification: str
    products: list
    numbers_of_category = 0
    numbers_of_products = 0

    def __init__(self, name, specification, products):
        self.name = name
        self.specification = specification
        self.__products = products

        Category.numbers_of_category += 1
        Category.numbers_of_products = len(products)

    @property
    def products(self):
        return self.__products

    def add_products(self, new_product):
        self.__products.append(new_product)
        Category.numbers_of_products += 1
        return self.__products

    @property
    def products_display(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result
