from questions import Question
from quizbrain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    q_options = [question["correct_answer"]] + question["incorrect_answers"]
    q_object = Question(question["question"], q_options, question["correct_answer"])
    question_bank.append(q_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"Your final score is: {quiz.score}/{quiz.question_number}")
