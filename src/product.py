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
