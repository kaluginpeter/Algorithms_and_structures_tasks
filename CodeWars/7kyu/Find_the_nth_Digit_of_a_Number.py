# Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).
#
# Note
# If num is negative, ignore its sign and treat it as a positive value
# If nth is not positive, return -1
# Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0
# Examples(num, nth --> output)
# 5673, 4 --> 5
# 129, 2 --> 2
# -2825, 3 --> 8
# -456, 4 --> 0
# 0, 20 --> 0
# 65, 0 --> -1
# 24, -8 --> -1
# FUNDAMENTALS
# Solution
def find_digit(num, nth):
    return int(str(num)[-nth]) if nth <= len(str(num)) and nth > 0 else -1 if nth <= 0 else 0