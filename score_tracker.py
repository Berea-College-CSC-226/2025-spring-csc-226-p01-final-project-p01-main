def load_scores(filename="score_log.txt"):
    try:
        with open(filename, "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
        return scores
    except FileNotFoundError:
        return []

def display_scores(scores):
    if not scores:
        print("No scores recorded yet.")
        return

    print("All Scores:")
    for i, score in enumerate(scores, 1):
        print(f"Game {i}: {score}")

    print(f"\nHighest Score: {max(scores)}")
    print(f"Average Score: {sum(scores) / len(scores):.2f}")

if __name__ == "__main__":
    scores = load_scores()
    display_scores(scores)
