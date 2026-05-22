from datetime import date
from utils.storage import load_expenses, save_expenses


def show_menu():
    print("\n" + "="*40)
    print("EXPENSE TRACKER")
    print("="*40)
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. View Total Spending")
    print("  4. Exit")
    print("="*40)


def get_valid_amount():
    while True:
        try:
            amount = float(input("  Amount ($): ").strip())
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Please enter a valid number.")


def get_valid_date():
    while True:
        date_input = input(f"  Date (YYYY-MM-DD) [press Enter for today]: ").strip()
        if date_input == "":
            return str(date.today())
        try:
            date.fromisoformat(date_input)
            return date_input
        except ValueError:
            print("  Invalid date format. Use YYYY-MM-DD.")


CATEGORIES = ["Food", "Transport", "Shopping", "Health", "Bills", "Other"]


def get_valid_category():
    print("  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")
    while True:
        try:
            choice = int(input("  Choose category (1-6): ").strip())
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            else:
                print(f"   Please enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("Please enter a valid number.")


def add_expense(expenses):
    print("\n" + "-"*40)
    print(" ADD NEW EXPENSE")
    print("-"*40)

    title = input("  Title: ").strip()
    while not title:
        print(" Title cannot be empty.")
        title = input("  Title: ").strip()

    amount = get_valid_amount()
    category = get_valid_category()
    expense_date = get_valid_date()

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": expense_date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print(f"\n Expense saved!")
    print(f"     {title} | OMR{amount} | {category} | {expense_date}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("  Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            print("\n [View Expenses - Coming Soon]")
        elif choice == "3":
            print("\n [Total Spending - Coming Soon]")
        elif choice == "4":
            print("\n Goodbye! Stay on budget!\n")
            break
        else:
            print("\n Invalid choice. Please enter 1 to 4.")


if __name__ == "__main__":
    main()