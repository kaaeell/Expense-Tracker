import os
import json
from datetime import datetime
from collections import defaultdict


BUDGET_FILE = "budget.json"
EXPENSES_FILE = "expenses.json"
CATEGORIES = ["Food", "Transportation", "Entertainment", "Utilities", "Healthcare", "Shopping", "Other"]


def load_budget():
    """Load budget settings from file."""
    try:
        with open(BUDGET_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"limit": None, "amount": 0}


def save_budget(budget):
    """Save budget settings to file."""
    with open(BUDGET_FILE, "w") as file:
        json.dump(budget, file)


def set_budget_limit():
    """Set a monthly budget limit."""
    try:
        limit = float(input("Enter your monthly budget limit ($): "))
        if limit <= 0:
            print("Budget must be greater than 0.\n")
            return
        budget = load_budget()
        budget["limit"] = limit
        save_budget(budget)
        print(f"Budget limit set to ${limit:.2f}!\n")
    except ValueError:
        print("Invalid amount. Please enter a valid number.\n")


def check_budget():
    """Check current spending against budget."""
    expenses = load_expenses()
    total = sum(expense['amount'] for expense in expenses)
    
    budget = load_budget()
    if budget["limit"]:
        print(f"\n--- Budget Status ---")
        print(f"Budget Limit: ${budget['limit']:.2f}")
        print(f"Total Spent: ${total:.2f}")
        remaining = budget["limit"] - total
        print(f"Remaining: ${remaining:.2f}")
        
        if total > budget["limit"]:
            print(f"⚠️  WARNING: You've exceeded your budget by ${total - budget['limit']:.2f}!")
        elif remaining < budget["limit"] * 0.2:  # 20% warning
            print(f"⚠️  WARNING: You've used 80% of your budget!")
        print()
    else:
        print("No budget limit set yet.\n")


def delete_expense():
    """Delete a specific expense by number."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses to delete.\n")
        return
    
    print("\n--- Your Expenses ---")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['name']}: ${expense['amount']:.2f} [{expense['category']}]")
    print()
    
    try:
        choice = int(input("Enter the expense number to delete (0 to cancel): "))
        if choice == 0:
            print("Delete cancelled.\n")
            return
        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"Deleted: {deleted['name']} (${deleted['amount']:.2f})\n")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def load_expenses():
    """Load expenses from JSON file."""
    try:
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    """Save expenses to JSON file."""
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=2)


def add_expense():
    """Add a new expense to the tracker with category."""
    expense_name = input("Enter expense name: ").strip()
    
    if not expense_name:
        print("Expense name cannot be empty.\n")
        return
    
    print("\nSelect a category:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            cat_choice = int(input("Enter category number: "))
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
                break
            else:
                print("Invalid category number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    
    while True:
        try:
            expense_amount = float(input("Enter expense amount: $"))
            if expense_amount <= 0:
                print("Amount must be greater than 0.\n")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.\n")
    
    expenses = load_expenses()
    expense_entry = {
        "name": expense_name,
        "amount": expense_amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense_entry)
    save_expenses(expenses)
    
    print(f"Expense '{expense_name}' (${expense_amount:.2f}) added to {category}!\n")


def view_expenses():
    """Display all recorded expenses."""
    expenses = load_expenses()
    
    if expenses:
        print("\n--- Your Expenses ---")
        total = 0
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense['name']}: ${expense['amount']:.2f} [{expense['category']}] - {expense['date']}")
            total += expense['amount']
        print(f"\nTotal: ${total:.2f}\n")
    else:
        print("No expenses recorded yet.\n")


def clear_expenses():
    """Clear all recorded expenses after confirmation."""
    confirm = input("Are you sure you want to delete ALL expenses? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        save_expenses([])
        print("All expenses have been cleared!\n")
    else:
        print("Clear operation cancelled.\n")


def search_expenses():
    """Search expenses by keyword."""
    keyword = input("Enter search keyword: ").strip().lower()
    expenses = load_expenses()
    
    results = [exp for exp in expenses if keyword in exp['name'].lower()]
    
    if results:
        print(f"\n--- Search Results for '{keyword}' ---")
        total = 0
        for i, expense in enumerate(results, 1):
            print(f"{i}. {expense['name']}: ${expense['amount']:.2f} [{expense['category']}] - {expense['date']}")
            total += expense['amount']
        print(f"Total: ${total:.2f}\n")
    else:
        print(f"No expenses found matching '{keyword}'.\n")


def spending_by_category():
    """Display spending breakdown by category."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense['category']] += expense['amount']
    
    print("\n--- Spending by Category ---")
    total = 0
    for category in CATEGORIES:
        amount = category_totals.get(category, 0)
        if amount > 0:
            print(f"{category}: ${amount:.2f}")
            total += amount
    print(f"Total: ${total:.2f}\n")


def monthly_report():
    """Display monthly spending summary."""
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    
    monthly_totals = defaultdict(float)
    for expense in expenses:
        # Extract month from date (YYYY-MM-DD format)
        month = expense['date'][:7]  # Gets YYYY-MM
        monthly_totals[month] += expense['amount']
    
    print("\n--- Monthly Report ---")
    for month in sorted(monthly_totals.keys()):
        print(f"{month}: ${monthly_totals[month]:.2f}")
    
    total_all = sum(monthly_totals.values())
    print(f"Grand Total: ${total_all:.2f}\n")


def main():
    """Main function to run the expense tracker."""
    print("\n=== Expense Tracker ===")
    print("Welcome to your expense tracker app!\n")
    
    while True:
        print("What would you like to do?")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete an expense")
        print("4. Check budget")
        print("5. Set budget limit")
        print("6. Search expenses")
        print("7. Spending by category")
        print("8. Monthly report")
        print("9. Clear all expenses")
        print("10. Exit")
        choice = input("Enter your choice (1-10): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            check_budget()
        elif choice == "5":
            set_budget_limit()
        elif choice == "6":
            search_expenses()
        elif choice == "7":
            spending_by_category()
        elif choice == "8":
            monthly_report()
        elif choice == "9":
            clear_expenses()
        elif choice == "10":
            print("Thanks for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-10.\n")


if __name__ == "__main__":
    main()
