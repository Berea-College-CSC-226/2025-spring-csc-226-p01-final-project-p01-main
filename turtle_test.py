from inspect import getframeinfo, stack
import time
from turtle import TurtleObject
import time

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
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_game_suite():
    """
    Test suite for TurtleObject and game_timer.
    """
    print("\nRunning test_game_suite().")

    # 1. Test is_clicked() inside turtle bounds
    turtle = TurtleObject()
    turtle.x, turtle.y = 100, 100
    turtle.visible = True
    unittest(turtle.is_clicked((110, 110)) == True)  # inside bounds

    # 2. Test is_clicked() outside turtle bounds
    unittest(turtle.is_clicked((221, 221)) == False)  # outside bounds

    # 3. Test is_clicked() when invisible
    turtle.visible = False
    unittest(turtle.is_clicked((110, 110)) == False)

    # 4. Test move() updates position
    old_x, old_y = turtle.x, turtle.y
    turtle.visible = False
    turtle.move()
    unittest((turtle.x != old_x or turtle.y != old_y) and turtle.visible == True)


# Run the suite
if __name__ == "__main__":
    test_game_suite()
