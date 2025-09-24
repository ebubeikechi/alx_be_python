def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter the item to add: ")
            shopping_list.append(item_name)
            pass
        elif choice == '2':
            item_name = input("Enter item name: ")

            if item_name in shopping_list:
                shopping_list.remove(item_name)
            else:
                print(f"{item_name} is not an item in the list")
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()