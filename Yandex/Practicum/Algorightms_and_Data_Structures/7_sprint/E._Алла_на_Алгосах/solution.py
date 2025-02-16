import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(M)
    """
    x: int = int(sys.stdin.readline().rstrip())
    k: int = int(sys.stdin.readline().rstrip())
    coins: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    dp: list[int] = [10_001] * (x + 1)
    dp[0] = 0
    for exchange in range(1, x + 1):
        for coin in coins:
            if coin > exchange: continue
            dp[exchange] = min(dp[exchange], dp[exchange - coin] + 1)
    sys.stdout.write(f'{dp[x] if dp[x] != 10_001 else -1}\n')


if __name__ == '__main__':
    solution()