import html
import tkinter as tk
from tkinter import ttk, messagebox
import random
from questions import Question
from quizbrain import QuizBrain
from data import fetch_categories, fetch_questions

class QuizInterface:
    def __init__(self, window):
        """
        Initialize the layout and the elements of the quiz
        :param window: the game window
        """
        # Initialize main window and UI settings
        self.window = window
        self.window.title("Trivia Quiz Game")
        self.window.config(bg="#660033")  # Set background color (purple theme)

        # Timer setup
        self.timer_label = None
        self.timer_count = 10
        self.timer_job = None

        # Core components of the quiz
        self.top_frame = None
        self.quiz = None
        self.buttons = []  # Stores the 4 option buttons
        self.canvas = None  # Displays the question
        self.question_text = None  # Text ID for canvas question
        self.score_label = None  # Shows current score
        self.buttons_frame = None  # Container for answer buttons
        self.final_frame = None  # Holds the "Play Again / Exit" screen

        # Load quiz categories from the API
        self.categories = fetch_categories()

        # Create the setup screen
        self.setup_frame = tk.Frame(window, bg="#660033")
        self.setup_frame.pack(pady=20, padx=20)

        # Form variables for the quiz configuration
        self.category_var = tk.StringVar()
        self.difficulty_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        self.create_setup_screen()

    def create_setup_screen(self):
        """
        Create the setup screen and asks for user's inputs
        :return: None
        """
        tk.Label(self.setup_frame, text="Welcome to the Trivia Quiz Game", font=("Times New Roman", 12), bg="#660033", fg="white").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Dropdown for category
        tk.Label(self.setup_frame, text="Select Category", font=("Times New Roman", 12), bg="#660033", fg="white").grid(row=1, column=0, sticky="w", padx=10)
        category_dropdown = ttk.Combobox(self.setup_frame, textvariable=self.category_var, values=list(self.categories.keys()), width=30)
        category_dropdown.grid(row=1, column=1)

        # Dropdown for difficulty
        tk.Label(self.setup_frame, text="Select Difficulty", font=("Times New Roman", 12), bg="#660033", fg="white").grid(row=2, column=0, sticky="w", padx=10)
        difficulty_dropdown = ttk.Combobox(self.setup_frame, textvariable=self.difficulty_var, values=["Easy", "Medium", "Hard"], width=30)
        difficulty_dropdown.grid(row=2, column=1)

        # Entry for number of questions
        tk.Label(self.setup_frame, text="Number of Questions", font=("Times New Roman", 12), bg="#660033", fg="white").grid(row=3, column=0, sticky="w", padx=10)
        amount_entry = tk.Entry(self.setup_frame, textvariable=self.amount_var, width=33)
        amount_entry.grid(row=3, column=1)

        # Start button
        start_button = tk.Button(self.setup_frame, text="Start Quiz", font=("Times New Roman", 14), command=self.start_quiz)
        start_button.grid(row=4, column=0, columnspan=2, pady=20)

    def start_quiz(self):
        """
        Fetch and get data from the database
        :return: None
        """
        cat_name = self.category_var.get()
        diff = self.difficulty_var.get().lower()
        amount = self.amount_var.get()

        # Validate form input
        if cat_name not in self.categories or diff not in ["easy", "medium", "hard"] or not amount.isdigit():
            messagebox.showwarning("Invalid Input", "Please complete all fields correctly.")
            return

        # Fetch questions
        try:
            data = fetch_questions(int(amount), self.categories[cat_name], diff)
        except Exception as e:
            messagebox.showerror("Error", f"Couldn't fetch questions.\n{e}")
            return

        # Convert data into Question objects
        question_bank = []
        for q in data:
            options = q["incorrect_answers"] + [q["correct_answer"]]
            random.shuffle(options)
            question_bank.append(Question(q["question"], options, q["correct_answer"]))

        self.quiz = QuizBrain(question_bank)

        # Hide setup screen and show the quiz UI
        self.setup_frame.pack_forget()
        self.show_quiz_screen()

    def show_quiz_screen(self):
        """
        Display the main quiz UI: score, timer, question, and answer buttons
        :return: None
        """
        # Score and Timer section
        self.top_frame = tk.Frame(self.window, bg="#660033")
        self.top_frame.pack(fill="x", padx=20, pady=(10, 0))

        self.timer_label = tk.Label(self.top_frame, text="Time Left: 10s", fg="white", bg="#660033", font=("Times New Roman", 12))
        self.timer_label.pack(side="left")

        self.score_label = tk.Label(self.top_frame, text="Score: 0", fg="white", bg="#660033", font=("Times New Roman", 12))
        self.score_label.pack(side="right")

        # Question area
        self.canvas = tk.Canvas(width=500, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            250, 125, width=420, text="Question here",
            fill="black", font=("Times New Roman", 16, "bold")
        )
        self.canvas.pack(padx=30, pady=30)

        # Answer buttons frame (2x2 grid)
        self.buttons_frame = tk.Frame(self.window, bg="#660033")
        self.buttons_frame.pack()

        for i in range(4):
            btn = tk.Button(self.buttons_frame, text="Option", font=("Times New Roman", 12), width=25, height=2,
                            bg="#f0f0f0", fg="black", wraplength=350, justify="center", anchor="center", relief="raised"
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            self.buttons.append(btn)

        self.get_next_question()

    def start_timer(self):
        """
        Start or continue the countdown timer
        :return: None
        """
        self.timer_label.config(text=f"Time Left: {self.timer_count}s")
        if self.timer_count > 0:
            self.timer_count -= 1
            self.timer_job = self.window.after(1000, self.start_timer)
        else:
            # Time's up behavior
            self.canvas.itemconfig(self.question_text, text="⏱ Time's Up!\n" + self.canvas.itemcget(self.question_text, "text"))
            for btn in self.buttons:
                btn.config(state="disabled")
                if btn["text"] == self.quiz.current_question.answer:
                    btn.config(bg="green", fg="white", activebackground="green", activeforeground="white", disabledforeground="white")
            self.window.after(1500, self.get_next_question)

    def check_answer(self, user_choice):
        """
        Handle button press — check answer and show feedback
        :param user_choice: the user's choice
        :return: None
        """
        if self.timer_job:
            self.window.after_cancel(self.timer_job)

        correct_answer = self.quiz.current_question.answer

        for btn in self.buttons:
            btn.config(state="disabled")

            # Color feedback for selected and correct answers
            if btn["text"] == user_choice:
                if user_choice == correct_answer:
                    btn.config(bg="green", fg="white", activebackground="green", activeforeground="white", disabledforeground="white")
                    self.quiz.score += 1
                else:
                    btn.config(bg="red", fg="white", activebackground="red", activeforeground="white", disabledforeground="white")

            elif btn["text"] == correct_answer:
                btn.config(bg="green", fg="white", activebackground="green", activeforeground="white", disabledforeground="white")

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(750, self.get_next_question)

    def get_next_question(self):
        """
        Load the next question and reset UI state
        :return: None
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            # Reset and start timer
            if self.timer_job:
                self.window.after_cancel(self.timer_job)
            self.timer_count = 10
            self.start_timer()

            # Display next question
            q_text, options = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

            # Update answer buttons
            for i in range(4):
                option_text = html.unescape(options[i])
                self.buttons[i].config(text=option_text, command=lambda opt=option_text: self.check_answer(opt), state="normal",
                                       bg="#f0f0f0", fg="black", activebackground="#f0f0f0", activeforeground="black", disabledforeground="black"
                )
        else:
            self.show_final_screen()

    def show_final_screen(self):
        """
        Display score and ask user to play again or exit
        :return: None
        """
        # Clean up quiz UI
        self.canvas.pack_forget()
        self.score_label.pack_forget()
        self.buttons_frame.pack_forget()
        self.top_frame.pack_forget()

        # Create final screen with score and options
        self.final_frame = tk.Frame(self.window, bg="#660033")
        self.final_frame.pack(pady=50)

        final_msg = tk.Label(self.final_frame, text=f"Final Score: {self.quiz.score}/{self.quiz.question_number}",
                             font=("Times New Roman", 16), fg="white", bg="#660033", justify="center"
        )
        final_msg.pack(pady=20)

        continue_msg = tk.Label(self.final_frame, text="Do you want to continue playing?",
                                font=("Times New Roman", 16), fg="white", bg="#660033", justify="center"
        )
        continue_msg.pack(padx=20, pady=20)

        btn_row = tk.Frame(self.final_frame, bg="#660033")
        btn_row.pack()

        btn_width = 15

        again_btn = tk.Button(btn_row, text="Play Again", font=("Times New Roman", 12),width=btn_width,command=self.restart_quiz)
        again_btn.grid(row=0, column=0, padx=10)

        exit_btn = tk.Button(btn_row, text="Exit", font=("Times New Roman", 12), width=btn_width, command=self.window.quit)
        exit_btn.grid(row=0, column=1, padx=10)

    def restart_quiz(self):
        """
        Reset game state and return to the setup screen
        :return: None
        """
        if hasattr(self, 'final_frame'):
            self.final_frame.pack_forget()

        # Hide and reset remaining elements
        self.canvas.pack_forget()
        self.score_label.pack_forget()
        self.buttons_frame.pack_forget()

        self.top_frame.pack_forget()
        if self.timer_job:
            self.window.after_cancel(self.timer_job)

        for btn in self.buttons:
            btn.grid_forget()
        self.buttons = []

        # Reset form fields
        self.category_var.set("")
        self.difficulty_var.set("")
        self.amount_var.set("")

        # Show setup screen again
        self.setup_frame.pack(pady=20, padx=20)