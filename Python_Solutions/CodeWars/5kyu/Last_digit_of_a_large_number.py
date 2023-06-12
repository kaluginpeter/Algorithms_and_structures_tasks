# Define a function that takes in two non-negative integers
# b and returns the last decimal digit of
# You may assume that the input will always be valid.
# Examples
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6
# Remarks
# JavaScript, C++, R, PureScript, COBOL
# Since these languages don't have native arbitrarily large integers,
# your arguments are going to be strings representing non-negative integers instead.
# Soltuion
def last_digit(n1, n2):
    return pow(n1, n2, 10)