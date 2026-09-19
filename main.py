import numpy as np

# List to store all our expense records
expenses = []

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

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Books, etc.): ")
    
    # Simple input validation using a loop
    while True:
        try:
            amount = float(input("Enter amount spent: "))
            if amount < 0:
                print("Amount cannot be negative! Try again.")
                continue
            break
        except:
            print("Invalid input! Please enter a valid number for amount.")
            
    # Storing data in a dictionary
    expense_item = {
        "date": date,
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense_item)
    print("\nSuccess: Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")
    if len(expenses) == 0:
        print("No expenses recorded yet!")
        return
    
    count = 1
    for item in expenses:
        print("{}. Date: {} | Category: {} | Amount: Rs. {:.2f}".format(
            count, item["date"], item["category"], item["amount"]
        ))
        count = count + 1

def calculate_stats():
    print("\n--- Expense Statistics ---")
    if len(expenses) == 0:
        print("No data available to calculate statistics.")
        return
    
    # Extracting amounts into a list to use numpy
    amount_list = []
    for item in expenses:
        amount_list.append(item["amount"])
        
    # Converting to numpy array
    amounts_array = np.array(amount_list)
    
    total_spent = np.sum(amounts_array)
    average_spent = np.mean(amounts_array)
    max_spent = np.max(amounts_array)
    
    print("Total Money Spent   : Rs. {:.2f}".format(total_spent))
    print("Average Per Expense : Rs. {:.2f}".format(average_spent))
    print("Highest Single Spend: Rs. {:.2f}".format(max_spent))

def search_by_category():
    print("\n--- Search Expenses ---")
    if len(expenses) == 0:
        print("No expenses recorded yet!")
        return
        
    search_cat = input("Enter category to search for: ")
    found = False
    
    print("\nSearch Results for '{}':".format(search_cat))
    for item in expenses:
        # Simple case-insensitive comparison using .lower()
        if item["category"].lower() == search_cat.lower():
            print("Date: {} | Amount: Rs. {:.2f}".format(item["date"], item["amount"]))
            found = True
            
    if found == False:
        print("No expenses found under this category.")

def delete_expense():
    print("\n--- Delete Expense ---")
    if len(expenses) == 0:
        print("No expenses available to delete!")
        return
    
    # First show all expenses with their numbers
    view_expenses()
    
    try:
        item_num = int(input("\nEnter the expense number you want to delete: "))
        
        # Checking if index is valid (converting 1-based index to 0-based index)
        if item_num >= 1 and item_num <= len(expenses):
            removed_item = expenses.pop(item_num - 1)
            print("\nSuccess: Removed expense for '{}' of Rs. {:.2f}".format(
                removed_item["category"], removed_item["amount"]
            ))
        else:
            print("Invalid expense number!")
    except:
        print("Please enter a valid number!")

# Main program execution loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        calculate_stats()
    elif choice == '4':
        search_by_category()
    elif choice == '5':
        delete_expense()
    elif choice == '6':
        print("\nThank you for using Personal Expense Tracker. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")
