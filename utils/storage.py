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
            print("Warning: Could not read data file. Starting fresh.")
            return []


def save_expenses(expenses):
    """Save all expenses to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)