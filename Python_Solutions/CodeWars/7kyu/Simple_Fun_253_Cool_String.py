# Task
# Let's call a string cool if it is formed only by Latin letters and no two lowercase and no two uppercase letters are in adjacent positions. Given a string, check if it is cool.
#
# Input/Output
# [input] string s
#
# A string that contains uppercase letters, lowercase letters numbers and spaces.
#
# 1 ≤ s.length ≤ 20.
#
# [output] a boolean value
#
# true if s is cool, false otherwise.
#
# Example
# For s = "aQwFdA", the output should be true
#
# For s = "aBC", the output should be false;
#
# For s = "AaA", the output should be true;
#
# For s = "q q", the output should be false.
#
# FUNDAMENTALS
# Solution
def cool_string(s):
    return all(i.isalpha() for i in s) and all(i.isupper() and j.islower() if i.isupper() else i.islower() and j.isupper() for i,j in zip(s, s[1:]))