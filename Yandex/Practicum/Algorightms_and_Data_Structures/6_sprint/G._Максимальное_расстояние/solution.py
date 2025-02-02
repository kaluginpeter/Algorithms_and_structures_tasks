import sys


def solution() -> None:
    """
    Time Complexity O(V + E)
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(m):
        source, destintaion = map(int, sys.stdin.readline().rstrip().split())
        if source not in adj_list: adj_list[source] = []
        adj_list[source].append(destintaion)
        if destintaion not in adj_list: adj_list[destintaion] = []
        adj_list[destintaion].append(source)
    source: int = int(sys.stdin.readline().rstrip())
    colors: list[int] = [-1] * (n + 1)
    colors[source] = 1
    cur_nodes: list[int] = [source]
    next_nodes: list[int] = []
    distance: int = -1
    while cur_nodes:
        for node in cur_nodes:
            for neighbor in adj_list.get(node, []):
                if colors[neighbor] == -1:
                    colors[neighbor] = 1
                    next_nodes.append(neighbor)
        cur_nodes = next_nodes
        next_nodes = []
        distance += 1
    sys.stdout.write(f'{distance}\n')


if __name__ == '__main__':
    solution()