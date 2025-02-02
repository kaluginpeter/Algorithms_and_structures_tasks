import sys


def is_bipartite(source: int, adj_list: dict[int, list[int]], colors: list[int]) -> bool:
    call_stack: list[int] = [source]
    while call_stack:
        vertex: int = call_stack.pop()
        for neighbor in adj_list.get(vertex, []):
            if colors[neighbor] == colors[vertex]: return False
            elif colors[neighbor] != -1: continue
            colors[neighbor] = (colors[vertex] + 1) % 2
            call_stack.append(neighbor)
    return True


def solution() -> None:
    """
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        if u not in adj_list: adj_list[u] = list()
        adj_list[u].append(v)
        if v not in adj_list: adj_list[v] = list()
        adj_list[v].append(u)
    colors: list[int] = [-1] * (n + 1)
    for vertex in range(1, n + 1):
        if colors[vertex] != -1: continue
        colors[vertex] = 0
        if not is_bipartite(vertex, adj_list, colors):
            sys.stdout.write('NO\n')
            return
    sys.stdout.write('YES\n')


if __name__ == '__main__':
    solution()
