import sys


def dfs(source: int, adj_list: dict[int, list[int]], colors: list[int], components_color: int, components: list[list[int]]) -> None:
    call_stack: list[int] = [source]
    while call_stack:
        vertex: int = call_stack.pop()
        if colors[vertex] == -1:
            colors[vertex] = components_color
            components[components_color].append(vertex)
            for neighbor in adj_list.get(vertex, []):
                if colors[neighbor] == -1: call_stack.append(neighbor)


def solution() -> None:
    """
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(m):
        before, after = map(int, sys.stdin.readline().rstrip().split())
        if before not in adj_list: adj_list[before] = []
        adj_list[before].append(after)
        if after not in adj_list: adj_list[after] = []
        adj_list[after].append(before)
    colors: list[int] = [-1] * (n + 1)
    components: list[list[int]] = []
    components_color: int = 0
    for vertex in range(1, n + 1):
        if colors[vertex] == -1:
            components.append([])
            dfs(vertex, adj_list, colors, components_color, components)
            components_color += 1
    for component in components: component.sort()
    components.sort()
    sys.stdout.write(str(components_color) + '\n')
    for component in components:
        sys.stdout.write(' '.join(str(vertex) for vertex in component) + '\n')


if __name__ == '__main__':
    solution()