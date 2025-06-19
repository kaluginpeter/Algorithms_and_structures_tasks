import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(NM)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    dp: list[list[int]] = [[0] * m for _ in range(n)]
    moves: list[tuple[int, int]] = [
        (-1, -2), (-2, -1), (1, -2), (-2, 1)
    ]
    dp[0][0] = 1
    main_r: int = 0
    while main_r < n:
        r: int = main_r
        c: int = 0
        while r >= 0 and c < m:
            for x, y in moves:
                next_r: int = r + x
                next_c: int = c + y
                if (0 <= next_r < n) and (0 <= next_c < m):
                    dp[r][c] += dp[next_r][next_c]
            r -= 1 
            c += 1
        main_r += 1

    main_c: int = 1
    while main_c < m:
        r: int = n - 1
        c: int = main_c
        while r >= 0 and c < m:
            for x, y in moves:
                next_r: int = r + x
                next_c: int = c + y
                if (0 <= next_r < n) and (0 <= next_c < m):
                    dp[r][c] += dp[next_r][next_c]
            r -= 1 
            c += 1
        main_c += 1
    sys.stdout.write('{}\n'.format(dp[n - 1][m - 1]))


if __name__ == '__main__':
    solution()