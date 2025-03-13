import sys
from collections import deque

MOD: int = 10 ** 9 + 7


def solution():
    """
    Time Complexity O(VE)
    Memory Complexity O(VE)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: list[list[int]] = [[] for _ in range(n + 1)]
    in_degree: list[int] = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        adj_list[u].append(v)
        in_degree[v] += 1

    q: list[int] = deque()
    top_order: list[int] = []

    for vertex in range(1, n + 1):
        if in_degree[vertex] == 0: q.append(vertex)

    while q:
        vertex = q.popleft()
        top_order.append(vertex)
        for neighbor in adj_list[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0: q.append(neighbor)

    A, B = map(int, sys.stdin.readline().rstrip().split())
    dp: list[int] = [0] * (n + 1)
    dp[A] = 1

    for vertex in top_order:
        for neighbor in adj_list[vertex]:
            dp[neighbor] = (dp[neighbor] + dp[vertex]) % MOD

    sys.stdout.write('{}\n'.format(dp[B]))


if __name__ == "__main__":
    solution()