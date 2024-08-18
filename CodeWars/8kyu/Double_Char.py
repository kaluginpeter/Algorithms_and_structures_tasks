# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Good Luck!
#
# FUNDAMENTALSSTRINGS
# Solution
def double_char(s):
    double = 2
    return ''.join([char*double for char in s])