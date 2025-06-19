import sys


def solution() -> None:
    """
    Time Complexity O(N**3)
    Memory Complexity O(N**2)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    grid: list[list[int]] = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): grid[i][i] = 0;
    for _ in range(m):
        source, destination, weight = map(int, sys.stdin.readline().rstrip().split())
        grid[source][destination] = min(grid[source][destination], weight)
        grid[destination][source] = min(grid[destination][source], weight)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
    start_town: int = 0
    max_distance: int = float('inf')
    for town in range(1, n + 1):
        max_town_distance: int = max(grid[town][1:])
        if max_town_distance < max_distance:
            start_town = town
            max_distance = max_town_distance
    sys.stdout.write('{}\n'.format(start_town))


if __name__ == '__main__':
    solution()