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


    ##########################################


def main():
    QuizBrain_suite()


if __name__ == "__main__":
    main()

