# A. Calculating Function
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# For a positive integer n let's define a function f:
#
# f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn
#
# Your task is to calculate f(n) for a given integer n.
#
# Input
# The single line contains the positive integer n (1 ≤ n ≤ 1015).
#
# Output
# Print f(n) in a single line.
#
# Examples
# inputCopy
# 4
# outputCopy
# 2
# inputCopy
# 5
# outputCopy
# -3
# Note
# f(4) =  - 1 + 2 - 3 + 4 = 2
#
# f(5) =  - 1 + 2 - 3 + 4 - 5 =  - 3
# Solution Math O(1) O(1)
import sys

def solution(n: int) -> str:
    answer: int = 0
    negative: int = ((n + 1) // 2) * (1 + (n if n & 1 else n - 1)) // 2
    positive: int = (n // 2) * (2 + (n if not n & 1 else n - 1)) // 2
    answer = positive - negative
    return str(answer)

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(n))