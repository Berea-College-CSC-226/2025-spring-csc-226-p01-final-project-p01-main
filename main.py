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
# Additional help from Google and AI was used to brainstorm structure,
# organize class responsibilities, and write boilerplate code.
#####################################################################
# food_companion.py
import json
from food_companion import Recipe, RecipeCollection, MealPlanner, ShoppingList

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

def suggest_recipes_by_ingredients(recipe_collection, user_ingredients):
    scores = []
    for recipe in recipe_collection.recipes:
        match_count = sum(1 for ing in recipe.ingredients if ing.lower() in user_ingredients)
        if match_count > 0:
            scores.append((match_count, recipe))
    scores.sort(reverse=True, key=lambda x: x[0])
    return [r for score, r in scores]

def display_menu():
    print("\n== Food Companion Menu ==")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. Plan a Meal")
    print("4. View Meal Plan")
    print("5. Generate Shopping List")
    print("6. Suggest Recipes by Ingredients")
    print("7. View Calories for a Recipe")
    print("8. Save and Exit")

def main():
    recipe_collection = RecipeCollection()
    recipe_collection.recipes = load_recipes_from_file()
    meal_planner = MealPlanner()
    shopping_list = ShoppingList()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Recipe name: ")
            ingredients = input("Ingredients (comma separated): ").split(",")
            instructions = input("Instructions (semicolon separated): ").split(";")
            servings = int(input("Servings: "))
            recipe = Recipe(name.strip(), [i.strip() for i in ingredients], [i.strip() for i in instructions], servings)
            recipe_collection.add_recipe(recipe)
            print("Recipe added.")

        elif choice == "2":
            for r in recipe_collection.recipes:
                print(r)

        elif choice == "3":
            day = input("Enter day (e.g. Monday): ")
            meal = input("Meal type (breakfast/lunch/dinner): ")
            name = input("Recipe name to plan: ")
            recipe = recipe_collection.get_recipe(name)
            if recipe:
                meal_planner.plan_meal(day, meal, recipe)
                print(f"{meal} planned for {day}.")
            else:
                print("Recipe not found.")

        elif choice == "4":
            day = input("Enter day to view: ")
            plan = meal_planner.get_plan_for_day(day)
            if plan:
                for meal, recipe in plan.items():
                    print(f"{meal.capitalize()}: {recipe.name}")
            else:
                print("No meals planned for this day.")

        elif choice == "5":
            items = meal_planner.generate_shopping_list()
            print("Shopping List:")
            for item in items:
                print(f"- {item}")

        elif choice == "6":
            user_input = input("Enter ingredients you have (comma separated): ")
            user_ingredients = [i.strip().lower() for i in user_input.split(',')]
            suggestions = suggest_recipes_by_ingredients(recipe_collection, user_ingredients)
            if suggestions:
                print("Top Recipe Suggestions:")
                for r in suggestions[:3]:
                    matched = sum(1 for i in r.ingredients if i.lower() in user_ingredients)
                    print(f"- {r.name} ({matched} matched ingredients)")
            else:
                print("No matching recipes found.")

        elif choice == "7":
            name = input("Enter recipe name to check calories: ")
            recipe = recipe_collection.get_recipe(name)
            if recipe:
                print(f"Total estimated calories: {recipe.calculate_nutrition()} kcal")
            else:
                print("Recipe not found.")

        elif choice == "8":
            save_recipes_to_file(recipe_collection)
            print("Recipes saved. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()