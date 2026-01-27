from auth import validate_user, get_role
from menus import engineer_menu, manager_menu
from file_setup import check_csv


def login_menu():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if validate_user(username, password):
            print(f"Welcome {username}!")
            role = get_role(username)

            if role == "ENGINEER":
                engineer_menu()
            else:
                manager_menu()
            break
        else:
            print("Invalid details. Please try again.\n")

if __name__ == "__main__":
    check_csv()
    login_menu()