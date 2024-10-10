import tkinter as tk
from tkinter import scrolledtext
import spacy
import pygame

# Initialize NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize Pygame for sound effects
pygame.mixer.init()

# Load sound effect (make sure you have a sound file named 'correct.wav')
sound = pygame.mixer.Sound(r'C:\Users\dell\Desktop\project\correct.wav')

# Response generation function using spaCy
def generate_response(user_input):
    doc = nlp(user_input)

    # Formal greetings
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hello! How can I assist you today?"

    # Formal farewells
    elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
        return "Goodbye! Have a great day ahead!"

    # Asking for help or guidance
    elif "help" in user_input.lower():
        return "I'm here to help! Please let me know what you need assistance with."

    # Python programming related questions
    elif "python" in user_input.lower():
        if "what is" in user_input.lower():
            return ("Python is a high-level, interpreted programming language known for its readability, simplicity, "
                    "and versatility. It supports multiple programming paradigms, including procedural, object-oriented, "
                    "and functional programming. It's widely used for web development, data analysis, artificial intelligence, "
                    "scientific computing, and more.")
        elif "how to" in user_input.lower():
            return ("To get started with Python, you can download it from python.org. Begin with the basic tutorials "
                    "to learn about syntax, data types, control structures, and functions. Would you like guidance on a specific topic?")
        elif "list comprehension" in user_input.lower():
            return ("List comprehension is a concise way to create lists in Python. For example, you can generate a list of squares like this: "
                    "[x**2 for x in range(10)]. It’s a powerful tool for writing cleaner and more efficient code.")
        elif "libraries" in user_input.lower():
            return ("Python has a rich ecosystem of libraries. Some popular ones include NumPy for numerical operations, "
                    "Pandas for data analysis, Matplotlib for data visualization, and Flask for web development. "
                    "Is there a particular library you're interested in?")

    # General knowledge or questions
    elif "tell me about" in user_input.lower():
        return "Could you please specify the topic you would like to know more about? I'm here to help!"

    # Catch-all response
    else:
        return "I'm here to help! Can you please provide more details or ask a specific question?"

# Function to handle user input
def send_message():
    user_input = entry_field.get()
    chat_window.configure(state='normal')
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    
    # Play sound effect
    sound.play()

    bot_response = generate_response(user_input)
    chat_window.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_window.configure(state='disabled')

    entry_field.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Basic Chatbot")
root.geometry("500x600")

# Load and set the background image
background_image = tk.PhotoImage(file=r"C:\Users\dell\Desktop\project\chatbot.png")  # Your background image path
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Frame for chat window and input field
frame = tk.Frame(root, bg='white', bd=5)  # Adding a frame with a white background
frame.place(relwidth=0.9, relheight=0.7, rely=0.1, relx=0.05)

# Chat window for conversation display
chat_window = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state='disabled', bg='white', font=("Arial", 12))
chat_window.pack(expand=True, fill=tk.BOTH)

# Entry field for user input
entry_field = tk.Entry(root, font=("Arial", 14))
entry_field.place(relwidth=0.7, relheight=0.05, rely=0.85, relx=0.05)

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.place(relwidth=0.2, relheight=0.05, rely=0.85, relx=0.75)

# Start the chatbot GUI
root.mainloop()