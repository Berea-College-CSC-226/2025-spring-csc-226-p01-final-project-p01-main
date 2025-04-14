######################################################################
# Author: Kamau Clark
# Username: clarkk2
#
# Assignment: Final Project
#
# Purpose: Learn about classes, inheritance, and Dictionaries
#####################################################################
# Acknowledgements:
# I acknowledge the help of my instructors, TAs, and classmates for
# their guidance throughout the course. I also used class examples
# and Python documentation as references while building this project.
#
# Additional help from ChatGPT was used to brainstorm structure,
# organize class responsibilities, and write boilerplate code.
#####################################################################
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
        # Placeholder for future nutritional info
        pass


class RecipeCollection:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        self.recipes = [r for r in self.recipes if r.name != recipe_name]

    def get_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe
        return None


class MealPlanner:
    def __init__(self):
        # Plan format: {'Monday': {'lunch': recipe1, 'dinner': recipe2}, ...}
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
        return list(set(all_ingredients))  # Remove duplicates


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


