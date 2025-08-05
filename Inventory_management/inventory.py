from item import Item
from utils import save_inventory_to_file, load_inventory_from_file, sort_items
class Inventory:
    def __init__(self):
        self.items = load_inventory_from_file()

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            print("Item ID already exists. Updating quantity.")
            self.items[item_id].quantity += quantity
        else:
            self.items[item_id] = Item(item_id, name, quantity, price)
        print(f"Item '{name}' added/updated successfully.")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item ID {item_id} deleted.")
        else:
            print("Item not found.")

    def update_item(self, item_id, quantity=None, price=None):
        if item_id in self.items:
            if quantity is not None:
                self.items[item_id].quantity = quantity
            if price is not None:
                self.items[item_id].price = price
            print(f"Item ID {item_id} updated.")
        else:
            print("Item not found.")

    def search_item(self, item_id):
        return self.items.get(item_id, None)

    def display_inventory(self, sort_by="name"):
        sorted_items = sorted(self.items.values(), key=lambda x: getattr(x, sort_by))
        print("Inventory List:")
        for item in sorted_items:
            print(item)

    def low_stock_alert(self, threshold):
        print("Low Stock Items:")
        for item in self.items.values():
            if item.quantity <= threshold:
                print(item)

    def total_inventory_value(self):
        total = sum(item.quantity * item.price for item in self.items.values())
        print(f"Total Inventory Value: ₹{total}")

    def save_data(self):
        save_inventory_to_file(self.items)

    def display_inventory(self, sort_by="name"):
        sorted_items = sort_items(self.items.values(), sort_by)
        print("Inventory List:")
        for item in sorted_items:
            print(item)