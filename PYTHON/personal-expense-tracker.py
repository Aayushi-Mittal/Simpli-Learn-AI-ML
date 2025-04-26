import csv
from datetime import datetime

# Initialize global variables
expenses = []
monthly_budget = 0.0

def add_expense():
    """Function to add an expense."""
    try:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        # Validate date format
        datetime.strptime(date, "%Y-%m-%d")
        category = input("Enter the category of the expense (e.g., Food, Travel): ")
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description of the expense: ")
        
        expenses.append({
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        })
        print("Expense added successfully!\n")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid data.\n")

def view_expenses():
    """Function to display all expenses."""
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\nYour Expenses:")
    for expense in expenses:
        if all(key in expense for key in ['date', 'category', 'amount', 'description']):
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
        else:
            print("Incomplete expense entry detected and skipped.")
    print()

def set_budget():
    """Function to set and track the budget."""
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print("Monthly budget set successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")

def track_budget():
    """Function to calculate total expenses and compare against the budget."""
    total_expenses = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal expenses so far: {total_expenses}")
    if monthly_budget > 0:
        if total_expenses > monthly_budget:
            print("Warning: You have exceeded your budget!\n")
        else:
            print(f"You have {monthly_budget - total_expenses} left for the month.\n")
    else:
        print("No budget set yet. Please set a budget to track your spending.\n")

def save_expenses():
    """Function to save expenses to a CSV file."""
    try:
        with open("expenses.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)
        print("Expenses saved successfully to expenses.csv!\n")
    except Exception as e:
        print(f"Error saving expenses: {e}\n")

def load_expenses():
    """Function to load expenses from a CSV file."""
    try:
        with open4("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])  # Convert amount to float
                expenses.append(row)
        print("Expenses loaded successfully from expenses.csv!\n")
    except FileNotFoundError:
        print("No saved expenses found. Starting fresh.\n")
    except Exception as e:
        print(f"Error loading expenses: {e}\n")

def menu():
    """Function to display the interactive menu."""
    while True:
        print("Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            track_budget()
        elif choice == "5":
            save_expenses()
        elif choice == "6":
            save_expenses()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Load existing expenses (if any) and start the program
load_expenses()
menu()
