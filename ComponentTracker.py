import csv
import os

#  Hardcoded credentials
Users = {
    "ENGINEER": "ENGINEER",
    "MANAGER": "MANAGER"
}

CSV_FILE = 'inventory.csv'

#  Create CSV with set headers if non-existant
# ******WOULD LIKE TO ADD IN CHECK HERE IF NOT EXISTING "WOULD YOU LIKE TO CREATE NEW CSV"
def check_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            fieldnames = ['name', 'type', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()


#  Login Menu
def login_menu():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username in Users and Users[username] == password:
            print(f"Welcome {username}!")
            if username == "ENGINEER":    #*********DEPENDS ON EXACT STRING, NEEDS AMENDING FOR SECURITY ********
                engineer_menu()
            else:
                manager_menu()
            break
        else:
            print("Invalid details. Please try again.\n")

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
# ******************COULD USE SOME CODE TO CHOOSE HOW MANY OF THE ITEMS TO USE**************
def use_item(name):
    name = name.strip()
    inventory = load_inventory()
    for item in inventory:
        if item['name'].strip().lower() == name.lower():
            if int(item['quantity']) > 0:
                item['quantity'] = str(int(item['quantity']) - 1)
                save_inventory(inventory)
                print(f"Used one {item['name']}. Remaining: {item['quantity']}")
            else:
                print("Item out of stock!")
            return
    print("Item not found.")

#  Edit Item (Available to both users)
def edit_item(name):
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
            print(f"{item['name']} updated to {item['quantity']} units.")
            return
    print("Item not found.")

#  Add New Item (Manager Only)
def add_new_item():
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
    print(f"{name} added to inventory.")

#  Remove Item (Manager Only)
def remove_item(name):
    name = name.strip()
    inventory = load_inventory()
    new_inventory = [item for item in inventory if item['name'].strip().lower() != name.lower()]
    if len(new_inventory) == len(inventory):
        print("Item not found.")
    else:
        save_inventory(new_inventory)
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

#  Engineer Menu
def engineer_menu():
    while True:
        print("\nENGINEER MENU:")
        print("1. Search Item")
        print("2. Use Item")
        print("3. Edit Item")
        print("4. Logout")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            search_item(input("Enter item name: ").strip())
        elif choice == '2':
            use_item(input("Enter item name: ").strip())
        elif choice == '3':
            edit_item(input("Enter item name: ").strip())
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

#  Manager Menu
def manager_menu():
    while True:
        print("\nMANAGER MENU:")
        print("1. Search Item")
        print("2. Edit Item")
        print("3. Add Item")
        print("4. Remove Item")
        print("5. Overall Report")
        print("6. Logout")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            search_item(input("Enter item name: ").strip())
        elif choice == '2':
            edit_item(input("Enter item name: ").strip())
        elif choice == '3':
            add_new_item()
        elif choice == '4':
            remove_item(input("Enter item name: ").strip())
        elif choice == '5':
            overall_report()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

#  Start Program
if __name__ == "__main__":
    check_csv()
    login_menu()
