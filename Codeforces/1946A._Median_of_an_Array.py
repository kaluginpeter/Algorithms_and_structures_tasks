# A. Median of an Array
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an array a
#  of n
#  integers.
#
# The median of an array q1,q2,…,qk
#  is the number p⌈k2⌉
# , where p
#  is the array q
#  sorted in non-decreasing order. For example, the median of the array [9,5,1,2,6]
#  is 5
# , as in the sorted array [1,2,5,6,9]
# , the number at index ⌈52⌉=3
#  is 5
# , and the median of the array [9,2,8,3]
#  is 3
# , as in the sorted array [2,3,8,9]
# , the number at index ⌈42⌉=2
#  is 3
# .
#
# You are allowed to choose an integer i
#  (1≤i≤n
# ) and increase ai
#  by 1
#  in one operation.
#
# Your task is to find the minimum number of operations required to increase the median of the array.
#
# Note that the array a
#  may not necessarily contain distinct numbers.
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. Then follows the description of the test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤105
# ) — the length of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the array a
# .
#
# It is guaranteed that the sum of the values of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output a single integer — the minimum number of operations required to increase the median of the array.
#
# Example
# InputCopy
# 8
# 3
# 2 2 8
# 4
# 7 3 3 1
# 1
# 1000000000
# 5
# 5 5 5 4 5
# 6
# 2 1 2 3 1 4
# 2
# 1 2
# 2
# 1 1
# 4
# 5 5 5 5
# OutputCopy
# 1
# 2
# 1
# 3
# 2
# 1
# 2
# 3
# Note
# In the first test case, you can apply one operation to the first number and obtain the array [3,2,8]
# , the median of this array is 3
# , as it is the number at index ⌈32⌉=2
#  in the non-decreasing sorted array [2,3,8]
# . The median of the original array [2,2,8]
#  is 2
# , as it is the number at index ⌈32⌉=2
#  in the non-decreasing sorted array [2,2,8]
# . Thus, the median increased (3>2
# ) in just one operation.
#
# In the fourth test case, you can apply one operation to each of the numbers at indices 1,2,3
#  and obtain the array [6,6,6,4,5]
# , the median of this array is 6
# , as it is the number at index ⌈52⌉=3
#  in the non-decreasing sorted array [4,5,6,6,6]
# . The median of the original array [5,5,5,4,5]
#  is 5
# , as it is the number at index ⌈52⌉=2
#  in the non-decreasing sorted array [4,5,5,5,5]
# . Thus, the median increased (6>5
# ) in three operations. It can be shown that this is the minimum possible number of operations.
#
# In the fifth test case, you can apply one operation to each of the numbers at indices 1,3
#  and obtain the array [3,1,3,3,1,4]
# , the median of this array is 3
# , as it is the number at index ⌈62⌉=3
#  in the non-decreasing sorted array [1,1,3,3,3,4]
# . The median of the original array [2,1,2,3,1,4]
#  is 2
# , as it is the number at index ⌈62⌉=3
#  in the non-decreasing sorted array [1,1,2,2,3,4]
# . Thus, the median increased (3>2
# ) in two operations. It can be shown that this is the minimum possible number of operations.