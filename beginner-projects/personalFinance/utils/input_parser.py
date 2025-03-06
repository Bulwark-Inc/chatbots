import re
from datetime import datetime, timedelta

class InputParser:
    def __init__(self):
        """Initialize predefined expense categories."""
        self.categories = ["food", "transport", "entertainment", "rent", "shopping", "utilities", "health"]
    
    def parse_input(self, user_input):
        """Extracts date, category, amount, and description from user input."""
        date = self.extract_date(user_input)
        amount = self.extract_amount(user_input)
        category = self.extract_category(user_input)
        
        # Use remaining input as description
        description = user_input
        for item in [str(amount), category]:
            if item:
                description = description.replace(item, "").strip()
        
        return date, category, amount, description
    
    def extract_date(self, text):
        """Extracts date from input (supports 'today', 'yesterday', and specific dates)."""
        text = text.lower()
        if "yesterday" in text:
            return (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        elif "today" in text:
            return datetime.today().strftime("%Y-%m-%d")
        
        date_match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", text)
        return date_match.group(1) if date_match else datetime.today().strftime("%Y-%m-%d")
    
    def extract_amount(self, text):
        """Extracts numeric amount from input."""
        match = re.search(r"(\d+\.?\d*)", text)
        return float(match.group(1)) if match else 0.0
    
    def extract_category(self, text):
        """Finds the closest matching category in the input text."""
        for category in self.categories:
            if category in text.lower():
                return category
        return "other"
