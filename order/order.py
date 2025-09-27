from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from order.orderItem import OrderItem


@dataclass
class Order:
    order_id: str
    customer_id: str
    customer_name: str
    created_at: datetime
    order_items: List[OrderItem]

    def add_order_item(self, order_item: OrderItem):
        self.order_items.append(order_item)

    def total_amount(self) -> float:
        return sum(item.total_price() for item in self.order_items)

