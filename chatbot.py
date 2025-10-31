class ChatBot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "hello": "Hello! Nice to meet you",
            "hi": "Hi there!",
            "how are you": "I'm doing great! Thanks for asking",
            "your name": f"My name is {self.name}. I'm your assistant",
            "bye": "Goodbye! Have a great day"
        }

    def header(self):
        print("=" * 50)
        print(f"🤖 {self.name.upper()} CHATBOT".center(50))
        print("=" * 50)
        print("💬 Type something to chat. Type 'bye' to exit.")
        print("_" * 50)

    def respond(self, message):
        message = message.lower()

        for key in self.responses:
            if key in message:
                return self.responses[key]

        return "Hmm.... I don't understand that yet"


# main program
bot = ChatBot("Jervis")
bot.header()

while True:
    user_input = input("👤 You: ")
    reply = bot.respond(user_input)
    print(f"🤖 Bot: {reply}")
    print("-" * 50)

    if "bye" in user_input.lower():
        break
