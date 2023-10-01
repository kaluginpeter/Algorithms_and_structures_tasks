# In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.
#
# Solve("*'&ABCDabcde12345") = [4,5,5,3].
# --the order is: uppercase letters, lowercase, numbers and special characters.
# More examples in the test cases.
#
# Good luck!
#
# FUNDAMENTALS
# Solution
def solve(s):
    uc, lc, num, sp = 0, 0, 0, 0
    for i in s:
        if i.isupper(): uc += 1
        elif i.islower(): lc += 1
        elif i.isdigit(): num += 1
        else: sp += 1
    return [uc, lc, num, sp]