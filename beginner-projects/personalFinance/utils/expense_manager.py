from utils.db_handler import DatabaseManager

class ExpenseManager:
    def __init__(self):
        """Initialize the ExpenseManager with a DatabaseManager instance."""
        self.db = DatabaseManager()

    def record_expense(self, date, category, amount, description=""):
        """Records an expense by interacting with the DatabaseManager."""
        self.db.add_expense(date, category, amount, description)

    def get_expense_summary(self):
        """Returns a summary of total spending and spending by category."""
        total_spent = self.db.get_total_spent()
        categories = {}
        
        expenses = self.db.get_all_expenses()
        for expense in expenses:
            category = expense[2]  # Category is the third column
            amount = expense[3]  # Amount is the fourth column
            categories[category] = categories.get(category, 0) + amount
        
        summary = f"Total spent: ${total_spent:.2f}\n"
        for cat, amt in categories.items():
            summary += f"- {cat}: ${amt:.2f}\n"
        
        return summary
    
    def get_category_summary(self, category):
        """Returns a formatted list of expenses for a specific category."""
        expenses = self.db.get_expenses_by_category(category)
        if not expenses:
            return f"No expenses found for category: {category}"
        
        summary = f"Expenses for {category}:\n"
        for expense in expenses:
            date, amount, description = expense[1], expense[3], expense[4]
            summary += f"- {date}: ${amount:.2f} ({description})\n"
        
        return summary
