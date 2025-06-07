# C. Cherry Bomb
# time limit per test2 seconds
# memory limit per test256 megabytes
# Two integer arrays a
#  and b
#  of size n
#  are complementary if there exists an integer x
#  such that ai+bi=x
#  over all 1≤i≤n
# . For example, the arrays a=[2,1,4]
#  and b=[3,4,1]
#  are complementary, since ai+bi=5
#  over all 1≤i≤3
# . However, the arrays a=[1,3]
#  and b=[2,1]
#  are not complementary.
#
# Cow the Nerd thinks everybody is interested in math, so he gave Cherry Bomb two integer arrays a
#  and b
# . It is known that a
#  and b
#  both contain n
#  non-negative integers not greater than k
# .
#
# Unfortunately, Cherry Bomb has lost some elements in b
# . Lost elements in b
#  are denoted with −1
# . Help Cherry Bomb count the number of possible arrays b
#  such that:
#
# a
#  and b
#  are complementary.
# All lost elements are replaced with non-negative integers no more than k
# .
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤n≤2⋅105
# , 0≤k≤109
# ) — the size of the arrays and the maximum possible value of their elements.
#
# The second line contains n
#  integers a1,a2,...,an
#  (0≤ai≤k
# ).
#
# The third line contains n
#  integers b1,b2,...,bn
#  (−1≤bi≤k
# ). If bi=−1
# , then this element is missing.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# Output exactly one integer, the number of ways Cherry Bomb can fill in the missing elements from b
#  such that a
#  and b
#  are complementary.
#
# Example
# InputCopy
# 7
# 3 10
# 1 3 2
# -1 -1 1
# 5 1
# 0 1 0 0 1
# -1 0 1 0 -1
# 5 1
# 0 1 0 0 1
# -1 1 -1 1 -1
# 5 10
# 1 3 2 5 4
# -1 -1 -1 -1 -1
# 5 4
# 1 3 2 1 3
# 1 -1 -1 1 -1
# 5 4
# 1 3 2 1 3
# 2 -1 -1 2 0
# 5 5
# 5 0 5 4 3
# 5 -1 -1 -1 -1
# OutputCopy
# 1
# 0
# 0
# 7
# 0
# 1
# 0
# Note
# In the first example, the only way to fill in the missing elements in b
#  such that a
#  and b
#  are complementary is if b=[2,0,1]
# .
#
# In the second example, there is no way to fill in the missing elements of b
#  such that a
#  and b
#  are complementary.
#
# In the fourth example, some b
#  arrays that are complementary to a
#  are: [4,2,3,0,1],[7,5,6,3,4],
#  and [9,7,8,5,6]
# .