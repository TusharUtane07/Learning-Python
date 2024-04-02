class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def edit_expense(self, index, new_expense):
        if 0 <= index < len(self.expenses):
            self.expenses[index] = new_expense
            print("Expense edited successfully.")
        else:
            print("Invalid index.")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense deleted successfully.")
        else:
            print("Invalid index.")

    def generate_report(self):
        if not self.expenses:
            print("No records found. Please add expenses first.")
            return

        total_expenses = sum(expense.amount for expense in self.expenses)
        categories = set(expense.category for expense in self.expenses)

        print("\nExpense Report:")
        print(f"Total Expenses: ${total_expenses}")
        print("Category-wise Expenses:")
        for category in categories:
            category_total = sum(expense.amount for expense in self.expenses if expense.category == category)
            print(f"{category}: ${category_total}")

    def display_expenses(self):
        if self.expenses:
            print("All Expenses:")
            for i, expense in enumerate(self.expenses):
                print(f"{i + 1}. Date: {expense.date}, Category: {expense.category}, Description: {expense.description}, Amount: ${expense.amount}")
        else:
            print("No expenses to display.")

def input_expense_details():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: $"))
    return Expense(date, category, description, amount)

if __name__ == "__main__":
    t = ExpenseTracker()

    while True:
        print("\n\nExpense Tracker Menu:")
        print("\n1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. Generate Report")
        print("5. Display All Expenses")
        print("6. Exit")

        choice = input("\nEnter your choice (eg: 1): ")

        if choice == "1":
            expense = input_expense_details()
            t.add_expense(expense)
            print("Expense added successfully.")
        elif choice == "2":
            index = int(input("Enter the index of the expense to edit: ")) - 1
            new_expense = input_expense_details()
            t.edit_expense(index, new_expense)
        elif choice == "3":
            index = int(input("Enter the index of the expense to delete: ")) - 1
            t.delete_expense(index)
        elif choice == "4":
            t.generate_report()
        elif choice == "5":
            t.display_expenses()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

