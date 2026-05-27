# One man (let's call him Eulampy) has a collection of almost identical Fabergé eggs. One day his friend Tempter said to him:
#
# Do you see that skyscraper? And can you tell me the highest floor that if you drop your egg from will not crack?
# No, - said Eulampy.
# But if you give me N eggs, - says Tempter - I'l tell you an answer.
# Deal - said Eulampy. But I have one requirement before we start this: if I will see more than M falls of the eggs, my heart will be crushed instead of the eggs. So you have only M tries to throw eggs. Would you tell me the exact floor with this limitation?
# Task
# Your task is to help Tempter - write a function that takes 2 arguments - the number of eggs n and the number of total tries m. You should calculate the maximum skyscraper height (in floors), in which it is guaranteed to find the exact highest floor from which a dropped egg won't crack.
#
# Which means,
#
# You can throw an egg from a specific floor every try
# Every egg has the same durability - if they're thrown from a certain floor or below, they won't crack. Otherwise they crack. If an egg does not crack, it can be dropped again.
# You have n eggs and m total tries
# What is the maxmimum skyscraper height, such that you can always determine exactly which floor is the highest, which will not break an egg when dropped?
# Examples
# Number of eggs (n), Number of total tries (m) -> Maximum skyscraper height
# 0, 14 -> 0
# 2, 0  -> 0
# 2, 14 -> 105
# 7, 20 -> 137979
# Data range
# n <= 20000
# m <= 20000
# MathematicsDynamic ProgrammingPerformanceAlgorithms
# Solution
from math import comb

def height(n, m):
    if n == 0 or m == 0: return 0
    n = min(n, m)
    total = 0
    c = 1
    for i in range(1, n + 1):
        c = c * (m - i + 1) // i
        total += c
    return total