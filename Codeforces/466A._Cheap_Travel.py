# A. Cheap Travel
# time limit per test1 second
# memory limit per test256 megabytes
# Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles. Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of money she will have to spend to make n rides?
#
# Input
# The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned, the number of rides covered by the m ride ticket, the price of a one ride ticket and the price of an m ride ticket.
#
# Output
# Print a single integer — the minimum sum in rubles that Ann will need to spend.
#
# Examples
# inputCopy
# 6 2 1 2
# outputCopy
# 6
# inputCopy
# 5 2 2 3
# outputCopy
# 8
# Note
# In the first sample one of the optimal solutions is: each time buy a one ride ticket. There are other optimal solutions. For example, buy three m ride tickets.
# Solution Math Greedy O(1) O(1)
import sys


def solution(n: int, m: int, a: int, b: int) -> str:
    a_c: float = a
    mb_c: float = b / m
    if a_c <= mb_c:
        return str(n * a_c)
    c: int = n // m * b
    n %= m
    return str(c + min(b, n * a_c))


if __name__ == '__main__':
    n, m, a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(solution(n, m, a, b))
