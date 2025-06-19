import sys


def solution() -> None:
    """
    Time Complexity O(|V| + |E|)
    Memory Complexity O(|V| + |E|)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        adj_list[u].append(v)
    order: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    positions: list[int] = [0] * (n + 1)
    for i in range(n): positions[order[i]] = i
    for source in range(1, n + 1):
        for destination in adj_list[source]:
            if positions[source] > positions[destination]:
                sys.stdout.write('NO\n')
                return
    sys.stdout.write('YES\n')


if __name__ == '__main__':
    solution()