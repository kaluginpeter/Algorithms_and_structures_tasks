# Let's create some scrolling text!
#
# Your task is to complete the function which takes a string, and returns an array with all possible rotations of the given string, in uppercase.
#
# Example
# scrollingText("codewars") should return:
#
# [ "CODEWARS",
#   "ODEWARSC",
#   "DEWARSCO",
#   "EWARSCOD",
#   "WARSCODE",
#   "ARSCODEW"
#   "RSCODEWA",
#   "SCODEWAR" ]
# Good luck!
#
# STRINGSARRAYSFUNDAMENTALS
# Solution
def scrolling_text(text):
    lst = []
    for i in range(len(text)):
        lst.append(text.upper())
        text = text[1:] + text[0]
    return lst