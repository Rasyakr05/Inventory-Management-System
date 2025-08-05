class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.item_id} | {self.name} | Qty: {self.quantity} | Price: {self.price}"
