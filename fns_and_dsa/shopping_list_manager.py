def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number 1-4.")
            continue

        if choice == 1:
            item = input("Item to add: ").strip()
            if item: shopping_list.append(item); print(f"'{item}' added.")
        elif choice == 2:
            item = input("Item to remove: ").strip()
            if item in shopping_list: shopping_list.remove(item); print(f"'{item}' removed.")
            else: print(f"'{item}' not found.")
        elif choice == 3:
            print("Shopping List:" if shopping_list else "Shopping list is empty.")
            for i, item in enumerate(shopping_list, 1): print(f"{i}. {item}")
        elif choice == 4:
            print("Goodbye!"); break
        else:
            print("Invalid choice. Enter a number 1-4.")

if __name__ == "__main__":
    main()
