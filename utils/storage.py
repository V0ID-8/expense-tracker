import json
import os

DATA_FILE = "expenses.json"


def load_expenses():
    """Load all expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            print("  Warning: Could not read data file. Starting fresh.")
            return []


def save_expenses(expenses):
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def get_total(expenses):
    """Return the sum of all expense amounts."""
    return round(sum(e["amount"] for e in expenses), 2)


def get_category_totals(expenses):
    """Return a dict of category -> total amount."""
    totals = {}
    for expense in expenses:
        cat = expense["category"]
        totals[cat] = round(totals.get(cat, 0) + expense["amount"], 2)
    return totals


def get_monthly_totals(expenses):
    """Return a dict of YYYY-MM -> total amount."""
    monthly = {}
    for expense in expenses:
        month = expense["date"][:7]
        monthly[month] = round(monthly.get(month, 0) + expense["amount"], 2)
    return monthly