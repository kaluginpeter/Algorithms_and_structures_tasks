import sys
from collections import defaultdict
import heapq


def check(cups: int, adj_list: dict[int, list[tuple[int, int, int]]], n: int) -> bool:
    dist: list[int] = [float('inf')] * (n + 1)
    dist[1] = 0
    min_heap: list[tuple[int, int]] = []
    heapq.heappush(min_heap, (0, 1))
    while min_heap:
        time, city = heapq.heappop(min_heap)
        if city == n: return True
        if time > dist[city]: continue
        for another_city, cost, bound in adj_list[city]:
            new_time: int = time + cost
            if cups * 100 <= bound and new_time <= 1440 and new_time < dist[another_city]:
                dist[another_city] = new_time
                heapq.heappush(min_heap, (new_time, another_city))
    
    return dist[n] <= 1440


def solution() -> None:
    """
    Time Complexity O((VlogE)log(M))
    Memory Complexity O(E)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for _ in range(m):
        from_, to, time, bound = map(int, sys.stdin.readline().rstrip().split())
        bound = max(0, bound - 3000000)
        adj_list[from_].append((to, time, bound))
        adj_list[to].append((from_, time, bound))
    left, right, output = 0, 10000000, 0
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if check(middle, adj_list, n):
            output = middle
            left = middle + 1
        else: right = middle - 1
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    solution()