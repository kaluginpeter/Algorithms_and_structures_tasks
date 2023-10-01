# Confusion, perplexity, a mild headache. These are just a sample of the things you have experienced in the last few minutes while trying to figure out what is going on in your code.
#
# The task is very simple: accept a list of values, and another value n, then return a new list with every value multiplied by n. For example, [1, 2, 3] and 4 should result in [4, 8, 12].
#
# While writing the function, you even added some debugging lines to make sure that you didn't mess anything up, and everything looked good! But for some reason when you run the function it always seems to return an empty list, even though you can clearly see, that the list should have the right values in it! Somehow, the values are simply disappearing! Is this a bug in the programming language itself...?
#
# DEBUGGINGREFACTORING
# Solution
def mul_by_n(lst, n):
    return [i * n for i in lst]