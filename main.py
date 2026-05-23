from datetime import date
from utils.storage import load_expenses, save_expenses


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
    while True:
        try:
            amount = float(input("  Amount (OMR): ").strip())
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
    print(f"     {title} | OMR{ amount} | {category} | {expense_date}")


def view_expenses(expenses):
    print("\n" + "-"*40)
    print(" VIEW ALL EXPENSES")
    print("-"*40)
    
    if not expenses:
        print(" No expenses to display.")
        return
        
    for i, expense in enumerate(expenses, 1):
        print(f"  {i}. {expense['date']} | {expense['category']:<12} | OMR{expense['amount']:<8} | {expense['title']}")

    print("-"*40)
    print(f" total records: {len(expenses)}")
        

def view_total(expenses):
    print("\n" + "-"*40)
    print(" TOTAL SPENDING")
    print("-"*40)
    
    if not expenses:
        print(" No expenses recorded yet.")
        return
    
    total = sum(expense["amount"] for expense in expenses)
    
    category_totals = {}
    for expense in expenses:
        cat = expense["category"]
        category_totals[cat] = category_totals.get(cat, 0) + expense["amount"]

    print(f"    {'category':<15}  {'total (OMR)':>10}")
    print("  " + "-"*25)
    for cat, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"    {cat:<15}  OMR{amount:>9.2f}")

    print("  " + "="*25)
    print(f"    {'TOTAL':<15}  OMR{total:>9.2f}")


def filter_by_category(expenses):
    print("\n" + "-"*40)
    print(" FILTER BY CATEGORY")
    print("-"*40)
    
    if not expenses:
        print(" No expenses recorded yet.")
        return
    
    print("  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")

    while True:
        try:
            choice = int(input("  Choose category to filter (1-6): ").strip())
            if 1 <= choice <= len(CATEGORIES):
                selected = CATEGORIES[choice - 1]
                break
            else:
                print(f"   Please enter a number between 1 and {len(CATEGORIES)}.")    
        except ValueError:
            print(" WARNING: Please enter a valid number.")

    filtered = [e for e in expenses if e["category"] == selected]

    print(f"\n Expenses in '{selected}':")
    print("  " + "-"*36)

    if not filtered:
        print(f"  No expenses found in '{selected}'.")
    else:
        for i, expense in enumerate(filtered, 1):
            print(f"   {i}. {expense['date']} | OMR{expense['amount']:<8.2f} | {expense['title']}")
        print("  " + "-"*36)
        print(f"   Category total: OMR{sum(e['amount'] for e in filtered):.2f}")


def view_monthly_summary(expenses):
    print("\n" + "-"*40)
    print(" MONTHLY SUMMARY")
    print("-"*40)
    
    if not expenses:
        print(" No expenses recorded yet.")
        return
    
    monthly = {}
    for expense in expenses:
        month = expense["date"][:7]  # YYYY-MM
        monthly[month] = monthly.get(month, 0) + expense["amount"]

    print(f"    {'month':<12}  {'total (OMR)':>10}")
    print("  " + "-"*25)
    for month in sorted(monthly.keys(), reverse=True):
        print(f"    {month:<12}  OMR{monthly[month]:>9.2f}")

def main():
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
            print("\n Exiting... Goodbye!")
            break 
        else:
            print("\n Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()