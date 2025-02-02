import sys


def solution() -> None:
    """
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, set[int]] = dict()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        if u != v:
            if u not in adj_list: adj_list[u] = set()
            adj_list[u].add(v)
            if v not in adj_list: adj_list[v] = set()
            adj_list[v].add(u)
    for vertex, edges in adj_list.items():
        if len(edges) != n - 1:
            sys.stdout.write('NO\n')
            return
    sys.stdout.write('YES\n' if (len(adj_list) == n or n == 1) else 'NO\n')


if __name__ == '__main__':
    solution()
