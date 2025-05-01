######################################################################
# Author: Kamau Clark
# Username: clarkk2
#
# Assignment: Final Project
#
# Purpose:
# This project demonstrates mastery of Python classes, inheritance,
# file handling, dictionaries, and graphical user interfaces (GUIs).
# Inspired by the Teamwork 2 (T12: Events and GUIs) assignment and
# the EventGuru concept, this app allows users to create, view, and
# manage recipes, plan meals, track calories, and receive smart
# AI-based suggestions through a fully interactive Tkinter interface.
#
######################################################################
# Acknowledgements:
# I’d like to thank my instructors, TAs, and classmates for their
# guidance throughout the semester. This project is influenced by
# the T12 assignment structure and builds on the t12_tkinter.py example.
#
# I also used Google, Python documentation, and AI tools to help
# brainstorm structure, polish the GUI design, and write supporting code in all honesty.
######################################################################
from ttkthemes import ThemedTk
from tkinter import ttk, messagebox, simpledialog
from PIL import ImageTk, Image
from food_companion import Recipe, RecipeCollection, MealPlanner
import json, os
import tkinter as tk

def save_recipes_to_file(recipe_collection, filename="recipes.json"):
    with open(filename, "w") as f:
        json.dump([vars(r) for r in recipe_collection.recipes], f, indent=4)

def load_recipes_from_file(filename="recipes.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Recipe(d["name"], d["ingredients"], d["instructions"], d["servings"]) for d in data]
    except FileNotFoundError:
        return []

recipes = RecipeCollection()
recipes.recipes = load_recipes_from_file()
planner = MealPlanner()

root = ThemedTk(theme="arc")
root.title("Food Companion")
root.geometry("600x750")
root.configure(bg="#fdf2f2")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11), background="#fdf2f2")
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), background="#fdf2f2")

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill='both', expand=True)

if os.path.exists("logo.png"):
    logo_img = Image.open("logo.png").resize((120, 120))
    logo_photo = ImageTk.PhotoImage(logo_img)
    ttk.Label(main_frame, image=logo_photo).pack(pady=10)

ttk.Label(main_frame, text="Food Companion", style="Header.TLabel").pack(pady=5)

def plan_direct(recipe=None):
    if recipe is None:
        recipe_name = simpledialog.askstring("Plan a Meal", "Enter recipe name to plan:")
        recipe = recipes.get_recipe(recipe_name)
        if recipe is None:
            messagebox.showerror("Error", "Recipe not found.")
            return
    day = simpledialog.askstring("Meal Planner", "Which day?")
    meal = simpledialog.askstring("Meal Type", "Which meal? (breakfast/lunch/dinner)")
    if day and meal:
        planner.plan_meal(day, meal, recipe)
        messagebox.showinfo("Planned", f"{recipe.name} planned for {meal} on {day}")

def view_meal_plan_gui():
    win = tk.Toplevel(root)
    win.title("Meal Plan Viewer")
    for day, meals in planner.weekly_plan.items():
        ttk.Label(win, text=f"{day}:", font=("Segoe UI", 12, "bold")).pack(pady=4)
        total_cal = 0
        for meal, recipe in meals.items():
            if recipe is not None:
                cal = recipe.calculate_nutrition()
                total_cal += cal
                ttk.Label(win, text=f" - {meal.title()}: {recipe.name} ({cal} kcal)").pack(anchor="w", padx=15)
        ttk.Label(win, text=f" Total for {day}: {total_cal} kcal").pack(pady=2)

def add_recipe_gui():
    def submit():
        name = name_entry.get()
        ingredients = [i.strip() for i in ingredients_entry.get().split(",")]
        instructions = [i.strip() for i in instructions_entry.get().split(";")]
        try:
            servings = int(servings_entry.get())
            r = Recipe(name, ingredients, instructions, servings)
            recipes.add_recipe(r)
            messagebox.showinfo("Success", "Recipe added!")
            win.destroy()
        except ValueError:
            messagebox.showerror("Error", "Servings must be a number.")

    win = tk.Toplevel(root)
    win.title("Add Recipe")
    for label in ["Name", "Ingredients (comma separated)", "Instructions (semicolon separated)", "Servings"]:
        ttk.Label(win, text=label).pack()
        ttk.Entry(win, name=label.split()[0].lower() + "_entry").pack()

    name_entry = win.children["name_entry"]
    ingredients_entry = win.children["ingredients_entry"]
    instructions_entry = win.children["instructions_entry"]
    servings_entry = win.children["servings_entry"]
    ttk.Button(win, text="Submit", command=submit).pack(pady=10)

def view_recipes_gui():
    win = tk.Toplevel(root)
    win.title("All Recipes")

    canvas = tk.Canvas(win)
    scroll_y = ttk.Scrollbar(win, orient="vertical", command=canvas.yview)
    frame = ttk.Frame(canvas)

    canvas.configure(yscrollcommand=scroll_y.set)
    scroll_y.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>", on_frame_configure)

    for r in recipes.recipes:
        recipe_frame = ttk.Frame(frame, padding=10)
        recipe_frame.pack(padx=10, pady=5, fill="x")

        container = ttk.Frame(recipe_frame)
        container.pack(anchor="w", fill="x")

        base_name = r.name.lower().replace(" ", "_")
        img_path = None
        for ext in [".png", ".jpg"]:
            test_path = f"{base_name}{ext}"
            if os.path.exists(test_path):
                img_path = test_path
                break

        if img_path:
            try:
                img = Image.open(img_path).resize((100, 80))
                photo = ImageTk.PhotoImage(img)
                lbl = ttk.Label(container, image=photo)
                lbl.image = photo
                lbl.pack(side="left", padx=5)
            except:
                pass

        text_frame = ttk.Frame(container)
        text_frame.pack(side="left", fill="both", expand=True)

        ttk.Label(text_frame, text=str(r)).pack(anchor="w")
        ttk.Button(text_frame, text="Plan", command=lambda r=r: plan_direct(r)).pack(side="left", padx=4)
        ttk.Button(text_frame, text="Calories", command=lambda r=r: messagebox.showinfo("Calories", f"{r.calculate_nutrition()} kcal")).pack(side="left")

def suggest_recipes_gui():
    def suggest():
        ingredients = [i.strip().lower() for i in input_entry.get().split(",")]
        matches = []
        for r in recipes.recipes:
            match_count = sum(1 for i in r.ingredients if i.lower() in ingredients)
            if match_count > 0:
                matches.append((match_count, r))
        matches.sort(reverse=True, key=lambda x: x[0])
        display_matches(matches[:5])

    def display_matches(matches):
        for widget in results_frame.winfo_children():
            widget.destroy()
        if not matches:
            ttk.Label(results_frame, text="No matches found.").pack()
            return
        for count, r in matches:
            box = ttk.Frame(results_frame, padding=6)
            box.pack(pady=6, fill="x")
            ttk.Label(box, text=f"{r.name} ({count} matched)", font=("Segoe UI", 11, "bold")).pack(anchor="w")
            ttk.Button(box, text="Calories", command=lambda r=r: messagebox.showinfo("Calories", f"{r.calculate_nutrition()} kcal")).pack(anchor="w")
            ttk.Button(box, text="Plan This", command=lambda r=r: plan_direct(r)).pack(anchor="w")

    win = tk.Toplevel(root)
    win.title("Smart AI Suggestion")
    ttk.Label(win, text="Enter ingredients (comma separated):").pack()
    input_entry = ttk.Entry(win)
    input_entry.pack()
    ttk.Button(win, text="Search", command=suggest).pack(pady=4)
    results_frame = ttk.Frame(win)
    results_frame.pack(pady=10)

def view_calories_gui():
    def check():
        r = recipes.get_recipe(entry.get())
        if r:
            result.config(text=f"Calories: {r.calculate_nutrition()} kcal")
        else:
            result.config(text="Recipe not found.")
    win = tk.Toplevel(root)
    win.title("Calories")
    ttk.Label(win, text="Enter Recipe Name").pack()
    entry = ttk.Entry(win)
    entry.pack()
    ttk.Button(win, text="Check", command=check).pack()
    result = ttk.Label(win, text="")
    result.pack(pady=6)

def save_and_exit():
    save_recipes_to_file(recipes)
    root.quit()

btns = [
    ("Add Recipe", add_recipe_gui),
    ("View Recipes", view_recipes_gui),
    ("Plan a Meal", lambda: plan_direct()),
    ("View Meal Plan", view_meal_plan_gui),
    ("Smart AI Suggestion", suggest_recipes_gui),
    ("Check Calories", view_calories_gui),
    ("Save and Exit", save_and_exit),
]
for text, cmd in btns:
    ttk.Button(main_frame, text=text, command=cmd).pack(fill='x', pady=6)

root.mainloop()