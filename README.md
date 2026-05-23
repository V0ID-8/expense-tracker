# Expense Tracker

A command-line application built with Python to help you track daily expenses,
monitor spending by category, and review monthly summaries.

---

## Features

- Add expenses with title, amount, category, and date
- View all recorded expenses in a clean table format
- View total spending broken down by category
- Filter expenses by category
- View monthly spending summary
- Data persists between sessions using a local JSON file
- Input validation for all fields

---

## Technologies Used

- Python 3
- JSON (data storage)
- Git (version control)

---

## Project Structure

    expense-tracker/
    │
    ├── main.py              # Main application entry point and all UI logic
    ├── expenses.json        # Local data storage file
    ├── README.md            # Project documentation
    │
    └── utils/
        ├── __init__.py      # Makes utils a Python package
        └── storage.py       # All data handling functions

---

## How to Run

1. Make sure Python 3 is installed on your machine:

    python --version

2. Clone or download the project folder

3. Navigate into the project directory:

    cd expense-tracker

4. Run the application:

    python main.py

No external libraries required. Everything runs on the Python standard library.

---

## How to Use

    ========================================
           EXPENSE TRACKER
    ========================================
      1. Add Expense
      2. View All Expenses
      3. View Total Spending
      4. Filter by Category
      5. View Monthly Summary
      6. Exit
    ========================================

- Choose 1 to add a new expense and fill in the details
- Choose 2 to see all your recorded expenses
- Choose 3 to see total spending grouped by category
- Choose 4 to filter and view expenses from one category
- Choose 5 to see how much you spent each month
- Choose 6 to exit the application

Your data is automatically saved after every entry.

---

## Data Format

Expenses are stored in expenses.json as a list of objects:

    [
        {
            "title": "Lunch",
            "amount": 12.5,
            "category": "Food",
            "date": "2026-05-23"
        }
    ]

---

## Available Categories

- Food
- Transport
- Shopping
- Health
- Bills
- Other

---

## Future Improvements

- Budget limit warnings per category
- Delete or edit an existing expense
- Export data to CSV
- Data visualization using matplotlib
- Search expenses by keyword
- Weekly summary view

---

## Git History

- Commit 1 - Initial project setup with folder structure
- Commit 2 - Implemented CLI menu system
- Commit 3 - Added expense input functionality
- Commit 4 - Implemented JSON file storage system
- Commit 5 - Added view expenses feature
- Commit 6 - Implemented total expense calculation, category filter, and monthly summary
- Commit 7 - Final cleanup and bug fixes
- Commit 8 - Added professional README

---

## Author

Built as a Python CLI project following clean code and professional Git practices.