from tracker import ExpenseTracker

def show_menu():
    print("\n" + "=" * 25)
    print("  STUDENT EXPENSE TRACKER")
    print("=" * 25)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Statistics & Breakdown")
    print("4. Search Expenses by Category")
    print("5. Delete an Expense")
    print("6. Exit")
    print("=" * 25)

def main():
    tracker = ExpenseTracker()

    while True:
        show_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.calculate_stats()
        elif choice == "4":
            tracker.search_by_category()
        elif choice == "5":
            tracker.delete_expense()
        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
