from sql_connect import get_connection

conn = get_connection()
cursor = conn.cursor()
        
def add_expense(name, category, date, amount):
        expense_name = name.strip()
        category = category.strip()
        amount = amount
        cursor.execute("""
        INSERT INTO Expenses (ExpenseName, Category, ExpenseDate, Amount)
        VALUES (?, ?, ?, ?)
        """, expense_name, category, date, amount)
        conn.commit()

def view_expenses():
    cursor.execute("SELECT * FROM Expenses")
    rows = cursor.fetchall()
    return rows

def remove_expense(ID):
    cursor.execute("DELETE FROM Expenses WHERE ID = ?", ID)
    print("The expense has been deleted!")
    conn.commit()

def get_expense(ID):
    cursor.execute("SELECT  * FROM Expenses WHERE ID = ?", ID)
    expense = cursor.fetchone()
    return expense

def update_expense(id, name, category, date, amount):
     cursor.execute("UPDATE Expenses SET ExpenseName = ?,Category = ?,ExpenseDate = ?,Amount = ? WHERE ID = ?;", name, category, date, amount, id)
     conn.commit()

def summarized_expenses(category):
    total = cursor.execute("SELECT SUM(Amount) FROM Expenses WHERE Category = '(?)' ", category)
    print(f"The total summarized amount for the expense category: '{category}' is: ", total)


def main() ->None:
    ...

if __name__ == "__main__":
    main()
