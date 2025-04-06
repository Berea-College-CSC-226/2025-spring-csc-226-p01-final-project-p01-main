import unittest
from inspect import getframeinfo, stack

from data import question_data
from quizbrain import *
from questions import *

import sys



def unittest(did_pass):
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def QuizBrain_suite():
    quiz = QuizBrain(question_data)

    ##########################################
    # Test still_has_question
    unittest(quiz.still_has_question() == True)

    # Test next_question increment
    quiz.next_question = lambda: None  # Mock to bypass input
    current_number = quiz.question_number
    quiz.next_question()
    unittest(quiz.question_number == current_number + 1)

    # Test correct answer
    quiz.question_number = 0
    quiz.check_answer("Paris", "Paris")
    unittest(quiz.score == 1)

    # Test incorrect answer
    quiz.question_number = 1
    quiz.check_answer("5", "4")
    unittest(quiz.score == 1)  # Score should not change


    ##########################################


def main():
    QuizBrain_suite()


if __name__ == "__main__":
    main()

