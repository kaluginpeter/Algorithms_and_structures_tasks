# Mighty Heroes
# Alyosha Popovich (Russian folk hero) stroke his sharp sword and
# cut the head of Zmey Gorynych (big Serpent with several heads)!
# He looked - and lo! - in its place immediately new heads appeared, exactly n.
# He stroke again, and where the second head was, 2*n heads appeared!
# The third time it was 2*3*n new heads, and after fourth swing it was 2*3*4*n heads,
# and so forth. And thus Alyosha decided to call it a day, and instead called a fellow
# Mage for help. While the Mage agreed, he needs to know the exact number of heads that Zmey Gorynych now has.
#
# The task
# Given the initial number of heads, the heads-count multiplier, and the number of sword-swings,
# calculate how many heads Zmey Gorynych has in the end.
#
# Examples
# initial = 2
# multiplier = 1
# swings = 1
#
# result:
#   1 head appearead after the swing: 2 - 1 + 1 = 2
#   Zmey has 2 heads in the end
# initial = 5
# multiplier = 10
# swings = 3
#
# result:
#   10 heads appearead after the first swing: 5 - 1 + 10 = 14
#   20 heads appearead after the second swing: 14 - 1 + 2 * 10 = 33
#   60 heads appearead after the third swing: 33 - 1 + 2 * 3 * 10 = 92
#   Zmey has 92 heads in the end
# FUNDAMENTALSALGORITHMSMATHEMATICS
# Solution
import math
def count_of_heads(initial, n, swings):
    for i in range(1, swings+1):
        initial = initial - 1 + n * math.factorial(i)
    return initial