from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    name: str
    price: float
    quantity: int

    def is_available(self) -> bool:
        return self.quantity is None

    def add_quantity(self, amount: int):
        self.quantity += amount

    def reduce_quantity(self, amount: int):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            raise ValueError("Not enough stock available.")




