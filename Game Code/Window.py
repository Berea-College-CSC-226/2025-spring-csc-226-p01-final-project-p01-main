# Import tkinter and subprocess
import tkinter as tk
import subprocess

def launch_turtle_game():
    subprocess.Popen(["python", "Test code.py"])

def launch_pos_system():
    subprocess.Popen(["python", "POS_System.py"])

# Create the main window
root = tk.Tk()
root.title("Game Launcher")
root.geometry("800x500")
root.configure(bg="lightblue")

# Add a label
label = tk.Label(root, text="Choose a Program", font=("Cambria UI", 16), bg="lightblue")
label.pack(pady=20)

# Button to launch Turtle Game
btn_turtle = tk.Button(root, text="Play Turtle Catch", font=("Segoe UI", 12), command=launch_turtle_game, width=20)
btn_turtle.pack(pady=5)

# Button to launch POS System
btn_pos = tk.Button(root, text="Open POS System", font=("Segoe UI", 12), command=launch_pos_system, width=20)
btn_pos.pack(pady=5)

# Run the launcher window
root.mainloop()
