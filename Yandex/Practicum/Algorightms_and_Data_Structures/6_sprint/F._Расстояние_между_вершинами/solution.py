import sys


def solution() -> None:
    """
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        if u not in adj_list: adj_list[u] = []
        adj_list[u].append(v)
        if v not in adj_list: adj_list[v] = []
        adj_list[v].append(u)
    source, destination = map(int, sys.stdin.readline().rstrip().split())
    edges: int = 0
    seen: list[bool] = [False] * (n + 1)
    cur_nodes: list[int] = [source]
    next_nodes: list[int] = []
    while cur_nodes:
        for node in cur_nodes:
            if node == destination:
                sys.stdout.write(f'{edges}\n')
                return
            for neighbor in adj_list.get(node, []):
                if not seen[neighbor]:
                    seen[neighbor] = True
                    next_nodes.append(neighbor)
        edges += 1
        cur_nodes = next_nodes
        next_nodes = []
    sys.stdout.write(f'-1\n')


if __name__ == '__main__':
    solution()
