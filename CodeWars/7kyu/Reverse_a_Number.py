# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
#
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
#
# Examples
#  123 ->  321
# -456 -> -654
# 1000 ->    1
# ALGORITHMSFUNDAMENTALS
# Solution
def reverseNumber(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)