# Having two standards for a keypad layout is inconvenient!
# Computer keypad's layout:
# 7 8 9  \n
# 4 5 6  \n
# 1 2 3  \n
#   0 \n
#
# Cell phone keypad's layout:
# 1 2 3\n
# 4 5 6\n
# 7 8 9\n
#   0\n
#
# Solve the horror of unstandardized keypads by providing a function that converts computer input to a number as if it was typed on a phone.
#
# Example:
# "789" -> "123"
#
# Notes:
# You get a string with numbers only
#
# STRINGS
# Solution
def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123456789', '789456123'))