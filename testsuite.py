from game.py import *

from inspect import getframeinfo, stack

def unittest(did_pass):

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def turn_switcher_test():
    pass

def game_won_test():
    pass

def select_piece_test():
    pass

def move_piece_test():
    pass

def make_piece_king_test():
    pass






turn_switcher_test()
game_won_test()
select_piece_test()
move_piece_test()
make_piece_king_test()

