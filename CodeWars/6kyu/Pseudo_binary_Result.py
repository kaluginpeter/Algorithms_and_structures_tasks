# Definition
# For this task, we will use the term "pseudo-binary" number, defining it as a positive decimal number, which consists of only 1s and/or 0s. So, the number
# 10110011
# 10110011 might look like a regular binary number but it is not.
#
# Task
# For every
# n
# ∈
# N
# n∈N, there exist an infinite amount of positive integers
# M
# =
# {
# m
# 1
# ,
# m
# 2
# ,
# m
# 3
# ,
# …
# }
# M={m
# 1
# ​
#  ,m
# 2
# ​
#  ,m
# 3
# ​
#  ,…}, such that, for any
# m
# i
# ∈
# M
# m
# i
# ​
#  ∈M, the number
# n
# ×
# m
# i
# n×m
# i
# ​
#   results in a pseudo-binary number. Your task is to find any such number
# m
# m based on the input
# n
# n.
#
# Examples
# pseudo_binary(2)  # can return 5;          2 * 5  = 10
# pseudo_binary(3)  # can return 37;         3 * 37 = 111
# pseudo_binary(10) # can return 1;          10 * 1 = 10
# pseudo_binary(9)  # can return 12 345 679; 9 * 12 345 679 = 111 111 111
# Random tests
# 100 small random tests (
# 1
# ≤
# n
# ≤
# 100
# 1≤n≤100)
# 50 medium random tests (
# 101
# ≤
# n
# ≤
# 1000
# 101≤n≤1000)
# 20 large random tests (
# 1001
# ≤
# n
# ≤
# 5000
# 1001≤n≤5000)
# Good luck!
#
# Number Theory
def pseudo_binary(n: int) -> int:
    q: list[int] = [1]
    while q:
        i: int = q.pop()
        if i % n == 0: return i // n
        if i > 10**20: continue
        q.append(i * 10)
        q.append(i * 10 + 1)