class Expense:
    def __init__(self, amount, category, date):
        self._amount = amount
        self._category = category
        self._date = date
    
    def __str__(self):
        return f"{self._date} | ${self._amount} | {self._category}"
    
def display_menu():
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def main():
    print("Expense Tracker - Basic Version")
    
if __name__ == "__main__":
    main()