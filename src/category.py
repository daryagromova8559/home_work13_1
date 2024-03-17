from src.product import Product


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
        """Добавление нового продукта"""
        if not isinstance(new_product, Product):
            raise TypeError('Добавлять можно только объекты Product или его наследников')
        elif new_product.amount <= 0:
            raise ValueError('Нельзя добавить товар с нулевым количеством!')
        else:
            self.__products.append(new_product)
            Category.numbers_of_products += 1
            return self.__products

    @property
    def products_display(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.amount} шт.\n'
        return result

    def __str__(self):
        return f'Название категории {self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        sum_product = 0
        for i in self.__products:
            sum_product += i.amount
        return sum_product

    def average_price(self):
        """Подсчет средней цены продуктов"""
        total_price = []
        average_price = []
        try:
            for i in self.__products:
                total_price.append(i.price * i.amount)
                average_price = round(sum(total_price) / len(self), 2)
        except ZeroDivisionError:
            average_price = 0
        return average_price
