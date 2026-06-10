import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random

# Response database for chatbot
responses = {

    "greetings": [
        "Hello! 👋 How can I help you today?",
        "Hi there! 😊",
        "Hey! Nice to meet you.",
        "Welcome! What can I do for you?"
    ],

    "how_are_you": [
        "I'm doing great! 😄",
        "Everything is working perfectly!",
        "I'm fine, thanks for asking.",
        "Feeling intelligent today! 🤖"
    ],

    "name": [
        "My name is AI ChatBot.",
        "I am an AI Assistant built using Python.",
        "You can call me ChatBot."
    ],

    "creator": [
        "I was created using Python and Tkinter.",
        "A talented developer built me. 😎",
        "I am powered by Python."
    ],

    "help": [
        """
Available Commands

• hello
• how are you
• your name
• who made you
• time
• date
• calculate 10+20
• joke
• motivate me
• quote
• fact
• thanks
• bye
"""
    ],

    "jokes": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
        "Python programmers don't byte, they hiss. 🐍",
        "Why was the computer cold? It left its Windows open! 😆"
    ],

    "motivation": [
        "Success comes from consistency, not perfection.",
        "Every expert was once a beginner.",
        "Keep learning and keep growing. 🚀",
        "Small progress is still progress."
    ],

    "quotes": [
        "The future depends on what you do today. – Gandhi",
        "Dream big and dare to fail.",
        "Knowledge is power.",
        "Never stop learning."
    ],

    "facts": [
        "Python was created by Guido van Rossum in 1991.",
        "The first computer bug was an actual moth.",
        "Artificial Intelligence is one of the fastest-growing fields.",
        "The first website went online in 1991."
    ],

    "thanks": [
        "You're welcome! 😊",
        "Happy to help!",
        "Anytime! 👍"
    ],

    "bye": [
        "Goodbye! 👋",
        "See you later!",
        "Have a wonderful day!",
        "Take care and keep coding! 🚀"
    ]
}

# Save chat history in a text file
def save_chat(user, bot):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {user}\n")
        file.write(f"Bot : {bot}\n\n")

# Generate response based on user input
def get_response(message):

    msg = message.lower().strip()

    # Greeting responses
    if any(word in msg for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greetings"])

    if "how are you" in msg:
        return random.choice(responses["how_are_you"])

    if "your name" in msg:
        return random.choice(responses["name"])

    if "who made you" in msg or "creator" in msg:
        return random.choice(responses["creator"])

    # Time feature
    if "time" in msg:
        return f"🕒 Current Time: {datetime.now().strftime('%H:%M:%S')}"

    # Date feature
    if "date" in msg:
        return f"📅 Today's Date: {datetime.now().strftime('%d-%m-%Y')}"

    if "joke" in msg:
        return random.choice(responses["jokes"])

    if "motivate me" in msg or "motivation" in msg:
        return random.choice(responses["motivation"])

    if "quote" in msg:
        return random.choice(responses["quotes"])

    if "fact" in msg:
        return random.choice(responses["facts"])

    if "thank" in msg or "thanks" in msg:
        return random.choice(responses["thanks"])

    if "help" in msg:
        return random.choice(responses["help"])

    # Calculator feature
    if msg.startswith("calculate"):
        try:
            expression = msg.replace("calculate", "").strip()
            result = eval(expression)
            return f"✅ Answer = {result}"
        except:
            return "❌ Invalid calculation."

    # Exit commands
    if any(word in msg for word in ["bye", "exit", "quit"]):
        return random.choice(responses["bye"])

    return (
        "🤔 Sorry, I don't understand that.\n"
        "Type 'help' to see available commands."
    )

# Send message and display response
def send_message():

    user_message = entry.get().strip()

    if not user_message:
        return

    chat_area.insert(tk.END, f"You : {user_message}\n")

    bot_response = get_response(user_message)

    chat_area.insert(tk.END, f"Bot : {bot_response}\n\n")

    save_chat(user_message, bot_response)

    entry.delete(0, tk.END)

    chat_area.see(tk.END)

# Clear chat window
def clear_chat():
    chat_area.delete("1.0", tk.END)

# Create main application window
root = tk.Tk()
root.title("🤖 Advanced AI ChatBot")
root.geometry("900x650")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="🤖 Advanced AI ChatBot",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=10)

# Chat display area
chat_area = scrolledtext.ScrolledText(
    root,
    width=100,
    height=28,
    font=("Consolas", 11),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)

chat_area.pack(padx=10, pady=10)

chat_area.insert(
    tk.END,
    "🤖 Welcome to Advanced AI ChatBot\n"
    "Type 'help' to see available commands.\n\n"
)

# User input section
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

entry = tk.Entry(
    frame,
    width=60,
    font=("Arial", 12)
)

entry.grid(row=0, column=0, padx=5)

send_btn = tk.Button(
    frame,
    text="Send",
    width=12,
    command=send_message
)

send_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(
    frame,
    text="Clear Chat",
    width=12,
    command=clear_chat
)

clear_btn.grid(row=0, column=2, padx=5)

exit_btn = tk.Button(
    frame,
    text="Exit",
    width=12,
    command=root.destroy
)

exit_btn.grid(row=0, column=3, padx=5)

# Press Enter to send message
entry.bind("<Return>", lambda event: send_message())

# Start chatbot application
root.mainloop()

