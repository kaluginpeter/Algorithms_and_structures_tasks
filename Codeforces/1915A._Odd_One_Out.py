# A. Odd One Out
# time limit per test1 second
# memory limit per test256 megabytes
# You are given three digits a
# , b
# , c
# . Two of them are equal, but the third one is different from the other two.
#
# Find the value that occurs exactly once.
#
# Input
# The first line contains a single integer t
#  (1≤t≤270
# ) — the number of test cases.
#
# The only line of each test case contains three digits a
# , b
# , c
#  (0≤a
# , b
# , c≤9
# ). Two of the digits are equal, but the third one is different from the other two.
#
# Output
# For each test case, output the value that occurs exactly once.
#
# Example
# inputCopy
# 10
# 1 2 2
# 4 3 4
# 5 5 6
# 7 8 8
# 9 0 9
# 3 6 3
# 2 8 2
# 5 7 7
# 7 7 5
# 5 7 5
# outputCopy
# 1
# 3
# 6
# 7
# 0
# 6
# 8
# 5
# 5
# 7
# Solution O(1) O(1)
import sys


def solution(t: int) -> None:
    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        if a == b: print(c)
        elif b == c: print(a)
        else: print(b)


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
