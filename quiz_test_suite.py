import unittest
from inspect import getframeinfo, stack
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
    ##########################################
    unittest(still_has_questions("A") == "Oops! Wrong answer!")
    unittest(next_questions("B") == "Oops! Wrong answer!")


    ##########################################


def main():
    QuizBrain_suite()


if __name__ == "__main__":
    main()

