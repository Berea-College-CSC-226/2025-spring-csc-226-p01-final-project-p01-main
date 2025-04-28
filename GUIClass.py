import tkinter as tk

class FlashcardGUI:
    def __init__(self, app_logic):
        self.app_logic = app_logic
        self.root = tk.Tk()
        self.root.title("Flashcard App")
        self.root.geometry("500x500")
        self.root.configure(bg="#d0f0fd")
        self.cards_seen = 0
        self.total_rounds = len(self.app_logic.flashcards)  # adjust as needed

        self.current_card = None

        self.setup_initial_ui()

    def setup_initial_ui(self):
        self.clear_root()

        frame = tk.Frame(self.root, bg="#e0f7fa")
        frame.pack(pady=40)

        tk.Label(frame, text="Choose how to input flashcards:",
                 font=("Arial", 14), bg="#e0f7fa").pack(pady=10)

        tk.Button(frame, text="Upload File", width=20,
                  command=self.upload_ui).pack(pady=5)
        tk.Button(frame, text="Enter Manually", width=20,
                  command=self.manual_entry_ui).pack(pady=5)

        self.error_label = tk.Label(self.root, text="", fg="red", bg="#d0f0fd", font=("Arial", 10))
        self.error_label.pack(pady=5)

    def upload_ui(self):
        self.clear_root()

        frame = tk.Frame(self.root, bg="#d0f0fd")
        frame.pack(pady=20)

        tk.Label(frame, text="Enter file path (term::definition):",
                 font=("Arial", 12), bg="#d0f0fd").pack(pady=5)
        self.file_entry = tk.Entry(frame, width=40)
        self.file_entry.pack(pady=5)

        tk.Button(frame, text="Load Flashcards",
                  command=self.load_flashcards).pack(pady=10)
        self.error_label = tk.Label(self.root, text="", fg="red", bg="#d0f0fd", font=("Arial", 10))
        self.error_label.pack(pady=5)

    def load_flashcards(self):
        path = self.file_entry.get()
        success, msg = self.app_logic.load_from_file(path)
        if success and self.app_logic.flashcards:
            self.start_flashcard_session()
        else:
            self.error_label.config(text=f"Error: {msg}")

    def manual_entry_ui(self):
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
        self.current_card = self.app_logic.get_random_flashcard()
        if not self.current_card:
            return

        self.term_label = tk.Label(self.root, text=self.current_card.term,
                                   font=("Arial", 22), bg="#d0f0fd")
        self.term_label.pack(pady=20)

        self.def_label = tk.Label(self.root, text="", font=("Arial", 18),
                                  bg="#d0f0fd", wraplength=400)
        self.def_label.pack(pady=10)

        tk.Button(self.root, text="Show Answer", command=self.show_answer).pack(pady=5)
        tk.Button(self.root, text="Correct", command=self.mark_correct).pack(pady=5)
        tk.Button(self.root, text="Incorrect", command=self.mark_incorrect).pack(pady=5)

    def show_answer(self):
        self.def_label.config(text=self.current_card.definition)

    def mark_correct(self):
        self.current_card.score += 1
        self.next_card()

    def mark_incorrect(self):
        self.current_card.score = max(0, self.current_card.score - 1)
        self.next_card()

    def next_card(self):
        self.cards_seen += 1
        if self.cards_seen >= self.total_rounds:
            self.show_final_score()
        else:
            self.current_card = self.app_logic.get_random_flashcard()
            self.term_label.config(text=self.current_card.term)
            self.def_label.config(text="")

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

    def show_final_score(self):
        self.clear_root()
        total_score, total_cards = self.app_logic.get_total_score()

        frame = tk.Frame(self.root, bg="#d0f0fd")
        frame.pack(expand=True)

        score_msg = f"Your final score is {total_score} out of {total_cards * 3}!"
        tk.Label(frame, text="Session Complete!", font=("Arial", 22, "bold"), bg="#d0f0fd").pack(pady=10)
        tk.Label(frame, text=score_msg, font=("Arial", 18), bg="#d0f0fd").pack(pady=10)

        tk.Button(frame, text="Exit", command=self.root.destroy).pack(pady=20)

