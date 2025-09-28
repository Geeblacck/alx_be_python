# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # list (array)

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))  # must be integer

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(item + " has been added.")

        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(item + " has been removed.")
            else:
                print(item + " not found in the list.")

        elif choice == 3:
            if shopping_list:
                print("Current Shopping List:")
                for i in shopping_list:
                    print(i)
            else:
                print("The shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
