def chatbot():
    print("===================================")
    print("       BASIC CHATBOT")
    print("===================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I am a Python Chatbot.")

        elif user_input == "who created you":
            print("Bot: I was created using Python.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()