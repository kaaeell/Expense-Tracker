# Expense Tracker

A simple command-line application to track and manage your daily expenses.

## Features

- **Add Expense** - Record new expenses with name and amount
- **View Expenses** - Display all recorded expenses with total calculation
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
3. **Clear All Expenses** - Delete all expenses (confirmation required)
4. **Exit** - Close the application

## Example

```
=== Expense Tracker ===
Welcome to your expense tracker app!

What would you like to do?
1. Add expense
2. View expenses
3. Clear all expenses
4. Exit
Enter your choice (1-4): 1
Enter expense name: Grocery
Enter expense amount: $50.25
Expense 'Grocery' added successfully!
```

## Data Storage

Expenses are stored in `expenses.txt` in the same directory as the script. Each line contains:
```
Expense Name: $Amount
```

## Notes

- Use "yes" to confirm clearing all expenses (case-insensitive)
- Amounts must be valid numbers and greater than 0
- Expense names cannot be empty
