print("Type 'quit' or 'exit' or 'bye' to leave the chat.")

while True:
    message = input("You: ")
    if message.lower() in ["quit", "exit" , "bye"]:
        print("Bot: Goodbye!")
        break
    
    print("Bot:" ,message)
