# Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
#
# REGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def is_digit(n):
    return n in '0123456789' and n != ''