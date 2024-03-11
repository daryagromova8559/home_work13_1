from src.mixin import MixinLog
from src.product import Product

class LawnGrass(Product, MixinLog):
    """Класс для представления травы газонной"""

    def __init__(self, name, specification, price, amount, color, country, germination):
        super().__init__(name, specification, price, amount, color)
        self.country = country
        self.germination = germination