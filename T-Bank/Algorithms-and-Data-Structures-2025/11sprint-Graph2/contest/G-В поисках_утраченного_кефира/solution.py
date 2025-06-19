import sys
from collections import defaultdict
import heapq


def dijkstra(source: int, adj_list: dict[int, list[tuple[int, int]]], n: int) -> list[int]:
    dist: list[int] = [float('inf')] * (n + 1)
    dist[source] = 0
    min_heap: list[tuple[int, int]] = []
    heapq.heappush(min_heap, (0, source))
    while min_heap:
        path, vertex = heapq.heappop(min_heap)
        if path > dist[vertex]: continue
        for another_vertex, cost in adj_list[vertex]:
            new_path: int = path + cost
            if new_path < dist[another_vertex]:
                dist[another_vertex] = new_path
                heapq.heappush(min_heap, (new_path, another_vertex))
    
    return dist


def solution() -> None:
    """
    Time Complexity O(VlogE)
    Memory Complexity O(V + E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for _ in range(m):
        from_, to, time = map(int, sys.stdin.readline().rstrip().split())
        adj_list[from_].append((to, time))
        adj_list[to].append((from_, time))
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    dist_a: dict[int, list[tuple[int, int]]] = dijkstra(a, adj_list, n)
    dist_b: dict[int, list[tuple[int, int]]] = dijkstra(b, adj_list, n)
    dist_c: dict[int, list[tuple[int, int]]] = dijkstra(c, adj_list, n)
    if dist_a[b] == float('inf') or dist_a[c] == float('inf') or dist_b[c] == float('inf'):
        sys.stdout.write('-1\n')
        return
    min_time: int = float('inf')
    if dist_a[b] != float('inf') and dist_b[c] != float('inf'):
        min_time = min(min_time, dist_a[b] + dist_b[c])
    
    if dist_a[c] != float('inf') and dist_c[b] != float('inf'):
        min_time = min(min_time, dist_a[c] + dist_c[b])
    
    if dist_b[a] != float('inf') and dist_a[c] != float('inf'):
        min_time = min(min_time, dist_b[a] + dist_a[c])
    
    if dist_b[c] != float('inf') and dist_c[a] != float('inf'):
        min_time = min(min_time, dist_b[c] + dist_c[a])
    
    if dist_c[a] != float('inf') and dist_a[b] != float('inf'):
        min_time = min(min_time, dist_c[a] + dist_a[b])
    
    if dist_c[b] != float('inf') and dist_b[a] != float('inf'):
        min_time = min(min_time, dist_c[b] + dist_b[a])
    sys.stdout.write('{}\n'.format([min_time, -1][min_time == float('inf')]))


if __name__ == '__main__':
    solution()