import sys


def solution() -> None:
    """
    Time Complexity O(N^3)
    Memory Complexity O(N^3)
    """
    s: str = sys.stdin.readline().rstrip()
    n: int = len(s)
    dp: list[list[list[str]]] = [[''] * n for _ in range(n)]
    for i in range(n): dp[i][i] = [s[i]]
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right: int = left + length - 1
            dp[left][right] = list(s[left:left + length])
            for k in range(left, right):
                candidate: list[str] = dp[left][k] + dp[k + 1][right]
                if len(candidate) < len(dp[left][right]): dp[left][right] = candidate
            sub: str = s[left:left + length]
            sub_len: int = len(sub)
            for k in range(1, sub_len // 2 + 1):
                if sub_len % k != 0: continue
                is_repeat: bool = True
                for l in range(k, sub_len):
                    if sub[l] != sub[l % k]:
                        is_repeat = False
                        break
                if is_repeat:
                    compressed: list[str] = [str(sub_len // k), '('] + dp[left][left + k - 1] + [')']
                    if len(compressed) < len(dp[left][right]): dp[left][right] = compressed
    sys.stdout.write('{}\n'.format(''.join(dp[0][n - 1])))


if __name__ == '__main__':
    solution()