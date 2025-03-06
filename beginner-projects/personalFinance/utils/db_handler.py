import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="database/expenses.db"):
        """Initialize the database and create the expenses table if it doesn't exist."""
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Creates the expenses table if it doesn't already exist."""
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        );
        """
        self._execute_query(query)
    
    def _execute_query(self, query, params=()):
        """Executes a query with optional parameters."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def add_expense(self, date, category, amount, description=""):
        """Inserts a new expense record."""
        query = "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)"
        self._execute_query(query, (date, category, amount, description))
    
    def get_all_expenses(self):
        """Retrieves all expense records."""
        query = "SELECT * FROM expenses"
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
    
    def get_expenses_by_category(self, category):
        """Retrieves expenses filtered by category."""
        query = "SELECT * FROM expenses WHERE category = ?"
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (category,))
            return cursor.fetchall()
    
    def get_total_spent(self):
        """Calculates the total amount spent."""
        query = "SELECT SUM(amount) FROM expenses"
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchone()[0] or 0.0
    
    def delete_expense(self, expense_id):
        """Deletes an expense by its ID."""
        query = "DELETE FROM expenses WHERE id = ?"
        self._execute_query(query, (expense_id,))
