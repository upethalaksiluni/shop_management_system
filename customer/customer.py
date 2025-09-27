from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: str
    customer_name: str
    email: str
    contact: str
