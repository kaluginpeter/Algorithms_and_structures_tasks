# Given n number of people in a room, calculate the probability that any two people in that room have the same birthday (assume 365 days every year = ignore leap year). Answers should be two decimals unless whole (0 or 1) eg 0.05
#
# Algorithms
# Solution
from math import prod

def calculate_probability(n):
    return round(1 - prod(i / 365 for i in range(365, 365 - n, -1)), 2)