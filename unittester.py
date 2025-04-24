######################################################################
# Author: Hope Michael, Tafreed Sadart
# Username: michaelh, sadart
#
# Assignment: P01: Final Project
#
# Purpose: To test Calculator class methods
######################################################################
# Acknowledgements:
#
# some of the code is originally from: hw10_caesar_cipher_test_suite.py

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
from simple_calculator import *

from inspect import getframeinfo, stack

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def calculator_test_suite():
    """
    A test suite for testing the methods of the calculator class

    NOTE:
    Typically, a test suite for a Class would be written into a second class entirely.
    However, to keep the complexity low, I chose to incorporate the test suite in a familiar way.
    In the future, we will explore how to properly write a test suite as a separate class.
    """

    # Tests encrypting a normal string
    calculator = Calculator()
