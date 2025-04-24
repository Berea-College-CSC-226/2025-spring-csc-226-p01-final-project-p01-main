from inspect import getframeinfo, stack
from data import fetch_questions
from quizbrain import QuizBrain
from questions import Question

def unittest(did_pass):
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        print(f"Test at line {linenum} ok.")
    else:
        print(f"Test at line {linenum} FAILED.")

def QuizBrain_suite():
    # Fetch 5 questions for testing
    raw_questions = fetch_questions(5, 9, "easy")  # Category 9 = General Knowledge

    # Convert to Question objects
    question_list = [
        Question(q["question"], q["incorrect_answers"] + [q["correct_answer"]], q["correct_answer"])
        for q in raw_questions
    ]

    quiz = QuizBrain(question_list)

    # Test still_has_question
    unittest(quiz.still_has_question() == True)

    # Test next_question and check_answer
    q_text, options = quiz.next_question()
    unittest(isinstance(q_text, str))
    unittest(isinstance(options, list))

    correct_answer = quiz.current_question.answer
    unittest(quiz.check_answer(correct_answer) == True)
    unittest(quiz.score == 1)

    # Test incorrect answer
    quiz.next_question()
    unittest(quiz.check_answer("WRONG_ANSWER") == False)

    # Test finishing the quiz
    while quiz.still_has_question():
        quiz.next_question()

    unittest(quiz.still_has_question() == False)

def main():
    QuizBrain_suite()

if __name__ == "__main__":
    main()
