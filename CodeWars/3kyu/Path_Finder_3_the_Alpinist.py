# Task
# You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1]. Number of climb rounds between adjacent locations is defined as difference of location altitudes (ascending or descending).
#
# Location altitude is defined as an integer number (0-9).
#
# Path Finder Series:
# #1: can you reach the exit?
# #2: shortest path
# #3: the Alpinist
# #4: where are you?
# #5: there's someone here
# ALGORITHMS
# Solution
from heapq import heappop, heappush
def path_finder(area):
    mtrx = [list(map(int, line)) for line in area.split('\n')]
    n = len(mtrx)
    heap = [(0, 0, 0)]
    costs = [[float('inf')] * n for _ in range(n)]
    costs[0][0] = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while heap:
        current_cost, cur_r, cur_c = heappop(heap)
        if cur_r == cur_c == n - 1:
            return current_cost
        for dr, dc in directions:
            nxt_r, nxt_c = cur_r + dr, cur_c + dc
            if 0 <= nxt_r < n and 0 <= nxt_c < n:
                climb_cost = abs(mtrx[nxt_r][nxt_c] - mtrx[cur_r][cur_c])
                new_cost = current_cost + climb_cost
                if new_cost < costs[nxt_r][nxt_c]:
                    costs[nxt_r][nxt_c] = new_cost
                    heappush(heap, (new_cost, nxt_r, nxt_c))