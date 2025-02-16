import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(NM)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    grid: list[str] = []
    for _ in range(n):
        row: str = sys.stdin.readline().rstrip()
        grid.append(row)
    grid.reverse()
    dp: list[list[int]] = [[0] * m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            dp[row][col] = int(grid[row][col]) + max((dp[row - 1][col] if row else 0), (dp[row][col - 1] if col else 0))
    sys.stdout.write(f'{dp[n - 1][m - 1]}\n')
    stacktrace: list[str] = []
    row, col = n - 1, m - 1
    while row or col:
        right: int = dp[row][col - 1] if col else float('-inf')
        up: int = dp[row - 1][col] if row else float('-inf')
        if right >= up:
            stacktrace.append('R')
            col -= 1
        else:
            stacktrace.append('U')
            row -= 1
    stacktrace.reverse()
    sys.stdout.write(''.join(stacktrace) + '\n')



if __name__ == '__main__':
    solution()