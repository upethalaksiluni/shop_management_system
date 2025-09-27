from abc import ABC, abstractmethod
from typing import List

from customer.customer import Customer
from order.order import Order
from product.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> None:
        pass

    @abstractmethod
    def list_all_products(self) -> List[Product]:
        pass


class OrderRepository(ABC):

    @abstractmethod
    def add(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id) -> Order:
        pass

    @abstractmethod
    def list_all_orders(self) -> List[Order]:
        pass


class CustomerRepository(ABC):

    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, customer_id) -> Customer:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def list_all_customers(self) -> List[Customer]:
        pass
