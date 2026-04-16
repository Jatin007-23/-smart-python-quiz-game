import tkinter as tk
from tkinter import messagebox
import random

# ------------------ QUESTIONS ------------------ #
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["Python", "HTML", "CSS", "XML"],
        "answer": "Python"
    },
    {
        "question": "How many days in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "What is the output of 2 ** 3 in Python?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which of the following is NOT a programming language?",
        "options": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML"
    },
    {
        "question": "Which of the following is mutable in Python?",
        "options": ["Tuple", "String", "List", "Integer"],
        "answer": "List"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which protocol is used to access websites?",
        "options": ["FTP", "HTTP", "SMTP", "IP"],
        "answer": "HTTP"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },
    {
        "question": "Which loop is used when number of iterations is known?",
        "options": ["while", "for", "do-while", "loop"],
        "answer": "for"
    },
]

# ------------------ MAIN APP ------------------ #
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")

        self.score = 0
        self.q_index = 0
        random.shuffle(questions)

        self.show_welcome()

    # ------------------ WELCOME SCREEN ------------------ #
    def show_welcome(self):
        self.clear_screen()

        tk.Label(self.root, text="🎮 Welcome to Quiz Game", font=("Arial", 18)).pack(pady=20)

        tk.Label(self.root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=10)

        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        self.name = self.name_entry.get()
        if not self.name:
            messagebox.showwarning("Warning", "Please enter your name")
            return
        self.score = 0
        self.q_index = 0
        self.show_question()

    # ------------------ QUIZ SCREEN ------------------ #
    def show_question(self):
        self.clear_screen()

        if self.q_index >= len(questions):
            self.show_result()
            return

        q = questions[self.q_index]

        tk.Label(self.root, text=q["question"], font=("Arial", 14)).pack(pady=20)

        self.selected = tk.StringVar()

        for option in q["options"]:
            tk.Radiobutton(self.root, text=option, variable=self.selected, value=option).pack(anchor="w")

        tk.Button(self.root, text="Next", command=self.check_answer).pack(pady=20)

    def check_answer(self):
        selected = self.selected.get()
        if selected == "":
            messagebox.showwarning("Warning", "Select an answer")
            return

        if selected == questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1
        self.show_question()

    # ------------------ RESULT SCREEN ------------------ #
    def show_result(self):
        self.clear_screen()

        tk.Label(self.root, text=f"🎯 {self.name}, Your Score: {self.score}", font=("Arial", 16)).pack(pady=30)

        tk.Button(self.root, text="Play Again", command=self.show_welcome).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    # ------------------ CLEAR SCREEN ------------------ #
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ------------------ RUN APP ------------------ #
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
