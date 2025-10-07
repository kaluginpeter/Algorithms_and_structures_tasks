# B. Abraham's Great Escape
# time limit per test1.5 seconds
# memory limit per test256 megabytes
#
# Abraham is a brave explorer who goes where no other programmer has gone before. For his next expedition, he plans to investigate a peculiar maze. He knows that the maze is an n×n
#  grid with an arrow in each cell that points in one of four directions: up, down, left and right. Abraham also knows that if he stands on an arrow, he will be forced to follow the arrows starting from that cell. Each arrow moves Abraham exactly 1
#  cell in the direction that it is pointing. If he reaches an arrow that points towards the outside of the maze, Abraham will escape the maze.
#
# Abraham doesn't know how the arrows are arranged, so he wants to plan for multiple scenarios. He tasks you with finding an arrangement of arrows in the grid such that there are exactly k
#  starting cells from which he can escape the maze.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.
#
# The only line of each test case contains two integers n
# , k
#  (2≤n≤100
# , 0≤k≤n2
# ) — the size of the grid and the number of cells from which Abraham should be able to escape.
#
# It is guaranteed that the sum of n2
#  over all test cases does not exceed 105
# .
#
# Output
# For each test case, do one of the following:
#
# If there exists a grid satisfying the requirement, print YES and then print n
#  lines with n
#  characters in each line indicating the direction of the arrows. Each character should be one of U (up), R (right), L (left), or D (down).
# Otherwise, declare that the task is impossible by printing NO.
# If there are multiple solutions, print any of them.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 3
# 2 4
# 3 5
# 2 3
# OutputCopy
# YES
# UU
# UU
# YES
# UUU
# RDR
# ULR
# NO
# Note
# In the first test case, no matter which cell Abraham stands in initially, he will eventually exit the maze as he will move upward successively; thus, he can escape from all 4
#  cells, as required.
#
# In the second test case, Abraham eventually escapes if he stands on one of the following:
#
# Any cell in the first row (all of which are U)
# Any cell in the third column (one of which is U and the other two R)
# There is no other cell where he can stand and escape. We see that Abraham can escape from exactly 5
#  cells in this arrangement, as required.
#
# In the third test case, it can be proved that there's no arrangement of arrows so that Abraham can escape from exactly 3
#  cells.