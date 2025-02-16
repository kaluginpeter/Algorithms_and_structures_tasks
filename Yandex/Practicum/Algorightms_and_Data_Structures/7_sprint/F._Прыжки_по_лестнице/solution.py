import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(N)
    """
    MOD: int = 1000000007
    n, k = map(int, sys.stdin.readline().rstrip().split())
    dp: list[int] = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for prev in range(max(1, i - k), i):
            dp[i] = (dp[i] % MOD + dp[prev] % MOD) % MOD
    sys.stdout.write(f'{dp[n]}\n')


if __name__ == '__main__':
    solution()