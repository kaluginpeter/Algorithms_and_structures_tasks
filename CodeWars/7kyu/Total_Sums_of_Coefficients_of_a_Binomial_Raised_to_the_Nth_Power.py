# When you want to get the square of a binomial of two variables x and y, you will have:
#
# (
# x
# +
# y
# )
# 2
# =
# x
# 2
# +
# 2
# x
# y
# +
# y
# 2
# (x+y)
# 2
#  =x
# 2
#  +2xy+y
# 2
#
#
# And the cube:
#
# (
# x
# +
# y
# )
# 3
# =
# x
# 3
# +
# 3
# x
# 2
# y
# +
# 3
# x
# y
# 2
# +
# y
# 3
# (x+y)
# 3
#  =x
# 3
#  +3x
# 2
#  y+3xy
# 2
#  +y
# 3
#
#
# It is known from many centuries ago that for an exponent n, the result of a binomial x + y raised to the n-th power is:
#
# (
# x
# +
# y
# )
# n
# =
# (
# n
# 0
# )
# x
# n
# y
# 0
# +
# (
# n
# 1
# )
# x
# n
# −
# 1
# y
# 1
# +
# (
# n
# 2
# )
# x
# n
# −
# 2
# y
# 2
# +
# ⋯
# +
# (
# n
# n
# −
# 1
# )
# x
# 1
# y
# n
# −
# 1
# +
# (
# n
# n
# )
# x
# 0
# y
# n
# (x+y)
# n
#  =(
# 0
# n
# ​
#  )x
# n
#  y
# 0
#  +(
# 1
# n
# ​
#  )x
# n−1
#  y
# 1
#  +(
# 2
# n
# ​
#  )x
# n−2
#  y
# 2
#  +⋯+(
# n−1
# n
# ​
#  )x
# 1
#  y
# n−1
#  +(
# n
# n
# ​
#  )x
# 0
#  y
# n
#
# Or using the sumation notation:
#
# (
# x
# +
# y
# )
# n
# =
# ∑
# k
# =
# 0
# n
# (
# n
# k
# )
# x
# n
# −
# k
# y
# k
# =
# ∑
# k
# =
# 0
# n
# (
# n
# k
# )
# x
# k
# y
# n
# −
# k
# (x+y)
# n
#  =
# k=0
# ∑
# n
# ​
#  (
# k
# n
# ​
#  )x
# n−k
#  y
# k
#  =
# k=0
# ∑
# n
# ​
#  (
# k
# n
# ​
#  )x
# k
#  y
# n−k
#
# Each coefficient of a term has the following value:
#
# (
# n
# k
# )
# =
# n
# !
# (
# n
# −
# k
# )
# !
# ⋅
# k
# !
# =
# (
# n
# −
# k
# +
# 1
# )
# ⋯
# (
# n
# −
# 2
# )
# (
# n
# −
# 1
# )
# n
# k
# !
# (
# k
# n
# ​
#  )=
# (n−k)!⋅k!
# n!
# ​
#  =
# k!
# (n−k+1)⋯(n−2)(n−1)n
# ​
#
# Each coefficient value coincides with the amount of combinations without replacements of a set of n elements using only k different ones of that set.
#
# Let's see the total sum of the coefficients of the different powers for the binomial:
#
# (
# x
# +
# y
# )
# 0
# (
# 1
# )
# (x+y)
# 0
#  (1)
#
# (
# x
# +
# y
# )
# 1
# =
# x
# +
# y
# (
# 2
# )
# (x+y)
# 1
#  =x+y(2)
#
# (
# x
# +
# y
# )
# 2
# =
# x
# 2
# +
# 2
# x
# y
# +
# y
# 2
# (
# 4
# )
# (x+y)
# 2
#  =x
# 2
#  +2xy+y
# 2
#  (4)
#
# (
# x
# +
# y
# )
# 3
# =
# x
# 3
# +
# 3
# x
# 2
# y
# +
# 3
# x
# y
# 2
# +
# y
# 3
# (
# 8
# )
# (x+y)
# 3
#  =x
# 3
#  +3x
# 2
#  y+3xy
# 2
#  +y
# 3
#  (8)
#
# Task
# Create a function that returns (an array) of the coefficients sums from 0 to n (inclusive), where the last element is the sum of all previous elements.
#
# We add some examples below:
#
# for n = 0, return 1, 1
# for n = 1, return 1, 2, 3
# for n = 2, return 1, 2, 4, 7
# for n = 3, return 1, 2, 4, 8, 15
# Features of the test
#
# Low Performance Tests
# Number of tests = 50
# 9 < n < 101
#
# High Performance Tests
# Number of Tests = 50
# 99 < n < 5001
#
# N.B. In C, input is limited to 0 <= n <= 63
# FundamentalsData StructuresAlgorithmsMathematicsLogic