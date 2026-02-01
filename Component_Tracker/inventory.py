import csv
from file_setup import CSV_FILE
from history_log import log_action            #gives inventory functions access to the logging tool


#  Load CSV Inventory
def load_inventory():
    with open(CSV_FILE, mode='r', newline='') as file:
        return list(csv.DictReader(file))

#  Save CSV Inventory
def save_inventory(inventory):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['name', 'type', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)

#  Search Item (Available to both users)
def search_item(name):
    name = name.strip()
    inventory = load_inventory()
    for item in inventory:
        if item['name'].strip().lower() == name.lower():
            print(f"{item['name']} has {item['quantity']} units.")
            return
    print("Item not found.")

#  Use Item (Engineer Only)
def use_item(name, user):      #passing user as a parameter into the functions that modify data, to allow logging
    name = name.strip()
    inventory = load_inventory()
    for item in inventory:
        if item['name'].strip().lower() == name.lower():
            current_qty = int(item['quantity'])
            if current_qty <= 0:
                print("Item out of stock!")
                return
            print(f"Current stock of {item['name']}: {current_qty}")                      #helpful prompt to show stock before use and reduces invalid inputs
            try:
                amount = int(input(f"How many '{item['name']}' would you like to use? ")) #ask how many to use
            except ValueError:                                                            #handle input error
                print("Please enter a valid number.")
                return
            if amount <= 0:                                                               #input validation
                print("You must use at least one.")
                return
            if amount > current_qty:                                                      #only allow use of items in stock
                print(f"Not enough in stock. You only have {current_qty}.")
                return
            item['quantity'] = str(current_qty - amount)                                  #update quantity
            save_inventory(inventory)
            log_action(user, f"Used {amount} of {item['name']}. New quantity: {item['quantity']}")     #logs user and action performed into the history log
            print(f"Used {amount} of {item['name']}. Remaining: {item['quantity']}")
            return
    print("Item not found.")


#  Edit Item (Available to both users)
def edit_item(name, user):       #passing user as a parameter into the functions that modify data, to allow logging
    name = name.strip()
    inventory = load_inventory()
    for item in inventory:
        if item['name'].strip().lower() == name.lower():
            while True:
                change_input = input("Enter quantity to add or remove (use negative for removal): ")
                if not change_input:
                    print("No input detected, Please enter a number.")
                    continue
                try:
                    change = int(change_input)
                    break
                except ValueError:
                    print("Invalid input. Please use a number")
            current_quantity = int(item['quantity'])
            new_quantity = current_quantity + change
            if new_quantity < 0:
                print(f"Can't remove {abs(change)} units. Only {current_quantity} available.")
                return
            item['quantity'] = str(max(0, int(item['quantity']) + change))
            save_inventory(inventory)
            log_action(user, f"Edited {item['name']}: change {change}, new quantity {item['quantity']}")      #logs user and action performed into the history log
            print(f"{item['name']} updated to {item['quantity']} units.")
            return
    print("Item not found.")

#  Add New Item (Manager Only)
def add_new_item(user):       #passing user as a parameter into the functions that modify data, to allow logging
    name = input("Enter item name: ").strip()
    type_ = input("Enter item type: ").strip()
    while True:
        quantity_input = input("Enter numeric quantity: ").strip()
        try:
            quantity = int(quantity_input)
            if quantity < 0:
                print("Invalid input. Quantity cannot be negative")
                continue
            break
        except ValueError:
            print("Invalid input. Quantity must be a number")
    inventory = load_inventory()
    inventory.append({'name': name, 'type': type_, 'quantity': quantity})
    save_inventory(inventory)
    log_action(user, f"Added item: {name}, type: {type_}, quantity: {quantity}")   # logs user and action performed into the history log
    print(f"{name} added to inventory.")

#  Remove Item (Manager Only)
def remove_item(name, user):       #passing user as a parameter into the functions that modify data, to allow logging
    name = name.strip()
    inventory = load_inventory()
    new_inventory = [item for item in inventory if item['name'].strip().lower() != name.lower()]
    if len(new_inventory) == len(inventory):
        print("Item not found.")
    else:
        save_inventory(new_inventory)
        log_action(user, f"Removed item: {name}")    # logs user and action performed into the history log
        print(f"{name} removed from inventory.")

#  Overall Report (Manager Only)
def overall_report():
    inventory = load_inventory()
    if not inventory:
        print ("Inventory Empty.")
        return
    print("\nInventory Report:")
    for item in inventory:
        print(f"{item['name'].strip()} ({item['type'].strip()}): {item['quantity'].strip()} units")