# Gobang Weight Table
# You will generate a weight table of gobang game in less than 100 characters. The outermost layer of the table is 0, and the number is incremented by one for each layer inside.
#
# Your task is to define a function, which returns weight table in different sizes(N) as the examples below.
#
# Examples:
# Input: 3
# Output:
# [[0, 0, 0],
#  [0, 1, 0],
#  [0, 0, 0]]
# Input: 5
# Output:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, 2, 1, 0],
#  [0, 1, 1, 1, 0],
#  [0, 0, 0, 0, 0]]
# Input: 9
# Output:
# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 1, 1, 0],
#  [0, 1, 2, 2, 2, 2, 2, 1, 0],
#  [0, 1, 2, 3, 3, 3, 2, 1, 0],
#  [0, 1, 2, 3, 4, 3, 2, 1, 0],
#  [0, 1, 2, 3, 3, 3, 2, 1, 0],
#  [0, 1, 2, 2, 2, 2, 2, 1, 0],
#  [0, 1, 1, 1, 1, 1, 1, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# Notes
# 3 <= N <= 99, N will ONLY be odd number.
# Your code cannot be longer than 100 characters.
# RESTRICTEDPUZZLES
def weight_table(n):return[[min(i,n-1-i,j,n-1-j)for j in range(n)]for i in range(n)]