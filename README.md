# Expense Tracker

A simple command-line application to track and manage your daily expenses.

## Features

- **Add Expense** - Record new expenses with name and amount
- **View Expenses** - Display all recorded expenses with total calculation
- **Delete Expense** - Remove individual expenses from your history (NEW!)
- **Set Budget Limit** - Define a monthly budget limit to track spending (NEW!)
- **Check Budget** - View current spending against your budget with warnings (NEW!)
- **Clear Expenses** - Delete all expenses and remove the expenses file
- **Input Validation** - Validates expense names and amounts
- **File Storage** - Saves expenses to a local text file

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

1. **Add Expense** - Enter the expense name and amount to record a new expense
2. **View Expenses** - Display all recorded expenses with a running total
3. **Delete an Expense** - Select and remove a specific expense from your list (NEW!)
4. **Check Budget** - View your spending against the monthly budget limit with warnings (NEW!)
5. **Set Budget Limit** - Set a monthly budget and get alerts when approaching or exceeding it (NEW!)
6. **Clear All Expenses** - Delete all expenses (confirmation required)
7. **Exit** - Close the application

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
6. Clear all expenses
7. Exit
Enter your choice (1-7): 1
Enter expense name: Grocery
Enter expense amount: $50.25
Expense 'Grocery' added successfully!
```

## Data Storage

Expenses are stored in `expenses.txt` in the same directory as the script. Each line contains:
```
Expense Name: $Amount
```

Budget settings are stored in `budget.json` with the monthly limit you've set.

## Budget Tracking (NEW!)

- Set your monthly budget limit to track spending
- When viewing budget status, you'll see:
  - Your budget limit
  - Total amount spent
  - Remaining budget
  - Warnings if you exceed your budget or use 80% of it

## Notes

- Use "yes" to confirm clearing all expenses (case-insensitive)
- Amounts must be valid numbers and greater than 0
- Expense names cannot be empty
- Budget limit must be greater than 0
