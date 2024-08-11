# A. Cut Ribbon
# time limit per test1 second
# memory limit per test256 megabytes
# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:
#
# After the cutting each ribbon piece should have length a, b or c.
# After the cutting the number of ribbon pieces should be maximum.
# Help Polycarpus and find the number of ribbon pieces after the required cutting.
#
# Input
# The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.
#
# Output
# Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.
#
# Examples
# inputCopy
# 5 5 3 2
# outputCopy
# 2
# inputCopy
# 7 5 5 2
# outputCopy
# 2
# Note
# In the first example Polycarpus can cut the ribbon in such way: the first piece has length 2, the second piece has length 3.
#
# In the second example Polycarpus can cut the ribbon in such way: the first piece has length 5, the second piece has length 2.
# Solution Dynamic Programming O(N) O(N)
from typing import List
import sys

def solution(n: int, a: int, b: int, c: int) -> str:
    modules: List[int] = sorted([a, b, c])
    dp: List[int] = [float('-inf')] * (n + 1)
    dp[0] = 0

    for piece in range(1, n + 1):
        for module in modules:
            if piece >= module:
                dp[piece] = max(dp[piece], dp[piece - module] + 1)

    return str(dp[n] if dp[n] != float('-inf') else 0)

if __name__ == "__main__":
    n, a, b, c = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(solution(n, a, b, c))
