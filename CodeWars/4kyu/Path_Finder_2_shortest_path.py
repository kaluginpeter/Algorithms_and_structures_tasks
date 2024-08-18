# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return the minimal number of steps to exit position [N-1, N-1] if it is possible to reach the exit from the starting position. Otherwise, return false.
#
# Empty positions are marked .. Walls are marked W. Start and exit positions are guaranteed to be empty in all test cases.
#
# Path Finder Series:
# #1: can you reach the exit?
# #2: shortest path
# #3: the Alpinist
# #4: where are you?
# #5: there's someone here
# ALGORITHMS
# Solution
from collections import deque
def path_finder(maze):
    maze = maze.split('\n')
    queue = deque()
    seen = set()
    queue.append((0, 0))
    seen.add((0, 0))
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    length = 0
    n = len(maze)
    while queue:
        for _ in range(len(queue)):
            cur_r, cur_c = queue.popleft()
            if cur_r == cur_c == n - 1:
                return length
            for move in moves:
                nxt_r, nxt_c = cur_r + move[0], cur_c + move[1]
                if min(nxt_r, nxt_c) < 0 or max(nxt_r, nxt_c) >= n or maze[nxt_r][nxt_c] == 'W' or (nxt_r, nxt_c) in seen:
                    continue
                queue.append((nxt_r, nxt_c))
                seen.add((nxt_r, nxt_c))
        length += 1
    return False