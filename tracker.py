import numpy as np

# Core storage for expenses
expenses = []

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Books, etc.): ")
    
    while True:
        try:
            amount = float(input("Enter amount spent: "))
            if amount < 0:
                print("Amount cannot be negative! Try again.")
                continue
            break
        except:
            print("Invalid input! Please enter a valid number for amount.")
            
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
    
    amount_list = []
    for item in expenses:
        amount_list.append(item["amount"])
        
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
    
    view_expenses()
    
    try:
        item_num = int(input("\nEnter the expense number you want to delete: "))
        if item_num >= 1 and item_num <= len(expenses):
            removed_item = expenses.pop(item_num - 1)
            print("\nSuccess: Removed expense for '{}' of Rs. {:.2f}".format(
                removed_item["category"], removed_item["amount"]
            ))
        else:
            print("Invalid expense number!")
    except:
        print("Please enter a valid number!")
