# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
#
# Empty positions are marked ..
# Walls are marked W.
# Start and exit positions are empty in all test cases.
# Path Finder Series:
# #1: can you reach the exit?
# #2: shortest path
# #3: the Alpinist
# #4: where are you?
# #5: there's someone here
# ALGORITHMS
# Solution
def path_finder(maze):
    maze = maze.split('\n')
    n = len(maze)
    queue = dict()
    queue[(n - 1, n - 1)] = 0
    cache = set()
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        k, v = queue.popitem()
        current_row, current_col = k
        if current_row == current_col ==  0:
            return True
        cache.add((current_row, current_col))
        for move in moves:
            nxt_row, nxt_col = current_row + move[0], current_col + move[1]
            if (nxt_row, nxt_col) in cache:
                continue
            elif not (0 <= nxt_row < n) or not (0 <= nxt_col < n):
                continue
            elif maze[nxt_row][nxt_col] == 'W':
                continue
            queue[(nxt_row, nxt_col)] = 0
    return False