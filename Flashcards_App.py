import tkinter as tk

class FlashcardApp:
    def __init__(self):
        self.flashcards = []
        self.current_index = 0

        self.root = tk.Tk()
        self.root.title("Flashcard App")
        self.root.geometry("500x500")
        self.root.configure(bg="#d0f0fd")

        self.ask_input_method()

    def ask_input_method(self):
        self.clear_root()

        self.method_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.method_frame.pack(pady=40)

        tk.Label(self.method_frame, text="Choose how to input flashcards:",
                 font=("Arial", 14), bg="#e0f7fa").pack(pady=10)

        tk.Button(self.method_frame, text="Upload File", width=20,
                  command=self.upload_ui).pack(pady=5)

        tk.Button(self.method_frame, text="Enter Manually", width=20,
                  command=self.manual_entry_ui).pack(pady=5)

        self.error_label = tk.Label(self.root, text="", fg="red", bg="#d0f0fd", font=("Arial", 10))
        self.error_label.pack(pady=5)

    def upload_ui(self):
        self.clear_root()

        self.upload_frame = tk.Frame(self.root, bg="#d0f0fd")
        self.upload_frame.pack(pady=20)

        tk.Label(self.upload_frame, text="Enter file path (txt, term::definition):",
                 font=("Arial", 12), bg="#d0f0fd").pack(pady=5)

        self.file_entry = tk.Entry(self.upload_frame, width=40)
        self.file_entry.pack(pady=5)

        tk.Button(self.upload_frame, text="Load Flashcards", command=self.load_from_text).pack(pady=10)

        self.error_label = tk.Label(self.root, text="", fg="red", bg="#d0f0fd", font=("Arial", 10))
        self.error_label.pack(pady=5)

    def load_from_text(self):
        path = self.file_entry.get()
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if "::" in line:
                        term, definition = line.strip().split("::", 1)
                        self.flashcards.append((term, definition))
            if self.flashcards:
                self.start_app()
            else:
                self.error_label.config(text="No valid flashcards found.")
        except Exception as e:
            self.error_label.config(text=f"Error: {str(e)}")

    def manual_entry_ui(self):
        self.clear_root()

        self.manual_frame = tk.Frame(self.root, bg="#d0f0fd")
        self.manual_frame.pack(pady=20)

        tk.Label(self.manual_frame, text="Enter Term:", bg="#d0f0fd").pack()
        self.term_entry = tk.Entry(self.manual_frame, width=40)
        self.term_entry.pack(pady=5)

        tk.Label(self.manual_frame, text="Enter Definition:", bg="#d0f0fd").pack()
        self.def_entry = tk.Entry(self.manual_frame, width=40)
        self.def_entry.pack(pady=5)

        tk.Button(self.manual_frame, text="Add Flashcard", command=self.add_manual_card).pack(pady=10)
        tk.Button(self.manual_frame, text="Start Flashcards", command=self.start_flashcards_from_manual).pack()

        self.status_label = tk.Label(self.root, text="", fg="green", bg="#d0f0fd", font=("Arial", 10))
        self.status_label.pack(pady=5)

    def start_flashcards_from_manual(self):
        if not self.flashcards:
            self.status_label.config(text="Please add at least one flashcard.", fg="red")
        else:
            self.start_app()

    def add_manual_card(self):
        term = self.term_entry.get().strip()
        definition = self.def_entry.get().strip()
        if term and definition:
            self.flashcards.append((term, definition))
            self.term_entry.delete(0, tk.END)
            self.def_entry.delete(0, tk.END)
            self.status_label.config(text="Flashcard added!")
        else:
            self.status_label.config(text="Both fields are required.", fg="red")

    def start_app(self):
        if not self.flashcards:
            return
        self.clear_root()
        self.setup_layout()
        self.create_widgets()
        self.update_card()

    def setup_layout(self):
        self.top_frame = tk.Frame(self.root, bg="#d0f0fd")
        self.top_frame.pack(pady=20)

        self.middle_frame = tk.Frame(self.root, bg="#d0f0fd")
        self.middle_frame.pack(pady=10)

        self.bottom_frame = tk.Frame(self.root, bg="#d0f0fd")
        self.bottom_frame.pack(side="bottom", pady=20)

    def create_widgets(self):
        self.term_label = tk.Label(self.top_frame, text="", font=("Arial", 22, "bold"),
                                   bg="#d0f0fd", fg="#004080")
        self.term_label.pack()

        self.definition_label = tk.Label(self.middle_frame, text="", font=("Arial", 18, "italic"),
                                         bg="#d0f0fd", fg="#006600", wraplength=400, justify="center")
        self.definition_label.pack()
        self.definition_label.pack_forget()

        button_opts = {
            "width": 16,
            "height": 2,
            "font": ("Arial", 12, "bold"),
            "relief": "raised",
            "bd": 4,
            "cursor": "hand2"
        }

        self.show_btn = tk.Button(self.bottom_frame, text="Show Answer", bg="#ffeb3b", fg="black",
                                  command=self.show_answer, **button_opts)
        self.show_btn.grid(row=0, column=0, padx=15, pady=10)

        self.next_btn = tk.Button(self.bottom_frame, text="Next", bg="#4caf50", fg="white",
                                  command=self.next_card, **button_opts)
        self.next_btn.grid(row=0, column=1, padx=15, pady=10)

        self.correct_btn = tk.Button(self.bottom_frame, text="Correct", bg="#2196f3", fg="white", **button_opts)
        self.correct_btn.grid(row=1, column=0, padx=15, pady=10)

        self.incorrect_btn = tk.Button(self.bottom_frame, text="Incorrect", bg="#f44336", fg="white", **button_opts)
        self.incorrect_btn.grid(row=1, column=1, padx=15, pady=10)

    def update_card(self):
        term, _ = self.flashcards[self.current_index]
        self.term_label.config(text=term)
        self.definition_label.config(text="")
        self.definition_label.pack_forget()

    def show_answer(self):
        _, definition = self.flashcards[self.current_index]
        self.definition_label.config(text=definition)
        self.definition_label.pack()

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.update_card()

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = FlashcardApp()
    app.run()
