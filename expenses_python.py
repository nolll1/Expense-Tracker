import re
from datetime import datetime
from sql_connect import get_connection

conn = get_connection()
cursor = conn.cursor()

def print_menu() -> None:
    print("=== Expense Tracker ===")
    print("1. Add a expense")
    print("2. View the expense list")
    print("3. Remove an expense")
    print("4. View the summarized expense")
    print("5. Update the expense from the list")
    print("6. Exit")

def get_choice() -> str:
    while True:
        choice = input("Enter your choice number: ").strip()
        valid_choices = ['1', '2', '3', '4', '5', '6']
        if choice not in valid_choices:
            print("\nEnter a number from 1-6 according to the menu\n")

        else:
            return choice    
        
def add_expense():
        expense_name = input("Enter the name of the expense: ").strip().capitalize()
        category = input("Enter expense category: ").strip().capitalize()
        if not category:
            print("Category cannot be empty.")
            return None
        
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_str == '':
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
                try:
                    datetime.strptime(date_str, "%Y-%m-%d")
                    date = date_str
                except ValueError:
                    print("Invalid calendar date.")
                    return None
            else:
                print("Invalid format.")
                return None
        
        try:
            amount = int(input("Enter amount spent in Nrs: ").strip())
            if amount <= 0:
                print("Amount must be greater than 0.")
                return None
        except ValueError:
            print("Amount must be an integer.")
            return None
        
        cursor.execute("""
        INSERT INTO Expenses (ExpenseName, Category, ExpenseDate, Amount)
        VALUES (?, ?, ?, ?)
        """, expense_name, category, date, amount)

        conn.commit()

def view_expenses():
    cursor.execute("SELECT * FROM Expenses")
    rows = cursor.fetchall()
    print(f"{'ID':<5} {'Expense Name':<20} {'Category':<20} {'Date':<20} {'Amount':<20}\n")
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<20}\n")

def remove_expense():
    while True:
        try:
            ID = int(input("Enter the ID of the expense you want to remove: "))
            cursor.execute("DELETE FROM Expenses WHERE ID=(?)", ID)
            print("The expense has been deleted!")
            break
        except ValueError:
            print("The ID number must be an integer!")

def update_expense():
    try:
        choice = int(input("Enter the ID of the expense you want to edit: "))
    except ValueError:
        print("The ID must be an integer!")
        return
    cursor.execute("SELECT  * FROM Expenses WHERE ID = ?", choice)
    row = cursor.fetchone()
    if row is not None:
        print(f"{'ID':<5} {'Expense Name':<20} {'Category':<20} {'Date':<20} {'Amount':<20}\n")
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<20}\n")
    else:
        print(f"the expense with the ID: {choice} doesn't exist")
        return

    print("Enter new data or just press 'enter' for those you dont want to change")

    print(f"Current Expense Name: {row[1]}")
    name = input("New Expense Name(press Enter to keep): ").strip()
    if not name: 
        name = row[1]

    print(f"Current Category: {row[2]}")
    category = input("New Category(press Enter to keep): ").strip()
    if not category: 
        category = row[2]

    while True:
        print(f"Current Expense Date: {row[3]}")
        date = input("New Expense Date(press Enter to keep): ").strip()
        if not date: 
            date = row[3]
            break
        else:
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid calendar date.")
            else:
                print("Invalid format.")

    print(f"Current Amount: {row[4]}")
    while True:
        try:
            amt = input("New amount(press Enter to keep): ").strip()
            
            if not amt:
                amount = row[4]
                break
            else:
                amount = int(amt)
                if amount <= 0:
                    print("Amount must be greater than 0.")
                else:
                    break
        except ValueError:
            print("Amount must be an integer.")
    
    cursor.execute("UPDATE Expenses SET ExpenseName = ?,Category = ?,ExpenseDate = ?,Amount = ? WHERE ID = ?;", name, category, date, amount, choice)
    conn.commit()
    print("Expense updated successfully!")
     
def summarized_expenses():
    category = input("Enter the category for which you want a summarized amount of expenses: ").strip()
    cursor.execute("SELECT * FROM Expenses WHERE Category = ? ", category)
    rows = cursor.fetchall()
    if not rows:
        print("No such category")
        return
    else:
        print(f"===== CATEGORY : {category.upper()} =====")
        print(f"{'ID':<5} {'Expense Name':<20} {'Category':<20} {'Date':<20} {'Amount':<20}\n")
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<20} {row[3]:<20} {row[4]:<20}\n")
        cursor.execute("SELECT SUM(Amount) FROM Expenses WHERE Category = ? ", category)
        total = cursor.fetchone()
        print(f"The total summarized amount for the expense category: '{category}' is: ", total[0])

def main() ->None:
    while True:
        print_menu()

        choice = get_choice()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            remove_expense()
        elif choice == '4':
            summarized_expenses()
        elif choice == '5':
            update_expense()
        else:
            print("Goodbye!")
            conn.close()
            break

if __name__ == "__main__":
    main()
