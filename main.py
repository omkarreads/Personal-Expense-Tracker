from tracker import ExpenseTracker

def show_menu():
    print("\n" + "=" * 25)
    print("  STUDENT EXPENSE TRACKER")
    print("=" * 25)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Statistics & Breakdown")
    print("4. Search Expenses by Category")
    print("5. Storage Options")
    print("6. Delete an Expense")
    print("7. Exit")
    print("=" * 25)

def main():
    tracker = ExpenseTracker()

    while True:
        show_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.calculate_stats()
        elif choice == "4":
            tracker.search_by_category()
        elif choice == "5":
            # Call your storage options method here
            tracker.storage_options()  # Adjust method name if it's named differently in tracker.py
        elif choice == "6":
            tracker.delete_expense()
        elif choice == "7":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
