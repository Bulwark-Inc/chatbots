import re

# Define chatbot responses for each state
responses = {
    "greeting": "Hello! Welcome to [Business Name]. How can I assist you today?",
    "working_hours": "We are open Monday to Friday, 9 AM to 5 PM.",
    "services": "We provide X, Y, and Z services. Would you like more details?",
    "location": "We are located at [Your Business Address]. Would you like directions?",
    "contact": "You can reach us at contact@[business].com or call us at [Phone Number].",
    "fallback": "I'm sorry, I didn't understand that. Can you please rephrase?",
    "exit": "Thank you for chatting with us! Have a great day!"
}

# Define the transitions between states
transitions = {
    "greeting": ["working_hours", "services", "location", "contact", "exit"],
    "working_hours": ["greeting", "exit"],
    "services": ["greeting", "exit"],
    "location": ["greeting", "exit"],
    "contact": ["greeting", "exit"],
    "fallback": ["greeting", "exit"],
    "exit": []
}

# Function to check user input with regex
def match_input(user_input):
    if re.search(r"(working|open|hours)", user_input):
        return "working_hours"
    elif re.search(r"(service|offer|products)", user_input):
        return "services"
    elif re.search(r"(location|address|where)", user_input):
        return "location"
    elif re.search(r"(contact|email|phone)", user_input):
        return "contact"
    elif re.search(r"(exit|bye|quit)", user_input):
        return "exit"
    else:
        return "fallback"
