import requests

category_response = requests.get("https://opentdb.com/api_category.php")
category_response.raise_for_status()
categories = category_response.json()["trivia_categories"]

print("\nAvailable Categories:")
for cat in categories:
    print(f"{cat['id']}: {cat['name']}")

category_ids = [str(cat["id"]) for cat in categories]
category_id = input("\nEnter the ID of the category you'd like to play: ")
while category_id not in category_ids:
    category_id = input("Invalid ID. Please enter a valid category ID: ")
category_id = int(category_id)

num_questions = input("How many questions would you like to play? ")
while not num_questions.isdigit() or int(num_questions) <= 0:
    num_questions = input("Please enter a valid positive number: ")
num_questions = int(num_questions)

difficulty = input("What difficulty would you like to play? (Easy/Medium/Hard): ").lower()
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Please enter a valid difficulty (Easy/Medium/Hard): ").lower()

responses = requests.get("https://opentdb.com/api.php", params={"amount": num_questions, "difficulty": difficulty, "category": category_id})
responses.raise_for_status()
data = responses.json()

question_data = data["results"]