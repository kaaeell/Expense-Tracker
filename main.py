import os


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
        print("3. Clear all expenses")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            clear_expenses()
        elif choice == "4":
            print("Thanks for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()

