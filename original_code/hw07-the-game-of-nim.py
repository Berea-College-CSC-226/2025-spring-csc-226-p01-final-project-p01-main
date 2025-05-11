######################################################################
# Author: Dr. Scott Heggen             TODO: Change this to your names
# Username: heggens                    TODO: Change this to your usernames
#
# Assignment: HW07: The Game of Nim
#
# Purpose:  Some functions to play around with and understand return values
#           This function sings you the willaby wallaby children's song
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by Raffi: https://www.youtube.com/watch?v=sOOZQZlxxC4
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


def willoughby_wallaby(name):
    """
    A function that converts the first letter(s) of your name to a "W"

    :param name: Your name
    :return: Your name, with the first one or two letters replaced with a "W"
    """

    # A list of all the likely consonant blends
    consonant_blends = ["bl", "br", "ch", "ck", "cl", "cr",
                        "dr", "fl", "fr", "gh", "gl", "gr",
                        "ng", "ph", "pl", "pr", "qu", "sc",
                        "sh", "sk", "sl", "sm", "sn", "sp",
                        "st", "sw", "th", "tr", "tw", "wh", "wr"]

    if name[0:2].lower() in consonant_blends:   # if the first two letters are in the list above
        new_name = "W" + name[2:]               # Replace the first two letters
    else:
        new_name = "W" + name[1:]               # Else just replace the first letter
    return new_name                             # Return the modified name


def main():
    """
    A fun little program that sings the Willoughby Wallaby children's song.

    :return: None
    """

    your_name = ""
    while your_name != "STOP":
        your_name = input("What's your name (Enter STOP to stop the program)?\n")
        if your_name == "STOP":
            break
        w_name = willoughby_wallaby(your_name)
        print("Willaby, Wallaby " + w_name)
        print("An elephant sat on " + your_name + "!")


if __name__ == "__main__":
    main()
######################################################################
# Author: Dr. Scott Heggen             TODO: Change this to your names
# Username: heggens                    TODO: Change this to your usernames
#
# Assignment: HW07: The Game of Nim
#
# Purpose: This program is designed to demonstrate the use of Python's string capabilities
# as a method for peeling digits from an integer
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random


def peel_digits(num):
    """
    Given a positive integer num, peel_digits returns a list filled with the digits
    eg. given 1984, peel_digits returns the list [1, 9, 8, 4]
    :param num: an integer to peel into a list of digits
    :return: A list where each element of the list is a digit from num
    """
    str_num=str(num)                # convert to string to utilize Python's strong string features
    digit_list=[]                   # create empty list

    while len(str_num) > 0:         # Notice this is slightly different than last time you saw this function
        digit_list.append(int(str_num[0]))          #Puts each digits into list
        str_num = str_num[1:]
    return digit_list


def print_digits(digit_list): # takes a Python list as input
    """
    Given any Python list, this function prints each list element

    :param digit_list: a list where each element of the list is a digit from a larger number
    :return: None
    """
    print("\nDigits:")
    for digit in digit_list:
        print("\t",digit)
    # This function does not have a return, so it is not fruitful. It's job is to print()


def main():
    """
    This main function is intended to display the capabilities of the peel_digits() and print_digit() functions

    :return: None
    """

    year = random.randint(0, 2018)
    print("\nYear = "+ str(year))
    year_list = peel_digits(year)   # put list returned from function into year_list
    print_digits(year_list)


main()
