class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Item:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def cost_calculation(self, discount):
        total_cost = sum(item.cost * item.quantity for item in self.items)
        if discount != 0:
            total_cost *= (1 - discount)  # Apply discount
        total_cost += total_cost * 0.0625  # Add tax
        return total_cost

class Inventory:
    def __init__(self):
        self.items = {}

    def update_inventory(self, items, increase=True):
        for item in items:
            if item.name in self.items:
                if increase:
                    self.items[item.name] += item.quantity
                else:
                    self.items[item.name] -= item.quantity
            else:
                self.items[item.name] = item.quantity

    def check_for_item(self, item):
        return item.name in self.items and self.items[item.name] >= item.quantity

class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")

class OrderConfirmation:
    def __init__(self, email_service):
        self.email_service = email_service

    def send_confirmation(self, email):
        self.email_service.send_email(email, "Order Confirmation")

def main():
    customer = Customer("Kevin Endrijaitis", "kevin@email.com", "1 Peck Hall")
    items = [Item("Shirts", 20.0, 2), Item("Pants", 30.0, 1)]
    discount = 0.1
    inventory = Inventory()
    inventory.update_inventory(items)
    order = Order(customer, items)

    total_cost = order.cost_calculation(discount)
    print("Total cost of the order:", total_cost)

    for item in items:
        if inventory.check_for_item(item):
            print(f"{item.quantity} {item.name} available in inventory.")
        else:
            print(f"{item.quantity} {item.name} not available in inventory.")

    email_service = EmailService()
    order_confirmation = OrderConfirmation(email_service)
    order_confirmation.send_confirmation(customer.email)

if __name__ == "__main__":
    main()
