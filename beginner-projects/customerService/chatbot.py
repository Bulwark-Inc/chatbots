from utils import match_input, responses, transitions
import datetime

# Function to log the conversation
def log_conversation(user_input, bot_response):
    with open("conversation_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - User: {user_input}\n")
        file.write(f"{timestamp} - Bot: {bot_response}\n\n")

# Main function to handle conversation
def handle_conversation():
    state = "greeting"  # Initial state
    print(responses[state])  # Output greeting
    log_conversation("System", responses[state])  # Log greeting

    while True:
        user_input = input("You: ").lower().strip()

        if not user_input:
            bot_response = "Bot: Please enter a valid question or command."
            print(bot_response)
            log_conversation(user_input, bot_response)  # Log empty input case
            continue

        # Determine the next state based on user input
        state = match_input(user_input)
        
        # Ensure state transitions are valid
        if state not in transitions[state]:
            state = "fallback"
        
        bot_response = responses[state]
        print(f"Bot: {bot_response}")
        log_conversation(user_input, bot_response)  # Log conversation

        if state == "exit":
            break  # End conversation

# Run the chatbot
if __name__ == "__main__":
    handle_conversation()
