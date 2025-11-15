import json
import os

class Expense:
    def __init__(self, amount, category, date):
        self._amount = amount
        self._category = category
        self._date = date
    
    def __str__(self):
        return f"{self._date} | ${self._amount} | {self._category}"

EXPENSE_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            data = json.load(file)
            expenses = []
            for item in data:
                expense = Expense(item["amount"], item["category"], item["date"], "")
                expenses.append(expense)
            return expenses
    return []

def save_expenses(expenses):
    data = [{"amount": e._amount, "category": e._category, "date": e._date} for e in expenses]
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(data, file, indent=4)
    print("Saved!")

def add_expense(expenses):
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Amount: $"))
        category = input("Category: ")
        date = input("Date (YYYY-MM-DD): ")
        expense = Expense(amount, category, date)
        expenses.append(expense)
        print("Added!")
    except:
        print("Error!")   

def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses.")
        return
    total = 0
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense}")
        total += expense._amount
    print(f"\nTotal: ${total:.2f}")

def edit_expense(expenses):
    print("\n--- Edit Expense ---")
    if not expenses:
        print("No expenses.")
        return
    view_expenses(expenses)
    try:
        index = int(input("Number to edit: ")) - 1
        if 0 <= index < len(expenses):
            expense = expenses[index]
            amount = input(f"New amount (${expense._amount}): ")
            if amount:
                expense._amount = float(amount)
            print("Updated!")
    except:
        print("Error!") 

def delete_expense(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses.")
        return
    view_expenses(expenses)
    try:
        index = int(input("Number to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"Deleted: {deleted}")
    except:
        print("Error!")

def display_menu():
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def main():
    print("Expense Tracker - Basic Version")
    
if __name__ == "__main__":
    main()