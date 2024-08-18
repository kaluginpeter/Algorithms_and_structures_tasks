# Write a function that returns the greatest common factor of an array of positive integers.
# Your return value should be a number, you will only receive positive integers.
#
# greatest_common_factor([46, 14, 20, 88]) # == 2
# FUNDAMENTALSALGORITHMS
# Solution
def greatest_common_factor(seq):
    l = []
    for i in range(1, min(seq)+1):
        if all(j % i == 0 for j in seq): l.append(i)
    return max(l)