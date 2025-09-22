# All you have to do is use your cheating talent to pass this kata.
#
# Puzzles
# Solution
import random

def solution() -> int:
    state = random.getstate()
    temp = random.Random()
    temp.setstate(state)
    return temp.randint(0, 1000)