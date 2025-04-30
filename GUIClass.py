import tkinter as tk
import random

class FlashcardGUI:
    def __init__(self, app_logic):
        self.app_logic = app_logic
        self.root = tk.Tk()
        self.root.title("Flashcard App")
        self.root.geometry("500x500")
        self.root.configure(bg="#d0f0fd")

        # Session variables
        self.current_card = None
        self.session_flashcards = []
        self.current_index = 0
        self.correct_answers = 0

        self.setup_initial_ui()

    def setup_initial_ui(self):
        # Start screen for choosing input method
        self.clear_root()

        frame = tk.Frame(self.root, bg="#e0f7fa")
        frame.pack(pady=40)

        tk.Label(frame, text="Choose how to input flashcards:", font=("Arial", 14), bg="#e0f7fa").pack(pady=10)
        tk.Button(frame, text="Upload File", width=20, command=self.upload_ui).pack(pady=5)
        tk.Button(frame, text="Enter Manually", width=20, command=self.manual_entry_ui).pack(pady=5)

        self.error_label = tk.Label(self.root, text="", fg="red", bg="#d0f0fd", font=("Arial", 10))
        self.error_label.pack(pady=5)

    def upload_ui(self):
        # UI for file upload
        self.clear_root()
        frame = tk.Frame(self.root, bg="#d0f0fd")
        frame.pack(pady=20)

        tk.Label(frame, text="Enter file path (term::definition):", font=("Arial", 12), bg="#d0f0fd").pack(pady=5)
        self.file_entry = tk.Entry(frame, width=40)
        self.file_entry.pack(pady=5)
        tk.Button(frame, text="Load Flashcards", command=self.load_flashcards).pack(pady=10)

        self.error_label = tk.Label(self.root, text="", fg="red", bg="#d0f0fd", font=("Arial", 10))
        self.error_label.pack(pady=5)

    def load_flashcards(self):
        # Load flashcards from a file
        path = self.file_entry.get()
        success, msg = self.app_logic.load_from_file(path)
        if success and self.app_logic.flashcards:
            self.start_flashcard_session()
        else:
            self.error_label.config(text=f"Error: {msg}")

    def manual_entry_ui(self):
        # UI for entering flashcards manually
        self.clear_root()
        frame = tk.Frame(self.root, bg="#d0f0fd")
        frame.pack(pady=20)

        tk.Label(frame, text="Term:", bg="#d0f0fd").pack()
        self.term_entry = tk.Entry(frame, width=40)
        self.term_entry.pack(pady=5)

        tk.Label(frame, text="Definition:", bg="#d0f0fd").pack()
        self.def_entry = tk.Entry(frame, width=40)
        self.def_entry.pack(pady=5)

        tk.Button(frame, text="Add Flashcard", command=self.add_flashcard).pack(pady=10)
        tk.Button(frame, text="Start Session", command=self.start_flashcard_session).pack()

        self.status_label = tk.Label(self.root, text="", fg="green", bg="#d0f0fd", font=("Arial", 10))
        self.status_label.pack(pady=5)

    def add_flashcard(self):
        # Add a single flashcard to the deck
        term = self.term_entry.get().strip()
        definition = self.def_entry.get().strip()
        if term and definition:
            self.app_logic.add_flashcard(term, definition)
            self.status_label.config(text="Flashcard added!")
            self.term_entry.delete(0, tk.END)
            self.def_entry.delete(0, tk.END)
        else:
            self.status_label.config(text="Both fields required.", fg="red")

    def start_flashcard_session(self):
        self.clear_root()

        if not self.app_logic.flashcards:
            self.error_label = tk.Label(self.root, text="No flashcards loaded!", fg="red", bg="#d0f0fd")
            self.error_label.pack(pady=5)
            return

        # Create a fresh session with shuffled cards
        self.session_flashcards = self.app_logic.flashcards[:]
        random.shuffle(self.session_flashcards)

        # Reset session trackers
        self.current_index = 0
        self.correct_answers = 0

        # Show the first card
        self.show_card()

    def show_card(self):
        self.current_card = self.session_flashcards[self.current_index]

        self.term_label = tk.Label(self.root, text=self.current_card.term,
                                   font=("Arial", 22), bg="#d0f0fd")
        self.term_label.pack(pady=20)

        self.def_label = tk.Label(self.root, text="", font=("Arial", 18),
                                  bg="#d0f0fd", wraplength=400)
        self.def_label.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#d0f0fd")
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Show Answer", command=self.show_answer,
                  bg="red", fg="white", width=12).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(button_frame, text="Correct", command=self.mark_correct,
                  bg="dark blue", fg="white", width=12).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(button_frame, text="Incorrect", command=self.mark_incorrect,
                  bg="yellow", fg="black", width=12).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(button_frame, text="Next", command=self.next_card,
                  bg="green", fg="white", width=12).grid(row=1, column=1, padx=5, pady=5)

    def show_answer(self):
        # Reveal the definition
        self.def_label.config(text=self.current_card.definition)

    def mark_correct(self):
        self.current_card.score += 1
        self.correct_answers += 1
        # Don't go to next card yet — wait for user to click "Next"

    def mark_incorrect(self):
        self.current_card.score = max(0, self.current_card.score - 1)
        # Wait for user to click "Next"

    def next_card(self):
        self.current_index += 1
        if self.current_index >= len(self.session_flashcards):
            self.show_final_score()
        else:
            self.clear_root()
            self.show_card()

    def clear_root(self):
        # Clear all UI elements
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        # Start the Tkinter main loop
        self.root.mainloop()

    def show_final_score(self):
        # Display final session results
        self.clear_root()

        frame = tk.Frame(self.root, bg="#d0f0fd")
        frame.pack(expand=True)

        score_msg = f"You got {self.correct_answers} out of {len(self.session_flashcards)} correct!"
        tk.Label(frame, text="Session Complete!", font=("Arial", 22, "bold"), bg="#d0f0fd").pack(pady=10)
        tk.Label(frame, text=score_msg, font=("Arial", 18), bg="#d0f0fd").pack(pady=10)

        tk.Button(frame, text="Exit", command=self.root.destroy).pack(pady=20)
