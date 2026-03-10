# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
# Your Task
# Complete the bouncyRatio function.
#
# The input will be the target ratio.
#
# The output should be the smallest number such that the proportion of bouncy numbers reaches the target ratio.
#
# You should throw an Error for a ratio less than 0% or greater than 99%.
#
# Source
#
# https://projecteuler.net/problem=112
# Updates
#
# 26/10/2015: Added a higher precision test case.
# MathematicsPuzzles
# Solution
def is_bouncy(n: int) -> bool:
    inc: bool = False
    dec: bool = False
    prev: int = n % 10
    n //= 10
    while n:
        cur: int = n % 10
        if cur < prev: inc = True
        elif cur > prev: dec = True
        if inc and dec: return True
        prev = cur
        n //= 10
    return False


def bouncy_ratio(ratio):
    if not (0 <= ratio <= 0.99): raise Exception()
    if ratio == 0: return 1
    bouncy: int = 0
    n: int = 1
    while True:
        if is_bouncy(n): bouncy += 1
        if n >= 100 and bouncy / n >= ratio: return n
        n += 1