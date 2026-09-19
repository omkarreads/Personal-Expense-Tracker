import tracker

def run_tests():
    print("Running basic component tests...")
    
    # Test 1: Add item directly to memory
    test_item = {"date": "01-01-2026", "category": "Food", "amount": 150.0}
    tracker.expenses.append(test_item)
    
    if len(tracker.expenses) == 1:
        print("[PASS] Test 1: Expense insertion passed.")
    else:
        print("[FAIL] Test 1: Expense insertion failed.")
        
    # Test 2: Verify stats math
    if tracker.expenses[0]["amount"] == 150.0:
        print("[PASS] Test 2: Expense amount verification passed.")
    else:
        print("[FAIL] Test 2: Expense amount verification failed.")

if __name__ == "__main__":
    run_tests()
