import sys


def is_matching_pair(a: str, b: str) -> bool:
    return (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}')


def solution() -> None:
    """
    Time Complexity O(N**3)
    Memory Complexity O(N**3)
    """
    s: str = sys.stdin.readline().rstrip()
    n: int = len(s)
    dp: list[list[int]] = [[0] * n for _ in range(n)]
    path: list[list[str]] = [[''] * n for _ in range(n)]
    for ln in range(2, n + 1):
        for left in range(n - ln + 1):
            right: int = left + ln - 1
            if is_matching_pair(s[left], s[right]):
                if ln == 2:
                    dp[left][right] = 2
                    path[left][right] = s[left] + s[right]
                else:
                    dp[left][right] = 2 + dp[left + 1][right - 1]
                    path[left][right] = s[left] + path[left + 1][right - 1] + s[right]
            for k in range(right):
                if dp[left][right] < dp[left][k] + dp[k + 1][right]:
                    dp[left][right] = dp[left][k] + dp[k + 1][right]
                    path[left][right] = path[left][k] + path[k + 1][right]
    sys.stdout.write('{}\n'.format(path[0][n - 1]))

if __name__ == '__main__':
    solution()