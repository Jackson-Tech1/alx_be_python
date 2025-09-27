def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    actions = {
        '1': lambda: add_item(shopping_list),
        '2': lambda: remove_item(shopping_list),
        '3': lambda: view_list(shopping_list),
        '4': lambda: exit_program()
    }

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        action = actions.get(choice, lambda: print("Invalid choice. Please try again."))
        action()

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' added.")
    else:
        print("No item entered.")

def remove_item(shopping_list):
    item = input("Enter item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed.")
    else:
        print(f"'{item}' not found.")

def view_list(shopping_list):
    if shopping_list:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Shopping list is empty.")

def exit_program():
    print("Goodbye!")
    exit()

if __name__ == "__main__":
    main()
