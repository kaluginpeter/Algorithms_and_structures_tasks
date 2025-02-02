import sys
import heapq


def dijkstra(source: int, adj_list: dict[int, list[int]], n: int) -> list[int]:
    dist: list[int] = [-1] * (n + 1)
    dist[source] = 0
    min_heap: list[tuple[int, int]] = [(0, source)]
    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        for neighbor, cost in adj_list.get(vertex, []):
            amount: int = weight + cost
            if (dist[neighbor] == -1) or (amount < dist[neighbor]):
                heapq.heappush(min_heap, (amount, neighbor))
                dist[neighbor] = amount
    return dist


def solution() -> None:
    """
    Time Complexity O(V(VlogE))
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[int]] = dict()
    for _ in range(m):
        source, destination, weight = map(int, sys.stdin.readline().rstrip().split())
        if source not in adj_list: adj_list[source] = []
        adj_list[source].append((destination, weight))
        if destination not in adj_list: adj_list[destination] = []
        adj_list[destination].append((source, weight))
    for vertex in range(1, n + 1):
        shortest_path_tree: list[int] = dijkstra(vertex, adj_list, n)
        for idx in range(1, n + 1):
            if idx > 1: sys.stdout.write(' ')
            sys.stdout.write(str(shortest_path_tree[idx]))
        sys.stdout.write('\n')


if __name__ == '__main__':
    solution()