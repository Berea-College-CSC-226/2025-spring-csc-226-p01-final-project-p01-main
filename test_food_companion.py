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
