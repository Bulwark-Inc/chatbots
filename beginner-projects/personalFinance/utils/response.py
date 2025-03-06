from .input_parser import InputParser
from .expense_manager import ExpenseManager

class Chatbot:
    def __init__(self):
        """Initialize the chatbot with input parser and expense manager."""
        self.parser = InputParser()
        self.expense_manager = ExpenseManager()
    
    def handle_input(self, user_input):
        """Process user input and determine the action to take."""
        if "summary" in user_input.lower():
            return self.show_summary()
        elif "spent" in user_input.lower() or any(cat in user_input.lower() for cat in self.parser.categories):
            return self.record_expense(user_input)
        elif "category" in user_input.lower():
            return self.show_category_summary(user_input)
        else:
            return "I didn't understand that. You can record expenses or request a summary."
    
    def record_expense(self, user_input):
        """Extracts details and records an expense."""
        date, category, amount, description = self.parser.parse_input(user_input)
        if amount == 0:
            return "I couldn't detect an amount. Please specify how much you spent."
        
        self.expense_manager.record_expense(date, category, amount, description)
        return f"Recorded: {category} - ${amount:.2f} on {date}."
    
    def show_summary(self):
        """Fetches and returns a summary of all expenses."""
        return self.expense_manager.get_expense_summary()
    
    def show_category_summary(self, user_input):
        """Fetches and returns expenses for a specific category."""
        for category in self.parser.categories:
            if category in user_input.lower():
                return self.expense_manager.get_category_summary(category)
        return "Please specify a valid category."
