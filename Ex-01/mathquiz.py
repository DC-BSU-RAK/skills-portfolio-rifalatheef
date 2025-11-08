import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------
# Functions
# ---------------------------

def displayMenu():
    """Display difficulty selection menu."""
    clear_window()

    title = tk.Label(root, text="🎯 MATHS QUIZ 🎯", font=("Arial", 20, "bold"), fg="#333", bg="#F2F2F2")
    title.pack(pady=20)

    subtitle = tk.Label(root, text="Select Difficulty Level", font=("Arial", 14), bg="#F2F2F2")
    subtitle.pack(pady=10)

    btn_easy = tk.Button(root, text="1. Easy (1-digit)", width=20, font=("Arial", 12),
                         bg="#C8E6C9", activebackground="#A5D6A7", command=lambda: start_quiz('easy'))
    btn_easy.pack(pady=8)

    btn_mod = tk.Button(root, text="2. Moderate (2-digit)", width=20, font=("Arial", 12),
                        bg="#FFF59D", activebackground="#FFF176", command=lambda: start_quiz('moderate'))
    btn_mod.pack(pady=8)

    btn_adv = tk.Button(root, text="3. Advanced (4-digit)", width=20, font=("Arial", 12),
                        bg="#FFAB91", activebackground="#FF8A65", command=lambda: start_quiz('advanced'))
    btn_adv.pack(pady=8)

    quit_btn = tk.Button(root, text="Exit", width=15, font=("Arial", 11),
                         bg="#EF9A9A", activebackground="#E57373", command=root.destroy)
    quit_btn.pack(pady=25)


def randomInt(level):
    "Return a random integer based on the difficulty level."""
    if level == 'easy':
        return random.randint(1, 9)
    elif level == 'moderate':
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)


def decideOperation():
    """Randomly return + or -"""
    return random.choice(['+', '-'])


def displayProblem():
    """Display math question."""
    clear_window()
    global num1, num2, op, attempt

    op = decideOperation()
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)

    question_label = tk.Label(root, text=f"Question {question_number + 1}/10", font=("Arial", 13, "bold"), bg="#F2F2F2")
    question_label.pack(pady=10)

    problem_label = tk.Label(root, text=f"{num1} {op} {num2} = ?", font=("Arial", 22, "bold"), fg="#1E88E5", bg="#F2F2F2")
    problem_label.pack(pady=20)

    answer_frame = tk.Frame(root, bg="#F2F2F2")
    answer_frame.pack(pady=10)

    tk.Label(answer_frame, text="Your Answer: ", font=("Arial", 12), bg="#F2F2F2").pack(side=tk.LEFT, padx=5)
    answer_entry.delete(0, tk.END)
    answer_entry.pack(in_=answer_frame, side=tk.LEFT, padx=5)

    submit_btn = tk.Button(root, text="Submit", font=("Arial", 12), bg="#BBDEFB", activebackground="#90CAF9", command=checkAnswer)
    submit_btn.pack(pady=15)


def isCorrect(user_answer):
    """Check if the user's answer is correct."""
    correct = num1 + num2 if op == '+' else num1 - num2
    return user_answer == correct


def checkAnswer():
    """Handle user answer and scoring."""
    global score, attempt, question_number

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if isCorrect(user_answer):
        if attempt == 1:
            score += 10
            messagebox.showinfo("Correct!", "✅ Perfect! You got 10 points.")
        else:
            score += 5
            messagebox.showinfo("Correct!", "👍 Good job! You got 5 points.")
        nextQuestion()
    else:
        if attempt == 1:
            attempt += 1
            messagebox.showwarning("Try Again", "❌ Incorrect! You have one more try.")
            displayProblem()
        else:
            messagebox.showinfo("Incorrect", "😕 Wrong again! Moving to the next question.")
            nextQuestion()


def nextQuestion():
    """Go to next question or display results."""
    global question_number, attempt
    question_number += 1
    attempt = 1
    if question_number < 10:
        displayProblem()
    else:
        displayResults()


def displayResults():
    """Show final results."""
    clear_window()

    grade = ""
    if score >= 90:
        grade = "A+"
    elif score >= 75:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    else:
        grade = "F"

    tk.Label(root, text="🎉 QUIZ COMPLETED 🎉", font=("Arial", 18, "bold"), fg="#4CAF50", bg="#F2F2F2").pack(pady=20)
    tk.Label(root, text=f"Your Final Score: {score}/100", font=("Arial", 14), bg="#F2F2F2").pack(pady=10)
    tk.Label(root, text=f"Your Grade: {grade}", font=("Arial", 14, "bold"), fg="#1E88E5", bg="#F2F2F2").pack(pady=10)

    tk.Button(root, text="Play Again", width=15, font=("Arial", 12),
              bg="#AED581", activebackground="#9CCC65", command=displayMenu).pack(pady=10)
    tk.Button(root, text="Exit", width=15, font=("Arial", 12),
              bg="#EF9A9A", activebackground="#E57373", command=root.destroy).pack(pady=10)


def start_quiz(level):
    """Initialize quiz settings and start."""
    global difficulty, score, question_number, attempt
    difficulty = level
    score = 0
    question_number = 0
    attempt = 1
    displayProblem()


def clear_window():
    """Remove all widgets."""
    for widget in root.winfo_children():
        widget.destroy()


# ---------------------------
# GUI Setup
# ---------------------------
root = tk.Tk()
root.title("Maths Quiz App")
root.geometry("420x420")
root.resizable(False, False)
root.config(bg="#F2F2F2")

answer_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=10)

displayMenu()

root.mainloop()
