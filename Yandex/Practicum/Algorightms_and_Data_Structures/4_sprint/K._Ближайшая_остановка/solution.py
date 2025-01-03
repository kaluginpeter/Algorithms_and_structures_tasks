import sys
from collections import defaultdict

def euclidean_distance_squared(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def solution(n_points, m_points):
    """
    Time Complexity O(N + M + NK)
    Memory Complexity O(N + M)
    """
    max_distance: int = 20
    grid_size: int = max_distance
    grid: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)

    for idx, (x, y) in enumerate(m_points):
        cell_x: int = x // grid_size
        cell_y: int = y // grid_size
        grid[(cell_x, cell_y)].append((x, y))

    max_count: int = 0
    best_point_index: int = -1

    for idx, (x_n, y_n) in enumerate(n_points):
        count: int = 0
        cell_x_n: int = x_n // grid_size
        cell_y_n: int = y_n // grid_size

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                current_cell: tuple[int, int] = (cell_x_n + dx, cell_y_n + dy)
                if current_cell in grid:
                    for (x_m, y_m) in grid[current_cell]:
                        if euclidean_distance_squared((x_n, y_n), (x_m, y_m)) <= max_distance ** 2:
                            count += 1
        if count > max_count:
            max_count = count
            best_point_index = idx

    sys.stdout.write(f'{best_point_index + 1}\n')

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    n_points: list[tuple[int, int]] = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        n_points.append((x, y))
    m: int = int(sys.stdin.readline().rstrip())
    m_points: list[tuple[int, int]] = []
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        m_points.append((x, y))
    solution(n_points, m_points)
