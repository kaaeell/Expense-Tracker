# Expense Tracker

A powerful command-line application to track, manage, and analyze your daily expenses with categories, budgeting, and reporting features.

## Features

- **Add Expense** - Record expenses with name, amount, and category selection
- **View Expenses** - Display all recorded expenses with timestamps and categories
- **Delete Expense** - Remove individual expenses from your history
- **Search Expenses** - Find expenses by keyword (NEW!)
- **Spending by Category** - View expense breakdown across categories (NEW!)
- **Monthly Report** - Analyze spending trends by month (NEW!)
- **Set Budget Limit** - Define a monthly budget limit to track spending
- **Check Budget** - View current spending against your budget with warnings
- **Clear Expenses** - Delete all expenses at once
- **Input Validation** - Validates expense names and amounts
- **JSON Storage** - Saves expenses with full details including dates and categories

## Requirements

- Python 3.x

## Installation

No external dependencies required. Just clone or download the project and run:

```bash
python main.py
```

## Usage

Run the program:
```bash
python main.py
```

### Menu Options

1. **Add Expense** - Enter the expense name, select a category, and enter the amount
2. **View Expenses** - Display all recorded expenses with timestamps and categories
3. **Delete an Expense** - Select and remove a specific expense from your list
4. **Check Budget** - View your spending against the monthly budget limit with warnings
5. **Set Budget Limit** - Set a monthly budget and get alerts when approaching or exceeding it
6. **Search Expenses** - Find expenses by keyword (NEW!)
7. **Spending by Category** - See how much you've spent in each category (NEW!)
8. **Monthly Report** - View your spending trends by month (NEW!)
9. **Clear All Expenses** - Delete all expenses (confirmation required)
10. **Exit** - Close the application

## Categories

Pre-defined expense categories:
- Food
- Transportation
- Entertainment
- Utilities
- Healthcare
- Shopping
- Other

## Example

```
=== Expense Tracker ===
Welcome to your expense tracker app!

What would you like to do?
1. Add expense
2. View expenses
3. Delete an expense
4. Check budget
5. Set budget limit
6. Search expenses
7. Spending by category
8. Monthly report
9. Clear all expenses
10. Exit
Enter your choice (1-10): 1
Enter expense name: Grocery Shopping
Select a category:
1. Food
2. Transportation
3. Entertainment
4. Utilities
5. Healthcare
6. Shopping
7. Other
Enter category number: 1
Enter expense amount: $50.25
Expense 'Grocery Shopping' ($50.25) added to Food!
```

## Data Storage

Expenses are stored in `expenses.json` in JSON format with full details:
```json
[
  {
    "name": "Grocery Shopping",
    "amount": 50.25,
    "category": "Food",
    "date": "2026-02-08 14:30:45"
  }
]
```

Budget settings are stored in `budget.json` with your monthly limit.

## Features in Detail

### Search Expenses
Quickly find specific expenses by entering a keyword. The search is case-insensitive and searches across expense names.

### Spending by Category
See a breakdown of your total spending in each category. This helps you identify which categories consume the most money.

### Monthly Report
Analyze your spending trends across different months to see if your expenses are increasing or decreasing over time.

### Budget Tracking

- Set your monthly budget limit to track spending
- When checking budget status, you'll see:
  - Your budget limit
  - Total amount spent
  - Remaining budget
  - Warnings if you exceed your budget or use 80% of it

## Notes

- Use "yes" to confirm clearing all expenses (case-insensitive)
- Amounts must be valid numbers and greater than 0
- Expense names cannot be empty
- Categories are pre-defined for consistency
- All timestamps are recorded automatically when expenses are added
- Budget limit must be greater than 0
