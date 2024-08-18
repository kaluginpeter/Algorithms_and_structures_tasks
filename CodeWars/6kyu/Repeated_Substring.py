# For a given nonempty string s find a minimum substring t and the maximum number k,
# such that the entire string s is equal to t repeated k times.
#
# The input string consists of lowercase latin letters.
#
# Your function should return :
#
# a tuple (t, k) (in Python)
# an array [t, k] (in Ruby and JavaScript)
# in C, return k and write to the string t passed in parameter
# Example #1:
#
# for string
#
# s = "ababab";
# the answer is
#
# ("ab", 3)
# Example #2:
#
# for string
#
# s = "abcde"
# the answer is
#
# ("abcde", 1)
# because for this string "abcde" the minimum substring t, such that s is t repeated k times, is itself.
#
# ALGORITHMS
# Solution
def f(s):
    c = min([s.count(i) for i in s])
    w = ''
    for i in s:
        w += i
        if w * c == s: return (w, c)
    return (s, 1)