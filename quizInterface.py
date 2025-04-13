import html
import tkinter as tk
from tkinter import ttk, messagebox
import random
from questions import Question
from quizbrain import QuizBrain
from data import fetch_categories, fetch_questions

class QuizInterface:
    def __init__(self, window):
        self.window = window
        self.window.title("Trivia Quiz Game")
        self.window.config(bg="#00ffff")

        self.quiz = None
        self.buttons = []
        self.canvas = None
        self.question_text = None
        self.score_label = None
        self.buttons_frame = None

        self.categories = fetch_categories()

        self.setup_frame = tk.Frame(window, bg="#00ffff")
        self.setup_frame.pack(pady=20, padx=20)

        self.category_var = tk.StringVar()
        self.difficulty_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        self.create_setup_screen()


    def create_setup_screen(self):
        tk.Label(self.setup_frame, text="Welcome To The Quiz Game", bg="#00ffff", font=("Times New Roman", 14)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)#title of the screen

        tk.Label(self.setup_frame, text="Select Category", bg="#00ffff", font=("Times New Roman", 14)).grid(row=1, column=0, sticky="w", padx=10)
        category_dropdown = ttk.Combobox(self.setup_frame, textvariable=self.category_var, values=list(self.categories.keys()), width=30)
        category_dropdown.grid(row=1, column=1)

        tk.Label(self.setup_frame, text="Select Difficulty", bg="#00ffff", font=("Times New Roman", 14)).grid(row=2, column=0, sticky="w", padx=10)
        difficulty_dropdown = ttk.Combobox(self.setup_frame, textvariable=self.difficulty_var, values=["Easy", "Medium", "Hard"], width=30)
        difficulty_dropdown.grid(row=2, column=1)

        tk.Label(self.setup_frame, text="Number of Questions", bg="#00ffff", font=("Times New Roman", 14)).grid(row=3, column=0, sticky="w", padx=10)
        amount_entry = tk.Entry(self.setup_frame, textvariable=self.amount_var, width=33)
        amount_entry.grid(row=3, column=1)

        start_button = tk.Button(self.setup_frame, text="Start Game", font=("Times New Roman", 14), command=self.start_quiz)
        start_button.grid(row=4, column=0, columnspan=2, pady=10)

    def start_quiz(self):
        cat_name = self.category_var.get()
        diff = self.difficulty_var.get().lower()
        amount = self.amount_var.get()

        if cat_name not in self.categories or diff not in ["easy", "medium", "hard"] or not amount.isdigit():
            messagebox.showwarning(title="Invalid Input", message="Make sure all inputs are valid")
            return

        try:
            data = fetch_questions(int(amount), self.categories[cat_name], diff)
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Couldn't fetch questions. \n{e}")
            return

        question_bank = []
        for q in data:
            options = q["incorrect_answers"] + [q["correct_answer"]]
            random.shuffle(options)
            question_bank.append(Question(q["question"], options, q["correct_answer"]))

            self.quiz = QuizBrain(question_bank)

            self.setup_frame.pack_forget()
            self.show_quiz_screen()

    def show_quiz_screen(self):
        self.score_label = tk.Label(text="Score: 0", bg="#00ffff", fg="black", font=("Times New Roman", 11))
        self.score_label.pack(anchor="ne", padx=20, pady=10)

        self.canvas = tk.Canvas(width=500, height=250, bg="white")
        self.question_text = self.canvas.create_text(250, 125, width= 420, text="Placeholder", fill="black", font=("Times New Roman", 14))
        self.canvas.pack(padx=30, pady=30)

        self.buttons_frame = tk.Frame(self.window, bg="#00ffff")
        self.buttons_frame.pack()

        for i in range(4):
            btn = tk.Button(
                self.buttons_frame,
                text="Placeholder",
                font=("Times New Roman", 14),
                width=25,
                height=2,
                bg="white",
                fg="black",
                wraplength=350,
                justify="center",
                anchor="center",
                relief="raised"
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            self.buttons.append(btn)

        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            q_text, options = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        for i in range(4):
            option_text = html.unescape(options[i])
            self.buttons[i].config(
                text=option_text,
                command=lambda opt=option_text: self.check_answer(opt),
                state="normal",
                bg="white",
                fg="black",
                activebackground="white", activeforeground="black",
                disabledforeground="black"
            )
    def check_answer(self):
