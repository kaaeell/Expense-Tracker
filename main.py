import os
import json
from datetime import datetime


BUDGET_FILE = "budget.json"


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
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
        
        total = 0
        for expense in expenses:
            try:
                amount = float(expense.split("$")[1])
                total += amount
            except (IndexError, ValueError):
                pass
        
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
    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def delete_expense():
    """Delete a specific expense by number."""
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
        
        if not expenses:
            print("No expenses to delete.\n")
            return
        
        print("\n--- Your Expenses ---")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. {expense.strip()}")
        print()
        
        try:
            choice = int(input("Enter the expense number to delete (0 to cancel): "))
            if choice == 0:
                print("Delete cancelled.\n")
                return
            if 1 <= choice <= len(expenses):
                deleted = expenses.pop(choice - 1)
                with open("expenses.txt", "w") as file:
                    file.writelines(expenses)
                print(f"Deleted: {deleted.strip()}\n")
            else:
                print("Invalid expense number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def add_expense():
    """Add a new expense to the tracker."""
    expense_name = input("Enter expense name: ").strip()
    
    if not expense_name:
        print("Expense name cannot be empty.\n")
        return
    
    while True:
        try:
            expense_amount = float(input("Enter expense amount: $"))
            if expense_amount <= 0:
                print("Amount must be greater than 0.\n")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.\n")
    
    with open("expenses.txt", "a") as file:
        file.write(f"{expense_name}: ${expense_amount:.2f}\n")
    
    print(f"Expense '{expense_name}' added successfully!\n")


def view_expenses():
    """Display all recorded expenses."""
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
        
        if expenses:
            print("\n--- Your Expenses ---")
            total = 0
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. {expense.strip()}")
                # Extract amount for total calculation
                try:
                    amount = float(expense.split("$")[1])
                    total += amount
                except (IndexError, ValueError):
                    pass
            print(f"Total: ${total:.2f}")
            print()
        else:
            print("No expenses recorded yet.\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def clear_expenses():
    """Clear all recorded expenses after confirmation."""
    confirm = input("Are you sure you want to delete ALL expenses? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        try:
            os.remove("expenses.txt")
            print("All expenses have been cleared and file deleted!\n")
        except FileNotFoundError:
            print("No expenses file to delete.\n")
    else:
        print("Clear operation cancelled.\n")


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
        print("6. Clear all expenses")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()
        
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
            clear_expenses()
        elif choice == "7":
            print("Thanks for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-7.\n")


if __name__ == "__main__":
    main()
