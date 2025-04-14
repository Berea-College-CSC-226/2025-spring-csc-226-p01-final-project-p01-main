import final_code
from inspect import getframeinfo, stack
import unittest

from final_game.final_code import Planet, HEIGHT, Rocket


def testing(did_pass):
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

class TestRocketGame(unittest.TestCase):
    def test_planet_info(self):
        planet = Planet("Mars", "The Red Planet.", 400, 460)
        self.assertEqual(planet.get_info(), "Mars: The Red Planet.")

def main():
    #code_test()
main()