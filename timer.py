# Most of the code is in Naz's branch, we are just working in here and adding little elements into our game

import time

def game_timer(start_time, duration=20):
    """Check if the timer has expired."""
    current_time = time.time()
    elapsed = current_time - start_time
    return elapsed >= duration





