import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(NM)
    """
    a: str = sys.stdin.readline().rstrip()
    b: str = sys.stdin.readline().rstrip()
    n, m = len(a), len(b)
    dp: list[list[list[int]]] = [[[float('inf')] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0][0] = i
        dp[i][0][1] = i
    for j in range(m + 1):
        dp[0][j][0] = j
        dp[0][j][1] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j][0] = min(
                dp[i - 1][j - 1][0] + int(a[i - 1] != b[j - 1]),
                dp[i - 1][j][0] + 1,
                dp[i][j - 1][0] + 1,
            )
            if i >= 2 and j >= 2 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                dp[i][j][1] = dp[i - 2][j - 2][0] + 1
            else: dp[i][j][1] = float('inf')
            dp[i][j][0] = min(dp[i][j][0], dp[i][j][1])
    sys.stdout.write('{}\n'.format(dp[n][m][0]))


if __name__ == '__main__':
    solution()