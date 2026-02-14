# The code consists of four unique digits (from 0 to 9).
# Tests will call your solution; you should answer with an array of four digits.
# Your input is number of matches (the same digit in the same place) with your previous answer. For the first call input value is -1 (i.e. each new test starts with input -1)
# You have to find the code in 16 calls or less. You are the best. Do it.
#
# For example
# The code is [1, 2, 3, 4]
# 1st call return [1, 3, 4, 5] will give 1 match in next input
# 2nd call return [1, 2, 3, 0] will give 3 matches in next input
# 3rd call return [1, 2, 3, 4] will not give 4 matches in next input, because you're the champion!
#
# P.S.
# If the task seems too difficult, try this game with almost the same rules first.
#
# Algorithms
# Solution
from itertools import permutations

ALL = list(permutations(range(10), 4))
candidates = []
last_guess = None
def guess(matches):
    global candidates, last_guess
    if matches == -1:
        candidates = ALL.copy()
        last_guess = candidates[0]
        return list(last_guess)
    candidates = [
        cand for cand in candidates
        if sum(a == b for a, b in zip(cand, last_guess)) == matches
    ]
    last_guess = candidates[0]
    return list(last_guess)