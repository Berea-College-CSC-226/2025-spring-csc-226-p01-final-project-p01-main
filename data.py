import requests

def fetch_categories():
    """
    Get trivia question from the Open Trivia Database API.

    :return: json objects of the question
    """
    response = requests.get("https://opentdb.com/api_category.php")
    response.raise_for_status()
    return {cat["name"]: cat["id"] for cat in response.json()["trivia_categories"]}

def fetch_questions(amount, category_id, difficulty):
    """
    Get trivia question from the Open Trivia Database API.

    :param amount: Numbers of question
    :param category_id: Which category to use
    :param difficulty: The difficulty level
    :return: A list of question data
    """
    params = {
        "amount": amount,
        "category": category_id,
        "difficulty": difficulty,
        "type": "multiple"
    }
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    return response.json()["results"]
