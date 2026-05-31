# The goal of this kata is to multiply two integers using the ancient Egyptian method, which only requires divisions and multiplications by two, and additions.
#
# Your function takes two integers as input. It shall return a list of the steps in the multiplication.
#
# Let m be the largest and n the smallest. While m is superior to 0, at each step:
#
# if m is not divisible by 2, add n to the list
# divide m by 2 (integer division)
# multiply n by 2
# At the end, return the list in descending order. The result of the multiplication is the sum of the list elements, but you have to return only the list.
#
# Input
# n and m integers, from 0 to 10,000. It is not guaranteed that m > n.
#
# Example
# m	n	m % 2	list
# 100	15	0	[]
# 50	30	0	[]
# 25	60	1	[60]
# 12	120	0	[60]
# 6	240	0	[60]
# 3	480	1	[480, 60]
# 1	960	1	[960, 480, 60]
# 0		0	[960, 480, 60]
# 100 * 15 = 1500 = 60 + 480 + 960
#
# So the expected result is [960, 480, 60].
#
# MathematicsPuzzlesAlgorithms
# Solution
def bin_mul(m, n):
    m, n = max(m, n), min(m, n)
    output = []
    while m:
        if m & 1 and n: output.append(n)
        m //= 2
        n *= 2
    return output[::-1]