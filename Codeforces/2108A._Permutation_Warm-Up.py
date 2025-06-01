# A. Permutation Warm-Up
# time limit per test1 second
# memory limit per test256 megabytes
#
# For a permutation p
#  of length n
# ∗
# , we define the function:
#
# f(p)=∑i=1n|pi−i|
#
# You are given a number n
# . You need to compute how many distinct values the function f(p)
#  can take when considering all possible permutations of the numbers from 1
#  to n
# .
#
# ∗
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (n=3
#  but there is 4
#  in the array).
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first line of each test case contains an integer n
#  (1≤n≤500
# ) — the number of numbers in the permutations.
#
# Output
# For each test case, output a single integer — the number of distinct values of the function f(p)
#  for the given length of permutations.
#
# Example
# InputCopy
# 5
# 2
# 3
# 8
# 15
# 43
# OutputCopy
# 2
# 3
# 17
# 57
# 463
# Note
# Consider the first two examples of the input.
#
# For n=2
# , there are only 2
#  permutations — [1,2]
#  and [2,1]
# . f([1,2])=|1−1|+|2−2|=0
# , f([2,1])=|2−1|+|1−2|=1+1=2
# . Thus, the function takes 2
#  distinct values.
#
# For n=3
# , there are already 6
#  permutations: [1,2,3]
# , [1,3,2]
# , [2,1,3]
# , [2,3,1]
# , [3,1,2]
# , [3,2,1]
# , the function values of which will be 0,2,2,4,4
# , and 4
#  respectively, meaning there are a total of 3
#  values.