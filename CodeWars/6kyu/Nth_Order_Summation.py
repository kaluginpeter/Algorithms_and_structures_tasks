# Task
# Consider a series of functions
# S
# m
# (
# n
# )
# S
# m
# ​
#  (n) where:
#
# S
# 0
# (
# n
# )
# =
# 1
# S
# 0
# ​
#  (n)=1
# S
# m
# +
# 1
# (
# n
# )
# =
# ∑
# k
# =
# 1
# n
# S
# m
# (
# k
# )
# S
# m+1
# ​
#  (n)=
# k=1
# ∑
# n
# ​
#  S
# m
# ​
#  (k)
#
# Write a function s which takes two integer arguments m and n and returns the value defined by
# S
# m
# (
# n
# )
# S
# m
# ​
#  (n).
#
# Inputs
# 0 <= m <= 100
# 1 <= n <= 10**100
#
# MathematicsPerformance
# Solution
from math import factorial

def s(m, n):
    result = 1

    for i in range(m):
        result *= n + i

    return result // factorial(m)