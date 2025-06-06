# B. St. Chroma
# time limit per test2 seconds
# memory limit per test256 megabytes
# Given a permutation∗
#  p
#  of length n
#  that contains every integer from 0
#  to n−1
#  and a strip of n
#  cells, St. Chroma will paint the i
# -th cell of the strip in the color MEX(p1,p2,...,pi)
# †
# .
#
# For example, suppose p=[1,0,3,2]
# . Then, St. Chroma will paint the cells of the strip in the following way: [0,2,2,4]
# .
#
# You have been given two integers n
#  and x
# . Because St. Chroma loves color x
# , construct a permutation p
#  such that the number of cells in the strip that are painted color x
#  is maximized.
#
# ∗
# A permutation of length n
#  is a sequence of n
#  elements that contains every integer from 0
#  to n−1
#  exactly once. For example, [0,3,1,2]
#  is a permutation, but [1,2,0,1]
#  isn't since 1
#  appears twice, and [1,3,2]
#  isn't since 0
#  does not appear at all.
#
# †
# The MEX
#  of a sequence is defined as the first non-negative integer that does not appear in it. For example, MEX(1,3,0,2)=4
# , and MEX(3,1,2)=0
# .
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤4000
# ) — the number of test cases.
#
# The only line of each test case contains two integers n
#  and x
#  (1≤n≤2⋅105
# , 0≤x≤n
# ) — the number of cells and the color you want to maximize.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# Output a permutation p
#  of length n
#  such that the number of cells in the strip that are painted color x
#  is maximized. If there exist multiple such permutations, output any of them.
#
# Example
# InputCopy
# 7
# 4 2
# 4 0
# 5 0
# 1 1
# 3 3
# 1 0
# 4 3
# OutputCopy
# 1 0 3 2
# 2 3 1 0
# 3 2 4 1 0
# 0
# 0 2 1
# 0
# 1 2 0 3
# Note
# The first example is explained in the statement. It can be shown that 2
#  is the maximum amount of cells that can be painted in color 2
# . Note that another correct answer would be the permutation [0,1,3,2]
# .
#
# In the second example, the permutation gives the coloring [0,0,0,4]
# , so 3
#  cells are painted in color 0
# , which can be shown to be maximum.