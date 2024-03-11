from src.abs_class import AbsClass


class Product(AbsClass):
    """Класс для представления продукта"""

    name: str
    specification: str
    price: float
    amount: int
    color: str

    def __init__(self, name, specification, price, amount, color):
        self.name = name
        self.specification = specification
        self.__price = price
        self.amount = amount
        self.color = color

    @classmethod
    def new_product(cls, name, specification, price, amount, color):
        return cls(name, specification, price, amount, color)

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
        return f'{self.name}, {self.price} руб. Остаток: {len(self)} шт.'

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.price * self.amount + other.price * other.amount
        else:
            raise TypeError

    def __len__(self):
        return self.amount






