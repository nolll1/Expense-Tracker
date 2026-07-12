CREATE TABLE Expenses (
    Id INT IDENTITY(1,1) PRIMARY KEY,
	ExpenseName VARCHAR(50),
    Category VARCHAR(50),
    ExpenseDate DATE,
    Amount FLOAT
);