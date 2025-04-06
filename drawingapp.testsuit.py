######################################################################
# Author: Dumisani Chikomo, Dingani Munsaka and Abdou Diop
# Username: chikomod, munsakad, diopa
#
# Assignment: Drawing App GUI Test Suite
# Purpose: Test suite to test the DrawingApp class in the GUI drawing app.
#
######################################################################
# Acknowledgements: Dr Heggen's test suite templates
#   My partners: Dingani Munsaka and Abdou Diop
#   Inspiration: Dr. Heggen and Dr. Jan Pearce
######################################################################

import tkinter as tk
from drawing_app import DrawingApp  # Replace with the correct filename if needed
from inspect import getframeinfo, stack


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test result
    :return: None
    """
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = f"Test at line {linenum} ok."
    else:
        msg = f"Test at line {linenum} FAILED."
    print(msg)


def test_widget_creation():
    """
    Tests the creation of essential widgets in DrawingApp
    """
    app = DrawingApp("Test Window")

    # Test if root is a Tk instance
    unittest(isinstance(app.root, tk.Tk))

    # Test if textbox and label string var are initialized
    app.create_textbox1()
    app.create_label1("Test Label")

    unittest(isinstance(app.myTextBox1, tk.Text))
    unittest(isinstance(app.myTextLabel1Text, tk.StringVar))
    unittest(app.myTextLabel1Text.get() == "Test Label")


def main():
    test_widget_creation()


if __name__ == "__main__":
    main()
