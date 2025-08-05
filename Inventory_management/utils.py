import json
from item import Item

def save_inventory_to_file(inventory, filename="data.json"):
    data = {}
    for item_id, item in inventory.items():
        data[item_id] = {
            "name": item.name,
            "quantity": item.quantity,
            "price": item.price
        }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved to {filename}")

def load_inventory_from_file(filename="data.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        inventory_data = {}
        for item_id, item_info in data.items():
            inventory_data[item_id] = Item(item_id, item_info["name"], item_info["quantity"], item_info["price"])
        print(f"Inventory loaded from {filename}")
        return inventory_data
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty inventory.")
        return {}

def sort_items(items, sort_by="name"):
    return sorted(items, key=lambda x: getattr(x, sort_by))

