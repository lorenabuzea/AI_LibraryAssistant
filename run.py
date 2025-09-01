from app.chatbot import chat


def main():
    print("📚 Welcome to Smart Librarian!")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        response = chat(user_input)
        print(f"\n🤖 Librarian: {response}")

if __name__ == "__main__":
    #print(chat_debug("I want to read about a teen love story"))
    main()
