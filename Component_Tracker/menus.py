from inventory import (search_item, use_item, edit_item,
    add_new_item, remove_item, overall_report)


#  Engineer Menu
def engineer_menu(user):    #passing user into the functions that modify data, to allow logging
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
            use_item(input("Enter item name: ").strip(), user)     #passing user into the functions that modify data, to allow logging
        elif choice == '3':
            edit_item(input("Enter item name: ").strip(), user)    #passing user into the functions that modify data, to allow logging
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

#  Manager Menu
def manager_menu(user):             #passing user into the functions that modify data, to allow logging
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
            edit_item(input("Enter item name: ").strip(), user)     #passing user into the functions that modify data, to allow logging
        elif choice == '3':
            add_new_item(user)                                      # Line changed to add (user) to fix bug B1
        elif choice == '4':
            remove_item(input("Enter item name: ").strip(), user)    #passing user into the functions that modify data, to allow logging
        elif choice == '5':
            overall_report()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")