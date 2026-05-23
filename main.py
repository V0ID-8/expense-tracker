from datetime import date
from utils.storage import (
    load_expenses,
    save_expenses,
    get_total,
    get_category_totals,
    get_monthly_totals
)

CATEGORIES = ["Food", "Transport", "Shopping", "Health", "Bills", "Other"]


def show_menu():
    print("\n" + "="*40)
    print("       EXPENSE TRACKER")
    print("="*40)
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. View Total Spending")
    print("  4. Filter by Category")
    print("  5. View Monthly Summary")
    print("  6. Exit")
    print("="*40)


def get_valid_amount():
    """Prompt user for a valid positive number."""
    while True:
        try:
            amount = float(input("  Amount ($): ").strip())
            if amount <= 0:
                print("  Warning: Amount must be greater than 0.")
            else:
                return round(amount, 2)
        except ValueError:
            print("  Warning: Please enter a valid number.")


def get_valid_date():
    """Prompt user for a valid date or default to today."""
    while True:
        date_input = input("  Date (YYYY-MM-DD) [press Enter for today]: ").strip()
        if date_input == "":
            return str(date.today())
        try:
            date.fromisoformat(date_input)
            return date_input
        except ValueError:
            print("  Warning: Invalid date format. Use YYYY-MM-DD.")


def get_valid_category():
    """Prompt user to select a category from the list."""
    print("  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")
    while True:
        try:
            choice = int(input(f"  Choose category (1-{len(CATEGORIES)}): ").strip())
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            else:
                print(f"  Warning: Please enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("  Warning: Please enter a valid number.")


def add_expense(expenses):
    """Collect expense details from user and save."""
    print("\n" + "-"*40)
    print("  ADD NEW EXPENSE")
    print("-"*40)

    title = input("  Title: ").strip()
    while not title:
        print("  Warning: Title cannot be empty.")
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

    print(f"\n  Expense saved: {title} | ${amount} | {category} | {expense_date}")


def view_expenses(expenses):
    """Display all stored expenses in a readable format."""
    print("\n" + "-"*40)
    print("  ALL EXPENSES")
    print("-"*40)

    if not expenses:
        print("  No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, 1):
        print(f"  {i}. {expense['date']} | {expense['category']:<12} | ${expense['amount']:<8} | {expense['title']}")

    print("-"*40)
    print(f"  Total records: {len(expenses)}")


def view_total(expenses):
    """Display total spending broken down by category."""
    print("\n" + "-"*40)
    print("  TOTAL SPENDING")
    print("-"*40)

    if not expenses:
        print("  No expenses recorded yet.")
        return

    category_totals = get_category_totals(expenses)
    total = get_total(expenses)

    print(f"  {'Category':<15} {'Total':>10}")
    print("  " + "-"*25)
    for cat, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<15} ${amount:>9.2f}")

    print("  " + "="*25)
    print(f"  {'GRAND TOTAL':<15} ${total:>9.2f}")


def filter_by_category(expenses):
    """Display expenses filtered by a selected category."""
    print("\n" + "-"*40)
    print("  FILTER BY CATEGORY")
    print("-"*40)

    if not expenses:
        print("  No expenses recorded yet.")
        return

    selected = get_valid_category()
    filtered = [e for e in expenses if e["category"] == selected]

    print(f"\n  Expenses in '{selected}':")
    print("  " + "-"*36)

    if not filtered:
        print("  No expenses found in this category.")
        return

    for i, expense in enumerate(filtered, 1):
        print(f"  {i}. {expense['date']} | ${expense['amount']:<8} | {expense['title']}")

    print("  " + "-"*36)
    print(f"  Category total: ${sum(e['amount'] for e in filtered):.2f}")


def view_monthly_summary(expenses):
    """Display total spending grouped by month."""
    print("\n" + "-"*40)
    print("  MONTHLY SUMMARY")
    print("-"*40)

    if not expenses:
        print("  No expenses recorded yet.")
        return

    monthly = get_monthly_totals(expenses)

    print(f"  {'Month':<12} {'Total':>10}")
    print("  " + "-"*22)
    for month in sorted(monthly.keys(), reverse=True):
        print(f"  {month:<12} ${monthly[month]:>9.2f}")


def main():
    """Main entry point — load data and run the menu loop."""
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            filter_by_category(expenses)
        elif choice == "5":
            view_monthly_summary(expenses)
        elif choice == "6":
            print("\n  Goodbye! Stay on budget!\n")
            break
        else:
            print("\n  Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main() 