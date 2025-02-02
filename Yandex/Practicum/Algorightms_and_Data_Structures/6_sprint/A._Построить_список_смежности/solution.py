import sys


def solution() -> None:
    """Time Complexity O((V + E) + ElogE)
    Memory Complexity O(V + E)"""
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(e):
        source, destination = map(int, sys.stdin.readline().rstrip().split())
        if source not in adj_list:
            adj_list[source] = []
        adj_list[source].append(destination)
    for vertex in range(1, v + 1):
        edges: int = len(adj_list.get(vertex, []))
        if not edges:
            sys.stdout.write(str(edges) + '\n')
        else:
            adj_list[vertex].sort()
            sys.stdout.write(str(edges) + ' ' + ' '.join(str(neighbor) for neighbor in adj_list[vertex]) + '\n')


if __name__ == '__main__':
    solution()