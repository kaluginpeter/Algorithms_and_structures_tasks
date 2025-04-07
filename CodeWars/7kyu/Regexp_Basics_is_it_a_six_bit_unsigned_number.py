# Implement String#six_bit_number?, which should return true if given object is a number representable by 6 bit unsigned integer (0-63), false otherwise.
#
# It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.
#
# Regular ExpressionsFundamentals
# Solution
def six_bit_number(n):
    return bool(n) and n.isdigit() and str(int(n)) == n and 0 <= int(n) < 64