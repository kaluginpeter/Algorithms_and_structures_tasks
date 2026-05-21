# Delta Generators
# In mathematics, the symbols Δ and d are often used to denote the difference between two values. Similarly, differentiation takes the ratio of changes (ie. dy/dx) for a linear relationship. This method can be applied multiple times to create multiple 'levels' of rates of change. (A common example is x (position) -> v (velocity) -> a (acceleration)).
#
# Today we will be creating a similar concept. Our function delta will take a sequence of values and a positive integer level, and return a sequence with the 'differences' of the original values. (Differences here means strictly b - a, eg. [1, 3, 2] => [2, -1]) The argument level is the 'level' of difference, for example acceleration is the 2nd 'level' of difference from position. The specific encoding of input and output lists is specified below.
#
# The example below shows three different 'levels' of the same input.
#
# input = [1, 2, 4, 7, 11, 16, 22]
# list(delta(input, 1)) # [1, 2, 3, 4, 5, 6]
# list(delta(input, 2)) # [1, 1, 1, 1, 1]
# list(delta(input, 3)) # [0, 0, 0, 0]
# We do not assume any 'starting value' for the input, so the output for each subsequent level will be one item shorter than the previous (as shown above).
# If an infinite input is provided, then the output must also be infinite.
#
# Input/Output encoding
# Input and output can be any, possibly infinite, iterable. Possibilities include finite lists and possibly infinite generator objects, but any iterable must be accepted as input and is acceptable as output.
#
# Difference implementation
# delta must work for iterables of any objects/types that implement __sub__ (eg int, float, set, etc).
# Additional Requirements/Notes:
# delta must work for inputs which are infinite
# values will always be valid, and will always produce consistent classes/types of object
# level will always be valid, and 1 <= level <= 400
# Additional examples:
# def count():
#     c = 0
#     while True:
#         yield c
#         c += 1
#
# # count() => [0, 1, 2, 3, 4, ...]
# delta(count(), 1) # [1, 1, 1, 1, ...]
# delta(count(), 2) # [0, 0, 0, 0, ...]
#
#
# def cosine():
#     c = 0
#     while True:
#         yield [1, 0, -1, -1, 0, 1][c]
#         c = (c+1)%6
#
# # cosine() => [1, 0, -1, -1, 0, 1, 1, 0, ...]
# delta(cosine(), 1) # [-1, -1, 0, 1, 1, 0, -1, ...]
# delta(cosine(), 2) # [0, 1, 1, 0, -1, -1, 0, ...]
# delta(cosine(), 3) # [1, 0, -1, -1, 0, 1, 1, 0, ...]
#
#
# input = [set([6, 2, 'A']), set([2, 'B', 8]), set(['A', 'B'])]
#
# delta(input, 1) # [{8, 'B'}, {'A'}]
# delta(input, 2) # [{'A'}]
# IteratorsRecursion
# Solution
from itertools import tee


def delta(values, n):
    if n == 0:
        yield from values
        return
    a, b = tee(values)
    next(b, None)
    diffs = (y - x for x, y in zip(a, b))
    if n == 1: yield from diffs
    else: yield from delta(diffs, n - 1)