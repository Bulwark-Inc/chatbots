from utils.response import Chatbot

def main():
    chatbot = Chatbot()
    print("Welcome to the Personal Finance Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        
        response = chatbot.handle_input(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()