from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

def get_connection():
    return pyodbc.connect(
        driver=os.getenv("DB_DRIVER"),
        server=os.getenv("DB_SERVER"),
        database=os.getenv("DB_DATABASE"),
        trusted=os.getenv("DB_TRUSTED_CONNECTION")
    )

# "DRIVER={SQL Server};"
# "SERVER=LAPTOP-4DFHA4UG\SQLEXPRESS;"
# "DATABASE=ExpenseDB;"
# "Trusted_Connection=yes;"