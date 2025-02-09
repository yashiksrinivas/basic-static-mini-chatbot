
import nltk
import spacy
from tkinter import *
from nltk.chat.util import Chat, reflections

# Download NLTK resources
nltk.download('punkt')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define pairs for NLTK Chat
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?"]),
    (r"good morning",["good morning have a blessful and energitic day how are you doing"]),
    (r"good afternoon",["good afternoon hows your day going on "]),
    (r"good evening",["good eveing any plans for the evening or just a casual routine"]),
    (r"what is your name?", ["I am a chatbot created for demonstration purposes."]),
    (r"how are you?", ["I'm just a program, but I'm here to help you!"]),
    (r"i hope you are doing good", ["I'm doing great, thank you! How about you?"]),
    (r"i am doing good",["nice to know you are doing good,working on something intresting?"]),
    (r"quit", ["Goodbye! Have a great day!"]),
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to process user input using spaCy and NLTK
def process_input(user_input):
    doc = nlp(user_input)
    tokens = [token.text for token in doc]
    response = chatbot.respond(user_input.lower())
    if response:
        return response
    return "I didn't quite understand that. Could you rephrase?"

# GUI for the Chatbot
def chatbot_gui():
    def send_message():
        user_message = user_input.get()
        if user_message.lower() == "quit":
            chat_log.insert(END, "Chatbot: Goodbye!\n")
            root.quit()
            return

        # Display user message
        chat_log.insert(END, f"You: {user_message}\n")

        # Get chatbot response
        bot_response = process_input(user_message)
        chat_log.insert(END, f"Chatbot: {bot_response}\n")

        # Clear user input
        user_input.delete(0, END)

    # Initialize GUI window
    root = Tk()
    root.title("Chatbot")
    root.geometry("400x500")

    # Chat log display
    chat_log = Text(root, bd=1, bg="lightgray", font=("Arial", 12))
    chat_log.pack(pady=55, padx=10, fill=BOTH, expand=True)

    # User input field
    user_input = Entry(root, font=("Arial", 14))
    user_input.pack(pady=3, padx=5 , fill=X, side=LEFT, expand=True)

    # Send button
    send_button = Button(root, text="Send", font=("Arial", 12), command=send_message)
    send_button.pack(pady=10, padx=10, side=RIGHT)

    # Run the GUI loop
    root.mainloop()

# Start the chatbot GUI
chatbot_gui()
