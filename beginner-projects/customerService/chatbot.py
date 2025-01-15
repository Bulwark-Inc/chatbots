from utils import match_input, responses, transitions

# Main function to handle conversation
def handle_conversation():
    state = "greeting"  # Initial state
    print(responses[state])  # Output greeting

    while True:
        user_input = input("You: ").lower().strip()

        if not user_input:
            print("Bot: Please enter a valid question or command.")
            continue

        # Determine the next state based on user input
        state = match_input(user_input)
        
        # Ensure state transitions are valid
        if state not in transitions[state]:
            state = "fallback"
        
        print(f"Bot: {responses[state]}")

        if state == "exit":
            break  # End conversation

# Run the chatbot
if __name__ == "__main__":
    handle_conversation()
