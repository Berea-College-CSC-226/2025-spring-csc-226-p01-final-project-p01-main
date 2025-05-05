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
# test_food_companion.py

import unittest
from food_companion import Recipe, RecipeCollection, MealPlanner

class TestRecipeSystem(unittest.TestCase):
    def test_add_and_get_recipe(self):
        recipe = Recipe("PB&J", ["bread", "peanut butter", "jelly"], ["Spread peanut butter", "Spread jelly", "Combine"], 1)
        collection = RecipeCollection()
        collection.add_recipe(recipe)
        retrieved = collection.get_recipe("PB&J")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.name, "PB&J")

    def test_plan_meal_and_generate_list(self):
        recipe = Recipe("Pasta", ["noodles", "sauce"], ["Boil", "Mix"], 2)
        planner = MealPlanner()
        planner.plan_meal("Monday", "dinner", recipe)
        ingredients = planner.generate_shopping_list()
        self.assertIn("noodles", ingredients)
        self.assertIn("sauce", ingredients)

if __name__ == '__main__':
    unittest.main()