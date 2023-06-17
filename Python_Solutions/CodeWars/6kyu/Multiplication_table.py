# Your task, is to create N×N multiplication table, of size provided in parameter.
#
# For example, when given size is 3:
#
# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:
#
# [[1,2,3],[2,4,6],[3,6,9]]
# ARRAYSFUNDAMENTALS
# Solution
def multiplication_table(size):
    return [[i * n for i in range(1, size + 1)] for n in range(1, size + 1)]