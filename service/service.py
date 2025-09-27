from dataclasses import dataclass
from typing import List
from customer.customer import Customer
from order.order import Order, OrderItem
from product.product import Product
from repositories.repositories import ProductRepository, OrderRepository, CustomerRepository


class SuperMarketException(Exception):
    pass


@dataclass
class SuperMarketService:
    products: ProductRepository
    customers: CustomerRepository
    orders: OrderRepository  # fixed lowercase

    def add_products(self, product_id: str, name: str, price: float, quantity: int) -> Product:
        if self.products.get_by_id(product_id) is not None:
            raise SuperMarketException("Product ID already exists")
        if quantity < 0:
            raise SuperMarketException("Quantity can't be less than zero")
        if price < 0:
            raise SuperMarketException("Price can't be less than zero")
        product = Product(product_id=product_id, name=name, price=price, quantity=quantity)
        self.products.add_product(product)
        return product

    def add_customers(self, customer_id: str, name: str, email: str, contact: str) -> Customer:
        if self.customers.get_by_id(customer_id) is not None:
            raise SuperMarketException("Customer ID already exists")
        customer = Customer(customer_id=customer_id, customer_name=name, email=email, contact=contact)
        self.customers.add_customer(customer)
        return customer

    def add_orders(self, order_id: str, cust_id: str) -> Order:
        if self.orders.get_order_by_id(order_id) is not None:
            raise SuperMarketException("Order ID already exists")
        cust = self.customers.get_by_id(cust_id)
        if cust is None:
            raise SuperMarketException("Customer does not exist")
        order = Order(order_id=order_id, customer_id=cust_id)
        self.orders.add(order)
        return order

    def add_order_item(self, order_id: str, prod_id: str, quantity: int):
        order = self.orders.get_order_by_id(order_id)
        product = self.products.get_by_id(prod_id)
        if order is None:
            raise SuperMarketException("Order doesn't exist")
        if product is None:
            raise SuperMarketException("Product doesn't exist")
        if product.quantity < quantity:
            raise SuperMarketException("Stock not available")
        order_item = OrderItem(product_id=prod_id, product_name=product.name, quantity=quantity,
                               unit_price=product.price)
        order.add_order_item(order_item)
        product.reduce_quantity(quantity)
        self.orders.add(order)  # update with overwrite
        self.products.update(product)

    def get_all_available_products(self) -> List[Product]:
        return [product for product in self.products.list_all_products() if product.is_available()]

    def get_all_products(self) -> List[Product]:
        return self.products.list_all_products()

    def get_all_customers(self) -> List[Customer]:
        return self.customers.list_all_customers()
