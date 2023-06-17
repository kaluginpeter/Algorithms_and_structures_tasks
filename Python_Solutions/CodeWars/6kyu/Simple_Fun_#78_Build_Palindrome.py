# Task
# Given a string str, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
#
# Example
# For str = "abcdc", the output should be "abcdcba".
#
# Input/Output
# [input] string str
#
# A string consisting of lowercase latin letters.
#
# Constraints: 3 ≤ str.length ≤ 10.
#
# [output] a string
#
# PUZZLES
# Solution
def build_palindrome(w):
    n = 0
    while w[n:] != w[n:][::-1]: n += 1
    return w + w[:n][::-1]