import json

class ExpenseStorage:
    def __init__(self, filename="expenses.json"):
        self.filename = filename

    def save_data(self, expense_objects):
        raw_list = [item.convert_to_map() for item in expense_objects]
        try:
            with open(self.filename, "w") as f:
                json.dump(raw_list, f, indent=4)
            return True
        except Exception:
            return False

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                raw_list = json.load(f)
                return raw_list
        except (FileNotFoundError, json.JSONDecodeError):
            return []
