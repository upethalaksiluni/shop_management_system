from dataclasses import dataclass


@dataclass
class OrderItem:
    product_id: str
    product_name: str
    quantity: int
    unit_price: float

    def total_price(self) -> float:
        return self.quantity * self.unit_price
