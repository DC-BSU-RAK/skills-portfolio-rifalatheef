import tkinter as tk
from tkinter import messagebox
import random

# -------------------------
# ANIMATION FUNCTION
# -------------------------

def fadeIn(widget, step=0):
    """Simple fade-in animation for labels."""
    if step <= 10:
        color = f"#{step*20:02x}{step*20:02x}ff"  # blue fade
        widget.config(fg=color)
        root.after(30, lambda: fadeIn(widget, step + 1))


# -------------------------
# FUNCTIONS
# -------------------------

def displayMenu():
    clearWindow()

    title = tk.Label(root, text="DIFFICULTY LEVEL", font=("Arial", 20, "bold"), fg="white", bg="#003366")
    title.pack(fill="x", pady=10)

    fadeIn(title)

    tk.Button(root, text="1. Easy", width=20, bg="#6699cc", fg="white", command=lambda: startQuiz(1)).pack(pady=5)
    tk.Button(root, text="2. Moderate", width=20, bg="#336699", fg="white", command=lambda: startQuiz(2)).pack(pady=5)
    tk.Button(root, text="3. Advanced", width=20, bg="#003366", fg="white", command=lambda: startQuiz(3)).pack(pady=5)

    tk.Button(root, text="Quit", bg="red", fg="white", width=10, command=root.destroy).pack(pady=20)


def randomInt(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)


def decideOperation():
    return random.choice(['+', '-'])


def displayProblem():
    clearWindow()

    global questionLabel, answerEntry

    # Top bar: Question number + Score
    header = tk.Frame(root, bg="#003366")
    header.pack(fill="x")

    qnum_label = tk.Label(header, text=f"Question {questionNum}/10", font=("Arial", 14, "bold"), fg="white", bg="#003366")
    qnum_label.pack(side="left", padx=10)

    score_label = tk.Label(header, text=f"Score: {score}", font=("Arial", 14, "bold"), fg="white", bg="#003366")
    score_label.pack(side="right", padx=10)

    # Fade animation
    fadeIn(qnum_label)
    fadeIn(score_label)

    # Problem text
    question_text = f"{num1} {operation} {num2} ="
    questionLabel = tk.Label(root, text=question_text, font=("Arial", 28, "bold"), fg="#003366")
    questionLabel.pack(pady=30)

    fadeIn(questionLabel)

    # Entry box
    answerEntry = tk.Entry(root, font=("Arial", 20), justify="center")
    answerEntry.pack()

    # Submit button
    tk.Button(root, text="Submit Answer", bg="#336699", fg="white", command=checkAnswer).pack(pady=15)

    # Quit button
    tk.Button(root, text="Quit", bg="red", fg="white", width=10, command=root.destroy).pack(pady=5)


def isCorrect(answer):
    if operation == "+":
        return answer == (num1 + num2)
    else:
        return answer == (num1 - num2)


def checkAnswer():
    global attempt, score

    try:
        userAnswer = int(answerEntry.get())
    except:
        messagebox.showerror("Error", "Enter a valid number")
        return

    if isCorrect(userAnswer):
        if attempt == 1:
            score += 10
            messagebox.showinfo("Correct", "Correct! +10 points")
        else:
            score += 5
            messagebox.showinfo("Correct", "Correct! +5 points")
        nextQuestion()

    else:
        if attempt == 1:
            attempt = 2
            messagebox.showwarning("Incorrect", "Wrong. Try once more!")
        else:
            messagebox.showerror("Incorrect", "Wrong again. Moving to next question")
            nextQuestion()


def nextQuestion():
    global questionNum, attempt, num1, num2, operation

    questionNum += 1

    if questionNum > 10:
        displayResults()
        return

    attempt = 1
    num1 = randomInt(level)
    num2 = randomInt(level)
    operation = decideOperation()

    displayProblem()


def displayResults():
    clearWindow()

    grade = ""
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"

    result_title = tk.Label(root, text="QUIZ RESULTS", font=("Arial", 22, "bold"), fg="white", bg="#003366")
    result_title.pack(fill="x", pady=10)
    fadeIn(result_title)

    tk.Label(root, text=f"Final Score: {score}/100", font=("Arial", 20)).pack(pady=10)
    tk.Label(root, text=f"Your Grade: {grade}", font=("Arial", 20)).pack(pady=10)

    tk.Button(root, text="Play Again", bg="#336699", fg="white", width=15, command=displayMenu).pack(pady=5)
    tk.Button(root, text="Quit", bg="red", fg="white", width=15, command=root.destroy).pack(pady=5)


def startQuiz(selectedLevel):
    global level, score, questionNum, attempt, num1, num2, operation

    level = selectedLevel
    score = 0
    questionNum = 1
    attempt = 1

    num1 = randomInt(level)
    num2 = randomInt(level)
    operation = decideOperation()

    displayProblem()


def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()


# -------------------------
# MAIN WINDOW
# -------------------------

root = tk.Tk()
root.title("Arithmetic Quiz Game")
root.geometry("500x350")
root.configure(bg="#e6f0ff")

displayMenu()

root.mainloop()

   
   

   
