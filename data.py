import requests

responses = requests.get("https://opentdb.com/api.php", params={"amount": 20, "difficulty": "easy"})
responses.raise_for_status()
data = responses.json()

question_data = data["results"]
