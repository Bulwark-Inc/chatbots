# chatbot.py

# Define chatbot responses for each state
responses = {
    "greeting": "Hello! Welcome to [Business Name]. How can I assist you today?",
    "working_hours": "We are open Monday to Friday, 9 AM to 5 PM.",
    "services": "We provide X, Y, and Z services. Would you like more details?",
    "fallback": "I'm sorry, I didn't understand that. Can you please rephrase?",
    "exit": "Thank you for chatting with us! Have a great day."
}

# Define the transitions between states
transitions = {
    "greeting": ["working_hours", "services", "exit"],
    "working_hours": ["greeting", "exit"],
    "services": ["greeting", "exit"],
    "fallback": ["greeting", "exit"],
    "exit": []
}

# Main function to handle conversation
def handle_conversation():
    state = "greeting"  # Initial state
    print(responses[state])  # Output greeting

    while True:
        user_input = input("You: ").lower()

        if "working hours" in user_input:
            state = "working_hours"
        elif "services" in user_input:
            state = "services"
        elif "exit" in user_input:
            state = "exit"
        else:
            state = "fallback"

        print(f"Bot: {responses[state]}")

        if state == "exit":
            break  # End conversation

# Run the chatbot
if __name__ == "__main__":
    handle_conversation()
