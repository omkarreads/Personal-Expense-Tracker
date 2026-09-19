import tracker

def show_menu():
    print("\n" + "="*30)
    print("   PERSONAL EXPENSE TRACKER   ")
    print("="*30)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Calculate Total and Average Spent")
    print("4. Search Expense by Category")
    print("5. Delete an Expense")
    print("6. Exit")
    print("="*30)

# Main execution loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        tracker.add_expense()
    elif choice == '2':
        tracker.view_expenses()
    elif choice == '3':
        tracker.calculate_stats()
    elif choice == '4':
        tracker.search_by_category()
    elif choice == '5':
        tracker.delete_expense()
    elif choice == '6':
        print("\nThank you for using Personal Expense Tracker. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")
