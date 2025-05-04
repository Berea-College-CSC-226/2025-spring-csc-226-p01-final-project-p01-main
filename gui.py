import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Flashcard App")
root.geometry("450x400")
root.configure(bg="#d0f0fd")  # light blue

# Layout frames
top_frame = tk.Frame(root, bg="#d0f0fd")
top_frame.pack(pady=20)

middle_frame = tk.Frame(root, bg="#d0f0fd")
middle_frame.pack(pady=10)

# Bottom frame pinned to bottom using pack 'side'
bottom_frame = tk.Frame(root, bg="#d0f0fd")
bottom_frame.pack(side="bottom", pady=20)

# Term label
term_label = tk.Label(top_frame, text="Term goes here", font=("Arial", 22, "bold"),
                      bg="#d0f0fd", fg="#004080")
term_label.pack()

# Definition label (hidden initially)
definition_label = tk.Label(middle_frame, text="Definition goes here", font=("Arial", 18, "italic"),
                            bg="#d0f0fd", fg="#006600", wraplength=400, justify="center")
definition_label.pack()
definition_label.pack_forget()

# Button style settings
button_opts = {
    "width": 16,
    "height": 2,
    "font": ("Arial", 12, "bold"),
    "relief": "raised",
    "bd": 4,
    "cursor": "hand2"
}

# Buttons (row 0)
show_btn = tk.Button(bottom_frame, text="Show Answer", bg="#ffeb3b", fg="black", **button_opts)
show_btn.grid(row=0, column=0, padx=15, pady=10)

next_btn = tk.Button(bottom_frame, text="Next", bg="#4caf50", fg="white", **button_opts)
next_btn.grid(row=0, column=1, padx=15, pady=10)

# Buttons (row 1)
correct_btn = tk.Button(bottom_frame, text="Correct", bg="#2196f3", fg="white", **button_opts)
correct_btn.grid(row=1, column=0, padx=15, pady=10)

incorrect_btn = tk.Button(bottom_frame, text="Incorrect", bg="#f44336", fg="white", **button_opts)
incorrect_btn.grid(row=1, column=1, padx=15, pady=10)

# Run the application
root.mainloop()
