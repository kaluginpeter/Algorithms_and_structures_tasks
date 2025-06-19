import sys


def dfs(start: int, adj_list: list[list[int]], colors: list[int]) -> bool:
    queue: list[int] = [start]
    while queue:
        vertex: int = queue.pop()
        if not colors[vertex]:
            colors[vertex] = 1
            queue.append(vertex)
            for neighbor in adj_list[vertex]:
                if colors[neighbor] == 1: return True
                elif not colors[neighbor]:
                    queue.append(neighbor)
        else: colors[vertex] = 2
    return False


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
    colors: list[int] = [0] * (n + 1)
    has_cycle: bool = False
    for vertex in range(1, n + 1):
        if not colors[vertex]:
            has_cycle = has_cycle or dfs(vertex, adj_list, colors)
    sys.stdout.write('{}\n'.format(int(has_cycle)))


if __name__ == '__main__':
    solution()