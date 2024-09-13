class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    # Add or update an expense
    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    # Delete an expense category
    def delete_expense(self, category):
        if category in self.expenses:
            del self.expenses[category]
            print(f"Deleted {category} successfully.")
        else:
            print(f"Category '{category}' not found.")

    # View all expenses
    def view_expenses(self):
        print("\nExpense Tracker")
        print("-----------------------------")
        total_expenses = 0
        if not self.expenses:
            print("No expenses to show.")
        else:
            print(f"{'Category':<15} {'Amount ($)':>10}")
            print("-----------------------------")
            for category, amount in self.expenses.items():
                print(f"{category:<15} {amount:>10.2f}")
                total_expenses += amount
            print("-----------------------------")
            print(f"{'Total Expenses':<15} {total_expenses:>10.2f}")

    # Save all expenses to a text file
    def save_expenses(self, filename):
        try:
            with open(filename, 'w') as file:
                for category, amount in self.expenses.items():
                    file.write(f"{category},{amount}\n")
            print("All expenses saved successfully!")
        except IOError:
            print("Error saving expenses to the file.")

    # Save a single category of expenses to a text file
    def save_expense_category(self, category, filename):
        if category in self.expenses:
            try:
                with open(filename, 'w') as file:
                    file.write(f"{category},{self.expenses[category]}\n")
                print(f"Expense for '{category}' saved successfully in {filename}!")
            except IOError:
                print("Error saving expense to the file.")
        else:
            print(f"Category '{category}' not found.")

    # Load expenses from a text file
    def load_expenses(self, filename):
        try:
            with open(filename, 'r') as file:
                self.expenses.clear()
                for line in file:
                    category, amount = line.strip().split(',')
                    self.expenses[category] = float(amount)
            print("Expenses loaded successfully!")
        except FileNotFoundError:
            print("File not found. No expenses loaded.")
        except ValueError:
            print("Error loading expenses. The file format might be incorrect.")
        except IOError:
            print("Error reading the file.")

    # Clear all expenses
    def clear_expenses(self):
        self.expenses = {}
        print("All expenses cleared!")

    # Main function to handle user choices
    def start(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Delete Expense")
            print("4. Clear All Expenses")
            print("5. Save Expenses (All Categories)")
            print("6. Save Expense for Specific Category")
            print("7. Load Expenses")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                category = input("Enter expense category: ").strip()
                try:
                    amount = float(input("Enter expense amount: "))
                    self.add_expense(category, amount)
                    print("Expense added successfully!")
                except ValueError:
                    print("Invalid input. Please enter a valid number for amount.")
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                category = input("Enter category to delete: ").strip()
                self.delete_expense(category)
            elif choice == '4':
                confirmation = input("Are you sure you want to clear all expenses? (y/n): ").lower()
                if confirmation == 'y':
                    self.clear_expenses()
                else:
                    print("Clear expenses cancelled.")
            elif choice == '5':
                filename = input("Enter filename to save all expenses: ").strip()
                self.save_expenses(filename)
            elif choice == '6':
                category = input("Enter category to save: ").strip()
                filename = input("Enter filename to save this category: ").strip()
                self.save_expense_category(category, filename)
            elif choice == '7':
                filename = input("Enter filename to load expenses: ").strip()
                self.load_expenses(filename)
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    tracker = ExpenseTracker()
    tracker.start()

if __name__ == "__main__":
    main()
