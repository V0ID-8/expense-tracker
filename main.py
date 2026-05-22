from datetime import date 

def show_menu():
    print("\n" + "="*40)
    print("         Expense Tracker")
    print("="*40)
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Total spending")
    print("4. Exit")
    print("="*40)\
    

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter the expense amount: ").strip())
            if amount < 0:
                print("Amount cannot be negative. Please enter a greater than zero.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")


def get_valid_date():
    while True:
        date_input = input(f" Date (YYYY-MM-DD) [press Enter for today's date] ").strip()
        if date_input == "":
            return str(date.today())
        try:
            date.fromisoformat(date_input)
            return date_input
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


CATEGORIES = ["Food", "Transport", "Shopping", "Health", "Bills", "Other"]


def get_valid_category():
    print("\n Select a category:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
    while True:
        try:
            choice = int(input("Enter the category number: ").strip())
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the category.")



def add_expense():
        print("\n" + "="*40)
        print("         Add New Expense")
        print("="*40)

        title = input("Title: ").strip()
        while not title:
            print("Title cannot be empty. Please enter a valid title.")
            title = input("Title: ").strip()

        amount = get_valid_amount()
        category = get_valid_category() 
        expense_date = get_valid_date()

        expense = {
            "title": title,
            "amount": amount,
            "category": category,
            "date": expense_date
        }

        print("\n Expense added successfully!")
        print(f"   {title} | OMR{amount:.2f} | {category} | {expense_date}")
        return expense


def main():
    expenses = []

    while True:
        show_menu()
        choice = input("Enter your choice(1-4): ").strip()
        
        if choice == "1":
            expense = add_expense()
            expenses.append(expense)
        elif choice == "2":
            print("\n [View Expenses - Coming Soon]")
        elif choice == "3":
            print("\n [Total Spending - Coming Soon]")
        elif choice == "4":
            print("\n Goodbye! Stay on budget!\n")
            break
        else:
            print("\n  Invalid choice. Please enter 1 to 4.")

if __name__ == "__main__":
    main()    