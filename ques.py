from datetime import datetime

# Global variable to store expenses
expenses = []

# Function to initialize the text file
def initialize_text_file(filename):
    with open(filename, "w") as file:
        file.write("Date | Amount | Category | Description\n")

# Function to load expenses from the text file
def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip the header line
                date, amount, category, description = map(str.strip, line.split('|'))
                expenses.append({
                    "date": date,
                    "amount": float(amount),
                    "category": category,
                    "description": description
                })
    except FileNotFoundError:
        print(f"Expense file '{filename}' not found. Creating a new one.")
        initialize_text_file(filename)

# Function to save expenses to the text file
def save_expenses():
    filename = input("Enter the filename for saving expenses (e.g., expenses.txt): ")
    with open(filename, "w") as file:
        file.write("Date | Amount | Category | Description\n")
        for expense in expenses:
            file.write(f"{expense['date']} | {expense['amount']} | {expense['category']} | {expense['description']}\n")
    print(f"Expenses saved successfully to '{filename}'!")

# Function to add a new expense
def add_expense(amount, category, description):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expenses.append({"date": date, "amount": amount, "category": category, "description": description})
    print("Expense added successfully!")

# Function to display all expenses
def display_expenses():
    print("\nExpense List:")
    print("Date | Amount | Category | Description")
    print("-------------------------------------")
    for expense in expenses:
        print(f"{expense['date']} | {expense['amount']} | {expense['category']} | {expense['description']}")

# Function to get user input and add a new expense
def get_user_input():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break  # Break out of the loop if the input is a valid float
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")

    category = input("Enter the category: ")
    description = input("Enter the description (optional): ")

    add_expense(amount, category, description)

# Main function
def main():

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Save Expenses to Text File")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            get_user_input()
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            save_expenses()
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()

# https://docs.google.com/document/d/1dArBRZ3YGYRnhSnG7IuuzuyGR7I7CNjjAhRVh9gIszc/edit?usp=sharing