from models import Expense, Transaction
import analytics
import utils

def run_tests():
    print("Running tests...")

    e = Expense(250.0, "15-09-2026", "Food", "Essential")
    assert e.cost == 250.0
    assert e.cat == "Food"
    assert e.tag == "Essential"
    print("Expense creation test passed.")

    assert Transaction.check_date("12-05-2026") == True
    assert Transaction.check_date("2026/05/12") == False
    print("Date validation test passed.")

    test_data = [
        Expense(100.0, "01-01-2026", "Food"),
        Expense(200.0, "02-01-2026", "Travel"),
        Expense(300.0, "03-01-2026", "Food")
    ]
    
    stats = analytics.calc_stats(test_data)
    assert stats["total"] == 600.0
    assert stats["avg"] == 200.0
    assert stats["max"] == 300.0
    print("Analytics test passed.")

    assert utils.format_currency(150.5) == "Rs. 150.50"
    print("Formatting test passed.")

    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    run_tests()
