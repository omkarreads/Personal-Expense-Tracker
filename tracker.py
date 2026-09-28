from models import Expense
import analytics
import utils
from storage import ExpenseStorage

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.storage = ExpenseStorage(filename)
        self.expenses = []
        self.reload()

    def reload(self):
        data = self.storage.load_data()
        self.expenses = [Expense.make_from_map(x) for x in data]

    def add_expense(self):
        print("\n--- Add New Expense ---")
        dt = utils.parse_input("Enter date (DD-MM-YYYY): ")
        if not Expense.check_date(dt):
            print("Invalid date format!")
            return

        cat = utils.parse_input("Enter category: ")
        cost = utils.parse_input("Enter amount spent: ", float)

        if cost < 0:
            print("Amount cannot be negative!")
            return

        tag = input("Enter tag (Essential/Discretionary/Investment): ").strip() or "Essential"

        item = Expense(cost, dt, cat, tag)
        self.expenses.append(item)
        self.storage.save_data(self.expenses)
        utils.log_event("Added", cat, utils.format_currency(cost))

    def view_expenses(self):
        print("\n--- All Expenses ---")
        if not self.expenses:
            print("No expenses recorded yet!")
            return
        for i, item in enumerate(self.expenses, 1):
            print(f"{i}. {item.show_info()}")

    def calculate_stats(self):
        print("\n--- Expense Statistics ---")
        if not self.expenses:
            print("No data available!")
            return

        s = analytics.calc_stats(self.expenses)
        print(f"Total Spent : {utils.format_currency(s['total'])}")
        print(f"Average     : {utils.format_currency(s['avg'])}")
        print(f"Highest     : {utils.format_currency(s['max'])}")

        print("\nCategory Breakdown:")
        for cat, amt in analytics.cat_breakdown(self.expenses).items():
            print(f"- {cat}: {utils.format_currency(amt)}")

    def search_by_category(self):
        print("\n--- Search Expenses ---")
        if not self.expenses:
            print("No expenses recorded!")
            return

        query = utils.parse_input("Enter category: ").lower()
        matches = [x for x in self.expenses if x.cat.lower() == query]

        if not matches:
            print("No matching expenses.")
            return

        for item in matches:
            print(item.show_info())

    def delete_expense(self):
        print("\n--- Delete Expense ---")
        if not self.expenses:
            print("Nothing to delete!")
            return

        self.view_expenses()
        num = utils.parse_input("\nEnter number to delete: ", int)

        if 1 <= num <= len(self.expenses):
            removed = self.expenses.pop(num - 1)
            self.storage.save_data(self.expenses)
            utils.log_event("Deleted", removed.cat, utils.format_currency(removed.cost))
        else:
            print("Invalid selection!")
