def storage_options(self):
        print("\n--- Storage Options ---")
        print("1. Switch Storage Format / File")
        print("2. Reload Data from Storage")
        print("3. Export / Backup Data")
        
        choice = utils.parse_input("Select an option (1-3): ")
        
        if choice == "1":
            new_file = input("Enter new filename (e.g. expenses.json or expenses.csv): ").strip()
            if new_file:
                self.storage = ExpenseStorage(new_file)
                self.reload()
                print(f"Switched storage file to '{new_file}'.")
        elif choice == "2":
            self.reload()
            print("Data reloaded successfully!")
        elif choice == "3":
            # Saves current state explicitly
            self.storage.save_data(self.expenses)
            print("Data backup complete!")
        else:
            print("Invalid option!")
