# In this kata you're expected to find the longest consecutive sequence of positive squares that sums up to a number.
#
# E.g,
#
# ** 595 = 62 + 72 + 82 + 92 + 102 + 112 + 122 **.
#
# Your task is to write the function longest_sequence(n) that either finds the longest
# consecutive sequence of squares that sums to the number n, or determines that no such sequence exists.
#
# longest_sequence(50) # => [3, 4, 5]
#     # 9 + 16 + 25 = 50
#
# longest_sequence(595) # => [6, 7, 8, 9, 10, 11, 12]
#
# longest_sequence(10) # => []
# Return an empty list if no such sequence exists.
#
# MATHEMATICSALGORITHMS
# Solution
def longest_sequence(n):
    for i in range(1, int(n**0.5)+1):
        x, j = 0, i
        while x < n:
            x += j*j
            j += 1
        if x == n: return list(range(i, j))
    return []