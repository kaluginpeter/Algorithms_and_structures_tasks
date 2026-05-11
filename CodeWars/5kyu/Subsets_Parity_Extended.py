# Task
# Given an integer
# n
# n, determining the set
# S
# =
# {
# 1
# ,
# 2
# ,
# 3
# ,
# …
# ,
# n
# }
# S={1,2,3,…,n}. Determine whether the number of subsets with
# k
# k elements is divisible by
# d
# d.
#
# Input
# n - the boundary for the set of natural numbers.
# k - the number of elements the subsets must have.
# d - the divisor.
# Output
# Boolean, indicating whether the statement above is true.
# Examples
# subset_divisibility(4, 2, 6)  -> True
# subset_divisibility(8, 6, 7)  -> True
# subset_divisibility(13, 6, 4) -> True
#
# subset_divisibility(4, 2, 4)  -> False
# subset_divisibility(8, 6, 5)  -> False
# subset_divisibility(13, 6, 8) -> False
# Tests
# 100 random tests, with
# 10
# ≤
# n
# ≤
# 1
# 0
# 4
# ;
# 10
# ≤
# k
# ≤
# n
# 10≤n≤10
# 4
#  ;10≤k≤n;
# d
# d's highest prime factor is
# 547
# 547;
# d
# d can reach over
# 1
# 0
# 200
# 10
# 200
#  .
# 100 extreme random tests, with
# 1
# 0
# 6
# ≤
# n
# ≤
# 1
# 0
# 9
# ;
# 1
# 0
# 6
# ≤
# k
# ≤
# n
# 10
# 6
#  ≤n≤10
# 9
#  ;10
# 6
#  ≤k≤n;
# d
# d's highest prime factor is
# 3581
# 3581;
# d
# d can reach over
# 1
# 0
# 1000
# 10
# 1000
#  .
# Reference
# This problem is an extension of myjinxin2015's Sub Sets Parity kata.
#
# Number TheoryPerformance