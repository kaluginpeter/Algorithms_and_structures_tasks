import sys


def solution() -> None:
    """
    Time Complexity O(N^2)
    Memory Complexity O(N^2)
    """
    s: str = sys.stdin.readline().rstrip()
    n: int = len(s)
    dp: list[list[int]] = [[0] * n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right: int = left + length - 1
            if s[left] == s[right]: dp[left][right] = 2 + [dp[left + 1][right - 1], 0][length == 2]
            else: dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])
    length: int = dp[0][n - 1]
    output: list[str] = []
    left: int = 0
    right: int = n - 1
    while left <= right:
        if s[left] == s[right]:
            output.append(s[left])
            left += 1
            right -= 1
        else:
            if dp[left + 1][right] > dp[left][right - 1]: left += 1
            else: right -= 1
    reversed_part: list[str] = output[:len(output) - (length & 1):][::-1]
    output.extend(reversed_part)
    sys.stdout.write('{}\n{}\n'.format(len(output), ''.join(output)))


if __name__ == '__main__':
    solution()