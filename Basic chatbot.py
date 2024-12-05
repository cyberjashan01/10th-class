# Simple Chatbot Program

def chatbot_response(user_input):
    # Define some basic responses
    responses = {
        "hello": "Hello! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a chatbot created by a Python script.",
        "bye": "Goodbye! Have a great day!"
    }

    # Convert user input to lowercase to make the bot case insensitive
    user_input = user_input.lower()

    # Find the appropriate response or default to a generic response
    return responses.get(user_input, "I'm not sure how to respond to that.")

def main():
    print("Welcome to the simple chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
