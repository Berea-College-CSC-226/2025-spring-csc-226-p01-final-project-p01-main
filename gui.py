#################################################################################################
# Author: Fatma
# Username: Fatma Sherif
# assignment: the GUI for the flashcards app
#################################################################################################

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Flashcard App")
root.geometry("400x350")
root.configure(bg="#d0f0fd")  # light blue background

# Layout frames with matching bg
top_frame = tk.Frame(root, bg="#d0f0fd")
top_frame.pack(pady=20)

middle_frame = tk.Frame(root, bg="#d0f0fd")
middle_frame.pack(pady=10)

bottom_frame = tk.Frame(root, bg="#d0f0fd")
bottom_frame.pack(pady=20)

# Term label
term_label = tk.Label(top_frame, text="Term goes here", font=("Arial", 18),
                      bg="#d0f0fd", fg="#004080")  # dark blue text
term_label.pack()

# Definition label (hidden initially)
definition_label = tk.Label(middle_frame, text="Definition goes here", font=("Arial", 14),
                            bg="#d0f0fd", fg="#006600")  # green text
definition_label.pack()
definition_label.pack_forget()

# Buttons
show_btn = tk.Button(bottom_frame, text="Show Answer", bg="#ffeb3b", fg="black", width=15)  # yellow
show_btn.grid(row=0, column=0, padx=15, pady=5)

next_btn = tk.Button(bottom_frame, text="Next", bg="#4caf50", fg="white", width=15)  # green
next_btn.grid(row=0, column=1, padx=15, pady=5)

correct_btn = tk.Button(bottom_frame, text="Correct", bg="#2196f3", fg="white", width=15)  # blue
correct_btn.grid(row=1, column=0, padx=15, pady=10)

incorrect_btn = tk.Button(bottom_frame, text="Incorrect", bg="#f44336", fg="white", width=15)  # red
incorrect_btn.grid(row=1, column=1, padx=15, pady=10)

# Run the application
root.mainloop()
