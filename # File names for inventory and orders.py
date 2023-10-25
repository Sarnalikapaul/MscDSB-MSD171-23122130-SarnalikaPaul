# File names for inventory and orders
inventory_file = "inventory.txt"
orders_file = "orders.txt"

class SportMart:
    def _init_(self):
        self.inventory = {}
        self.orders = []

    def read_inventory(self):
        with open(inventory_file, 'r') as file:
            for line in file:
                item_name, item_price, quantity = line.strip().split(',')
                self.inventory[item_name] = {'price': float(item_price), 'quantity': int(quantity)}

    def read_orders(self):
        with open(orders_file, 'r') as file:
            for line in file:
                order_id, customer_name, item_name, item_quantity = line.strip().split(',')
                self.orders.append({'order_id': int(order_id), 'customer_name': customer_name, 'item_name': item_name, 'item_quantity': int(item_quantity)})

    def add_item_to_inventory(self, item_name, item_price, quantity):
        if item_name not in self.inventory:
            self.inventory[item_name] = {'price': item_price, 'quantity': quantity}
            self.save_inventory()

    def place_order(self, customer_name, item_name, item_quantity):
        if item_name in self.inventory and self.inventory[item_name]['quantity'] >= item_quantity:
            order_id = len(self.orders) + 1
            self.orders.append({'order_id': order_id, 'customer_name': customer_name, 'item_name': item_name, 'item_quantity': item_quantity})
            self.inventory[item_name]['quantity'] -= item_quantity
            self.save_orders()
            self.save_inventory()
            print("Order placed successfully.")
        else:
            print("Item not available or insufficient quantity in inventory.")

    def display_inventory(self):
        print("Inventory:")
        for item, details in self.inventory.items():
            print(f"{item} - Price: ${details['price']}, Quantity: {details['quantity']}")

    def display_order_history(self):
        print("Order History:")
        for order in self.orders:
            print(f"Order ID: {order['order_id']}, Customer: {order['customer_name']}, Item: {order['item_name']}, Quantity: {order['item_quantity']}")

    def save_inventory(self):
        with open(inventory_file, 'w') as file:
            for item, details in self.inventory.items():
                file.write(f"{item},{details['price']},{details['quantity']}\n")

    def save_orders(self):
        with open(orders_file, 'w') as file:
            for order in self.orders:
                file.write(f"{order['order_id']},{order['customer_name']},{order['item_name']},{order['item_quantity']}\n")

def main():
    trinity_store = SportMart()
    trinity_store.read_inventory()
    trinity_store.read_orders()

    while True:
        print("\nSportMart Menu:")
        print("1. Display Inventory")
        print("2. Display Order History")
        print("3. Add Item to Inventory")
        print("4. Place Order")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            trinity_store.display_inventory()
        elif choice == "2":
            trinity_store.display_order_history()
        elif choice == "3":
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            trinity_store.add_item_to_inventory(item_name, item_price, item_quantity)
        elif choice == "4":
            customer_name = input("Enter customer name: ")
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            trinity_store.place_order(customer_name, item_name, item_quantity)
        elif choice == "5":
            trinity_store.save_inventory()
            trinity_store.save_orders()
            print("Exiting SportMart. Inventory and orders have been saved to text files.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


