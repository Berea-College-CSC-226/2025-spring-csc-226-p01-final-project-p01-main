import requests

def fetch_categories():
    response = requests.get("https://opentdb.com/api_category.php")
    response.raise_for_status()
    return {cat["name"]: cat["id"] for cat in response.json()["trivia_categories"]}

def fetch_questions(amount, category_id, difficulty):
    params = {
        "amount": amount,
        "category": category_id,
        "difficulty": difficulty,
        "type": "multiple"
    }
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    return response.json()["results"]
