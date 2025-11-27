import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------------
# LOAD JOKES FROM FILE
# -----------------------------------
def loadJokes():
    jokes = []
    try:
        with open("randomjokes.txt", "r") as file:
            for line in file:
                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    jokes.append((setup.strip() + "?", punchline.strip()))
    except:
        messagebox.showerror("Error", "Could not find randomJokes.txt file!")
    return jokes


# -----------------------------------
# FUNCTIONS
# -----------------------------------

def tellJoke():
    """Display a setup of a random joke."""
    global current_setup, current_punchline

    if not jokes:
        messagebox.showerror("Error", "No jokes found!")
        return

    current_setup, current_punchline = random.choice(jokes)

    setup_label.config(text=current_setup)
    punchline_label.config(text="")  # Hide punchline
    show_punchline_btn.config(state="normal")


def showPunchline():
    """Display punchline."""
    punchline_label.config(text=current_punchline)
    show_punchline_btn.config(state="disabled")


# -----------------------------------
# MAIN GUI WINDOW
# -----------------------------------

root = tk.Tk()
root.title("Alexa Joke Assistant")
root.geometry("500x350")
root.config(bg="#f0f8ff")

jokes = loadJokes()

current_setup = ""
current_punchline = ""

# Title
title = tk.Label(root, text="Alexa Joke Assistant", font=("Arial", 20, "bold"), bg="#f0f8ff")
title.pack(pady=10)

# Joke setup label
setup_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, bg="#f0f8ff")
setup_label.pack(pady=20)

# Punchline label
punchline_label = tk.Label(root, text="", font=("Arial", 16, "italic"), fg="blue", wraplength=400, bg="#f0f8ff")
punchline_label.pack(pady=10)

# Buttons
tell_joke_btn = tk.Button(root, text="Alexa, Tell Me a Joke", font=("Arial", 14),
                          bg="#0077cc", fg="white", command=tellJoke)
tell_joke_btn.pack(pady=5)

show_punchline_btn = tk.Button(root, text="Show Punchline", font=("Arial", 14),
                               bg="#003366", fg="white", command=showPunchline, state="disabled")
show_punchline_btn.pack(pady=5)

next_joke_btn = tk.Button(root, text="Next Joke", font=("Arial", 14),
                          bg="#3399ff", fg="white", command=tellJoke)
next_joke_btn.pack(pady=5)

quit_btn = tk.Button(root, text="Quit", font=("Arial", 14),
                     bg="red", fg="white", command=root.destroy)
quit_btn.pack(pady=20)


root.mainloop()
