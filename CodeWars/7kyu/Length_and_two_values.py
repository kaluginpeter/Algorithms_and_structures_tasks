# Given an integer n and two other values, build an array of size n filled with these two values alternating.
#
# Examples
# 5, true, false     -->  [true, false, true, false, true]
# 10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
# 0, "one", "two"    -->  []
# Good luck!
#
# FUNDAMENTALSARRAYS
# Solution
def alternate(n, first_value, second_value):
    l = []
    while len(l) < n:
        l.append(first_value)
        l.append(second_value)
    return l[:-1] if n % 2 != 0 else l