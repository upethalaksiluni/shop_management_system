from repositories.repositories import (
    InMemoryProductRepository,
    InMemoryCustomerRepository,
    InMemoryOrderRepository
)
from service.service import SuperMarketService


def print_menu():
    print("\n=== Super Market System ===")
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Add Order")
    print("4. Add Order Item")
    print("5. View All Products")
    print("6. View Available Products")
    print("7. View All Customers")
    print("8. Exit")


def main():
    service = SuperMarketService(
        products=InMemoryProductRepository(),
        customers=InMemoryCustomerRepository(),
        orders=InMemoryOrderRepository()
    )

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            try:
                product = service.add_products(pid, name, price, qty)
                print(f"Product added: {product}")
            except Exception as e:
                print(f" {e}")

        elif choice == "2":
            cid = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            email = input("Enter Email: ")
            contact = input("Enter Contact: ")
            try:
                customer = service.add_customers(cid, name, email, contact)
                print(f"Customer added: {customer}")
            except Exception as e:
                print(f"{e}")

        elif choice == "3":
            oid = input("Enter Order ID: ")
            cid = input("Enter Customer ID: ")
            try:
                order = service.add_orders(oid, cid)
                print(f"Order created: {order.order_id}")
            except Exception as e:
                print(f"{e}")

        elif choice == "4":
            oid = input("Enter Order ID: ")
            pid = input("Enter Product ID: ")
            qty = int(input("Enter Quantity: "))
            try:
                service.add_order_item(oid, pid, qty)
                print("Order item added successfully")
            except Exception as e:
                print(f"{e}")

        elif choice == "5":
            print("\nAll Products:")
            for p in service.get_all_products():
                print(f"{p.product_id} - {p.name} - ${p.price} - Qty: {p.quantity}")

        elif choice == "6":
            print("\nAvailable Products:")
            for p in service.get_all_available_products():
                print(f"{p.product_id} - {p.name} - ${p.price} - Qty: {p.quantity}")

        elif choice == "7":
            print("\nAll Customers:")
            for c in service.get_all_customers():
                print(f"{c.customer_id} - {c.customer_name} - {c.email} - {c.contact}")

        elif choice == "8":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
