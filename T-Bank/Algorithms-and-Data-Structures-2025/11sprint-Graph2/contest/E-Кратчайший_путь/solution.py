import sys
import heapq
from collections import defaultdict


def solution() -> None:
    """
    Time Complexity O(NlogM)
    Memory Complexity O(N + M)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[tuple[int, int]]] = defaultdict(list)
    seen: list[bool] = [False] * (n + 1)
    cost: list[int] = [float('inf')] * (n + 1)
    seen[1] = True
    cost[1] = 0
    for _ in range(m):
        source, destination, weight = map(int, sys.stdin.readline().rstrip().split())
        adj_list[source].append((destination, weight))
        adj_list[destination].append((source, weight))
    
    min_heap: list[tuple[int, int]] = [(0, 1)]
    while min_heap:
        amount, vertex = heapq.heappop(min_heap)
        for next_vertex, weight in adj_list[vertex]:
            if not seen[next_vertex] or (amount + weight < cost[next_vertex]):
                seen[next_vertex] = True
                cost[next_vertex] = amount + weight
                heapq.heappush(min_heap, (amount + weight, next_vertex))
    sys.stdout.write('{}\n'.format(' '.join(str(cost[vertex]) for vertex in range(1, n + 1))))


if __name__ == '__main__':
    solution()