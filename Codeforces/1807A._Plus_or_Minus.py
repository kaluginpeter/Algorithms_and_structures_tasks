# A. Plus or Minus
# time limit per test1 second
# memory limit per test256 megabytes
# You are given three integers a
# , b
# , and c
#  such that exactly one of these two equations is true:
#
# a+b=c
# a−b=c
# Output + if the first equation is true, and - otherwise.
# Input
# The first line contains a single integer t
#  (1≤t≤162
# ) — the number of test cases.
#
# The description of each test case consists of three integers a
# , b
# , c
#  (1≤a,b≤9
# , −8≤c≤18
# ). The additional constraint on the input: it will be generated so that exactly one of the two equations will be true.
#
# Output
# For each test case, output either + or - on a new line, representing the correct equation.
#
# Example
# inputCopy
# 11
# 1 2 3
# 3 2 1
# 2 9 -7
# 3 4 7
# 1 1 2
# 1 1 0
# 3 3 6
# 9 9 18
# 9 9 0
# 1 9 -8
# 1 9 10
# outputCopy
# +
# -
# -
# +
# +
# -
# +
# +
# -
# -
# +
# Note
# In the first test case, 1+2=3
# .
#
# In the second test case, 3−2=1
# .
#
# In the third test case, 2−9=−7
# . Note that c
#  can be negative.
# Solution Math O(1) O(1)
import sys


def solution(t: int) -> None:
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        print(['-', '+'][a + b == c])


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
