from inventory import Inventory

def menu():
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Update Item")
    print("4. Search Item")
    print("5. Display Inventory")
    print("6. Low Stock Alerts")
    print("7. Total Inventory Value")
    print("0. Exit")

if __name__ == "__main__":
    inv = Inventory()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            item_id = input("Item ID: ")
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            inv.add_item(item_id, name, quantity, price)
            inv.save_data()
        elif choice == "2":
            item_id = input("Item ID to delete: ")
            inv.delete_item(item_id)
            inv.save_data()
        elif choice == "3":
            item_id = input("Item ID to update: ")
            quantity = input("New Quantity (leave blank if no change): ")
            price = input("New Price (leave blank if no change): ")
            inv.update_item(item_id, int(quantity) if quantity else None, float(price) if price else None)
            inv.save_data()
        elif choice == "4":
            item_id = input("Item ID to search: ")
            item = inv.search_item(item_id)
            if item:
                print(item)
            else:
                print("Item not found.")

        elif choice == "5":
            sort_by = input("Sort by (name/quantity/price): ").strip().lower()
            inv.display_inventory(sort_by if sort_by in ["name", "quantity", "price"] else "name")

        elif choice == "6":
            threshold = int(input("Enter low stock threshold: "))
            inv.low_stock_alert(threshold)

        elif choice == "7":
            inv.total_inventory_value()

        elif choice == "0":
            print("Exiting Program.")
            break

        else:
            print("Invalid choice! Try again.")
