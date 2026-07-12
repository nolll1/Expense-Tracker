# 💰 Expense Tracker

A Python-based Expense Tracker built to practice CRUD operations, SQL, and Flask web development. The project stores expenses in a SQL Server database and is available in both a command-line (CLI) version and a Flask web application.

## Features

* ➕ Add new expenses
* 📋 View all expenses
* ✏️ Edit existing expenses
* ❌ Delete expenses
* 📊 View summarized expenses by category (CLI version only)
* 🗄️ Store data in SQL Server using `pyodbc`
* 🌐 Web interface built with Flask
* 💻 Command-line version for practicing Python fundamentals

---

## Technologies Used

* Python
* Flask
* SQL Server
* pyodbc
* HTML
* CSS
* python-dotenv

---

## Project Structure

expense_tracker/
│
├── app.py                  # Flask application
├── expenses.py             # Database operations for Flask
├── expenses_python.py      # Command-line version
├── sql_connect.py          # Database connection
├── create_table.sql        # SQL script to create the database table
├── requirements.txt
├── .env                    # Local database configuration (not committed)
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
├── general.css
└── edit.css

---

## Database

The application uses SQL Server to store expenses.

Table structure:

| Column      | Type              |
| ----------- | ----------------- |
| ID          | INT (Primary Key) |
| ExpenseName | VARCHAR           |
| Category    | VARCHAR           |
| ExpenseDate | DATE              |
| Amount      | INT               |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/nolll1/Expense-Tracker.git
cd expense-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

macOS/Linux

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
DB_DRIVER=SQL Server
DB_SERVER=YOUR_SERVER\SQLEXPRESS
DB_DATABASE=ExpenseDB
DB_TRUSTED_CONNECTION=yes
```

### 5. Create the database

Run the SQL statements in `create_table.sql` using SQL Server Management Studio (SSMS).

---

## Running the Project

### Command-Line Version

```bash
python expenses_python.py
```

### Flask Web Version

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## What I Learned

This project helped me practice:

* CRUD operations with SQL Server
* Parameterized SQL queries
* Database design and SQL scripting
* Connecting Python to SQL Server using `pyodbc`
* Flask routing and form handling
* HTML forms and Jinja templates
* CRUD implementation in a web application
* Input validation and error handling
* Organizing a project into reusable modules

---

## Future Improvements

* Search expenses by date or category
* Monthly expense reports
* Charts and visualizations
* Expense categories with icons
* User authentication
* Pagination for large datasets


