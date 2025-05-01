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
# food_companion.py
class Recipe:
    def __init__(self, name, ingredients, instructions, servings):
        self.name = name
        self.ingredients = ingredients  # list of strings
        self.instructions = instructions  # list of steps
        self.servings = servings

    def __str__(self):
        return f"{self.name} ({self.servings} servings)\nIngredients: {', '.join(self.ingredients)}\nInstructions: {len(self.instructions)} steps"

    def calculate_nutrition(self):
        # Basic hardcoded calorie dictionary (expandable)
        calories_db = {
            "egg": 78,
            "bread": 80,
            "peanut butter": 94,
            "jelly": 56,
            "chicken": 165,
            "rice": 206,
            "noodles": 221,
            "sauce": 70,
            "lettuce": 5,
            "tomato": 22,
            "cheese": 113,
        }
        total = 0
        for item in self.ingredients:
            item = item.lower().strip()
            total += calories_db.get(item, 50)  # Default 50 if unknown
        return total


class RecipeCollection:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        self.recipes = [r for r in self.recipes if r.name != recipe_name]

    def get_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                return recipe
        return None


class MealPlanner:
    def __init__(self):
        self.weekly_plan = {}

    def plan_meal(self, day, meal_type, recipe):
        if day not in self.weekly_plan:
            self.weekly_plan[day] = {}
        self.weekly_plan[day][meal_type] = recipe

    def get_plan_for_day(self, day):
        return self.weekly_plan.get(day, {})

    def generate_shopping_list(self):
        all_ingredients = []
        for day in self.weekly_plan.values():
            for recipe in day.values():
                all_ingredients.extend(recipe.ingredients)
        return list(set(all_ingredients))


class ShoppingList:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def display(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")