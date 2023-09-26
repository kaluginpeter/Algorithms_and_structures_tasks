# Task
# Given a string, return if a given letter always appears immediately before another given letter.
#
# Worked Example
# ("he headed to the store", "h", "e") ➞ True
#
# # All occurences of "h": ["he", "headed", "the"]
# # All occurences of "h" have an "e" after it.
# # Return True
#
# ('abcdee', 'e', 'e') ➞ False
#
# # For first "e" we can get "ee"
# # For second "e" we cannot have "ee"
# # Return False
# Examples
# ("i found an ounce with my hound", "o", "u") ➞ True
#
# ("we found your dynamite", "d", "y") ➞ False
# Notes
# All sentences will be given in lowercase.
# FUNDAMENTALSSTRINGS
# Solution
def best_friend(txt, a, b):
    for i in range(len(txt) - 1):
        if txt[i] == a:
            if txt[i + 1] != b:
                return False
    if txt[-1] == a:
        return False
    return True