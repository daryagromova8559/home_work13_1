class Product:
    """Класс для представления продукта"""

    name: str
    specification: str
    price: float
    amount: int

    def __init__(self, name, specification, price, amount):
        self.name = name
        self.specification = specification
        self.__price = price
        self.amount = amount

    @classmethod
    def new_product(cls, name, specification, price, amount):
        return cls(name, specification, price, amount)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Некорректная цена')
            return
        self.__price = value

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.__len__()} шт.'

    def __add__(self, other):
        return self.price * self.amount + other.price * other.amount

    def __len__(self):
        return self.amount
