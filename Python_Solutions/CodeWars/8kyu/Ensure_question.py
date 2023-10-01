# Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, returns the original string.
#
# For example (Input --> Output)
#
# "Yes" --> "Yes?"
# "No?" --> "No?"
# FUNDAMENTALS
# Solution
def ensure_question(s):
    return s if s.endswith('?') else s + '?'