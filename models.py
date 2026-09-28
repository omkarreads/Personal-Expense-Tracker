from datetime import datetime

class Transaction:
    def __init__(self, cost, date):
        self._cost = cost
        self.date = date

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, num):
        if num < 0:
            raise ValueError("Amount cannot be negative")
        self._cost = num

    def show_info(self):
        return f"{self.date} | Rs. {self._cost:.2f}"

    @staticmethod
    def check_date(dt):
        try:
            datetime.strptime(dt, "%d-%m-%Y")
            return True
        except ValueError:
            return False

class Expense(Transaction):
    tag_options = frozenset(["Essential", "Discretionary", "Investment"])

    def __init__(self, cost, date, cat, tag="Essential"):
        super().__init__(cost, date)
        self.cat = cat
        self.tag = tag if tag in self.tag_options else "Discretionary"

    def show_info(self):
        return f"{self.date} | {self.cat} ({self.tag}) | Rs. {self._cost:.2f}"

    @classmethod
    def make_from_map(cls, item):
        return cls(
            cost=item.get("amount", 0.0),
            date=item.get("date", ""),
            cat=item.get("category", "Uncategorized"),
            tag=item.get("exp_type", "Essential")
        )

    def convert_to_map(self):
        return {
            "amount": self._cost,
            "date": self.date,
            "category": self.cat,
            "exp_type": self.tag
        }
