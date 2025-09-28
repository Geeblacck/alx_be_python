
def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' has been added to your shopping list.")
            else:
                print("⚠️ Item name cannot be empty.")

        elif choice == '2':
            if not shopping_list:
                print("⚠️ Your shopping list is empty, nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"🗑️ '{item}' has been removed from your shopping list.")
                else:
                    print(f"⚠️ '{item}' is not in your shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("🛒 Your shopping list is empty.")

        elif choice == '4':
            print("👋 Goodbye! Thanks for using Shopping List Manager.")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
