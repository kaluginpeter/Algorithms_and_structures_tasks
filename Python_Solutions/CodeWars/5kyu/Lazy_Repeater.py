# The makeLooper() function (make_looper in Python) takes a string (of non-zero length) as an argument. It returns a function. The function it returns will return successive characters of the string on successive invocations. It will start back at the beginning of the string once it reaches the end.
#
# For example:
#
# abc = make_looper('abc')
# abc() # should return 'a' on this first call
# abc() # should return 'b' on this second call
# abc() # should return 'c' on this third call
# abc() # should return 'a' again on this fourth call
# ITERATORSALGORITHMS
# Solution
from itertools import cycle
def make_looper(string):
    x = cycle(string)
    return lambda: next(x)