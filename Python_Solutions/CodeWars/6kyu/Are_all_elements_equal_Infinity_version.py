# Task
# Create a function eq_all that determines if all elements of any iterable are equal; the iterable may be infinite. Return value is a bool.
#
# Examples
# eq_all('aaa')   : True
# eq_all('abc')   : False
# eq_all('')      : True
#
# eq_all([0,0,0]) : True
# eq_all([0,1,2]) : False
# eq_all([])      : True
# Notes
# For the function result to be True, the iterable must be finite; False, however, can result from an element finitely far from the left end. There will be no tests with infinite series of equal elements.
# Elements will be primitive values.
#
# FUNDAMENTALS
# Solution
def eq_all(iterable):
    if not iterable:
        return True
    d: dict = {}
    for i in iterable:
        d[i] = d.get(i, 0) + 1
        if len(d) > 1:
            return False
    return True