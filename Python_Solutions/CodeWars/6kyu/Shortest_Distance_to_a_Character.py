# Given a string s and a character c, return an array of integers representing the shortest distance from the current character in s to c.
#
# Notes
# All letters will be lowercase.
# If the string is empty, return an empty array.
# If the character is not present, return an empty array.
# Examples
# s = "lovecodewars"
# c = "e"
# result = [3, 2, 1, 0, 1, 2, 1, 0, 1, 2, 3, 4]
#
# s = "aaaabbbb"
# c = "b"
# result = [4, 3, 2, 1, 0, 0, 0, 0]
#
# s = ""
# c = "b"
# result = []
#
# s = "abcde"
# c = ""
# result = []
# If you liked it, please rate :D
#
# STRINGSALGORITHMS
# Solution
def shortest_to_char(s, c):
    if not s or not c:return []
    l = [k for k, v in enumerate(s) if v == c]
    if not l: return []
    return [min(abs(i - j) for j in l) for i in range(len(s))]