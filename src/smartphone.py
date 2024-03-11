from src.mixin import MixinLog
from src.product import Product

class Smartphone(Product, MixinLog):
    """Класс для представления смартфона"""

    def __init__(self, name, specification, price, amount, color, performance, model, memory):
        super().__init__(name, specification, price, amount, color)
        self.performance = performance
        self.model = model
        self.memory = memory