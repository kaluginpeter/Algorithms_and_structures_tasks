# Well, those numbers were right and we're going to feed their ego.
#
# Write a function, isNarcissistic, that takes in any amount of numbers and returns true if all the numbers are narcissistic. Return false for invalid arguments (numbers passed in as strings are ok).
#
# For more information about narcissistic numbers (and believe me, they love it when you read about them) follow this link: https://en.wikipedia.org/wiki/Narcissistic_number
#
# ALGORITHMSMATHEMATICS
# Solution
def is_narcissistic(*args):
    for n in args:
        if not str(n).isdigit(): return False
        b: int = len(str(n))
        top: int = 0
        for i in str(n):
            top += int(i) ** b
        if top != int(n):
            return False
    return True