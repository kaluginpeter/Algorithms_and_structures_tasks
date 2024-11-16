import sys


def solution(n: int, m: int, matrix: list[list[int]], row: int, col: int) -> str:
    """
    Time Complexity O(1)
    Memory Complexity O(1)
    """
    neighbors: list[int] = []
    dirs: list[tuple[int, int]] = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for dir_row, dir_col in dirs:
        next_row, next_col = row + dir_row, col + dir_col
        if 0 <= next_row < n and 0 <= next_col < m:
            neighbors.append(matrix[next_row][next_col])
    neighbors.sort()
    return ' '.join(str(neighbor) for neighbor in neighbors)


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    matrix: list[list[int]] = []
    for _ in range(n):
        row: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        matrix.append(row)
    row: int = int(sys.stdin.readline().rstrip())
    col: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(n, m, matrix, row, col))
