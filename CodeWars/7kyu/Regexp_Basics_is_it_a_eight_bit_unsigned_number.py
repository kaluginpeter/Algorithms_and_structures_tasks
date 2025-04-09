# Implement String#eight_bit_number?, which should return true if given object is a number representable by 8 bit unsigned integer (0-255), false otherwise.
#
# It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.
#
# Regular ExpressionsFundamentals
# Solution
def eight_bit_number(n):
    return bool(n) and n.isdigit() and 0 <= int(n) <= 255 and not n.startswith('+') and not (n.startswith('0') and len(n) > 1)