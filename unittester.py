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
    caesar = CaesarCipher("encrypt")
    caesar.key = 3
    caesar.message = "A test string"
    caesar.encrypt()
    unittest(caesar.cipher == "D WHVW VWULQJ")

    # Tests encrypting a string with punctuation
    caesar.key = 13
    caesar.message = "It's a so-so kind of day!"
    caesar.encrypt()
    unittest(caesar.cipher == "VG'F N FB-FB XVAQ BS QNL!")

    #Tests encrypting a string with negative key
    caesar.key = -23
    caesar.message = "A test string"
    caesar.encrypt()
    unittest(caesar.cipher == "D WHVW VWULQJ")

    # Tests decrypting a normal string
    caesar.key = 3
    caesar.cipher = "D WHVW VWULQJ"
    caesar.crypt_type = "decrypt"
    caesar.decrypt()
    unittest(caesar.message == "A TEST STRING")

    # Tests decrypting a string with punctuation
    caesar.key = 6
    caesar.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"
    caesar.decrypt()
    unittest(caesar.message == "IT'S A SO-SO KIND OF DAY!")

    # Tests decrypting a string with negative key
    caesar.key = -20
    caesar.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"
    caesar.decrypt()
    unittest(caesar.message == "IT'S A SO-SO KIND OF DAY!")


CaesarCipher_test_suite()
