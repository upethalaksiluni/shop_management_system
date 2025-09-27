from abc import ABC, abstractmethod
from typing import List, Dict
from customer.customer import Customer
from order.order import Order
from product.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Product:
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
    def get_order_by_id(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def list_all_orders(self) -> List[Order]:
        pass


class CustomerRepository(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: str) -> Customer:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def list_all_customers(self) -> List[Customer]:
        pass


# In-memory implementations
class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.__products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def get_by_id(self, product_id: str) -> Product:
        return self.__products.get(product_id)

    def update(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def list_all_products(self) -> List[Product]:
        return list(self.__products.values())


class InMemoryCustomerRepository(CustomerRepository):
    def __init__(self):
        self.__customers: Dict[str, Customer] = {}

    def add_customer(self, customer: Customer) -> None:
        self.__customers[customer.customer_id] = customer

    def get_by_id(self, customer_id: str) -> Customer:
        return self.__customers.get(customer_id)

    def update(self, customer: Customer) -> None:
        self.__customers[customer.customer_id] = customer

    def list_all_customers(self) -> List[Customer]:
        return list(self.__customers.values())


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.__orders: Dict[str, Order] = {}

    def add(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def get_order_by_id(self, order_id: str) -> Order:
        return self.__orders.get(order_id)

    def list_all_orders(self) -> List[Order]:
        return list(self.__orders.values())
