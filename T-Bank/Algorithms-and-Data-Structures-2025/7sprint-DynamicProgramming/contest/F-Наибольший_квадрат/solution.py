import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(NM)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    matrix: list[list[int]] = []
    for _ in range(n):
        row: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        matrix.append(row)
    dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    max_square: int = 0
    max_square_row = max_square_col = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if not matrix[r - 1][c - 1]: continue
            dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1]) + 1
            if dp[r][c] > max_square:
                max_square = dp[r][c]
                max_square_row = r - dp[r][c] + 1
                max_square_col = c - dp[r][c] + 1
    sys.stdout.write('{}\n{} {}\n'.format(max_square, max_square_row, max_square_col))

if __name__ == '__main__':
    solution()