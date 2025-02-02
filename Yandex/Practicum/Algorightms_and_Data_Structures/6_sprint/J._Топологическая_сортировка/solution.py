import sys


def dfs(source: int, adj_list: dict[int, list[int]], colors: list[str], output: list[int]) -> None:
    call_stack: list[int] = [source]
    while call_stack:
        vertex: int = call_stack.pop()
        if colors[vertex] == 'white':
            colors[vertex] = 'grey'
            call_stack.append(vertex)
            for neighbor in adj_list.get(vertex, []):
                if colors[neighbor] == 'white': call_stack.append(neighbor)
        elif colors[vertex] == 'grey':
            output.append(vertex)
            colors[vertex] = 'black'


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
    colors: list[str] = ['white'] * (n + 1)
    output: list[int] = []
    for vertex in range(n, 0, -1):
        if colors[vertex] == 'white': dfs(vertex, adj_list, colors, output)
    output.reverse()
    sys.stdout.write(' '.join(str(vertex) for vertex in output) + '\n')


if __name__ == '__main__':
    solution()