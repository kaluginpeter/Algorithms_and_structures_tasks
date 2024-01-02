# Create a function that takes index [0, 8] and a character. It returns a string with columns. Put character in column marked with index.
#
# Ex.: index = 2, character = 'B'
#
# | | |B| | | | | | |
#  0 1 2 3 4 5 6 7 8
# Assume that argument index is integer [0, 8]. Assume that argument character is string with one character.
#
# FUNDAMENTALSSTRINGS
# Solution
def build_row_text(index, character):
    s: str = ''
    for i in range(9):
        s += f'|{character if index == i else " "}'
    return s + '|'