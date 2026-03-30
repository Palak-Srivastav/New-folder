# Program 2: Inventory Management System

# 1. Add Items
inventory = {"Laptop": 5, "Mouse": 10, "Keyboard": 7}
print("Added items:", inventory)

# 2. Update Quantity
inventory["Laptop"] = 8
inventory["Mouse"] += 5  
print("Updated quantities:", inventory)

# 3. Remove Item
del inventory["Keyboard"]
print("Removed Keyboard:", inventory)

# 4. Show Final Inventory
print("\n--- Final Inventory List ---")
for item, qty in inventory.items():
    print(f"Item: {item} | Quantity: {qty}")