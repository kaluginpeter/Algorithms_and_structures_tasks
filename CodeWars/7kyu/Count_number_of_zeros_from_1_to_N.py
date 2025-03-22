# Create an algorithm to count the number of zeros that appear between 1 and N.
#
# Examples
#  10  -->   1  // 10
#  20  -->   2  // 10, 20
# 100  -->  11  // 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# 200  -->  31
# Algorithms
# Solution
def count_zeros(x):
    return sum(str(i).count('0') for i in range(1, x + 1))