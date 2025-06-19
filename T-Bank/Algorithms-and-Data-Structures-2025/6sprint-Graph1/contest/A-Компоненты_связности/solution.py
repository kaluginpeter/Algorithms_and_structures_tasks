import sys


def dfs(start: int, adj_list: list[list[int]], colors: list[int], components: list[list[int]], color: int) -> None:
    colors[start] = color
    components.append([start])
    queue: list[int] = [start]
    while queue:
        vertex: int = queue.pop()
        for neighbor in adj_list[vertex]:
            if colors[neighbor] == -1:
                colors[neighbor] = color 
                components[color].append(neighbor)
                queue.append(neighbor)


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
        adj_list[v].append(u)
    colors: list[int] = [-1] * (n + 1)
    components: list[list[int]] = []
    color: int = 0
    for vertex in range(1, n + 1):
        if colors[vertex] == -1:
            dfs(vertex, adj_list, colors, components, color)
            color += 1
    sys.stdout.write('{}\n'.format(len(components)))
    for component in components:
        component.sort()
        sys.stdout.write('{}\n'.format(len(component)))
        sys.stdout.write('{}\n'.format(' '.join(str(vertex) for vertex in component)))


if __name__ == '__main__':
    solution()