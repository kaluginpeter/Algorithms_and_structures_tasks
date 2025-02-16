import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(M)
    """
    m: int = int(sys.stdin.readline().rstrip())
    n: int = int(sys.stdin.readline().rstrip())
    coins: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    dp: list[int] = [0] * (m + 1)
    dp[0] = 1
    for i in range(n):
        for exchange in range(coins[i], m + 1):
            dp[exchange] += dp[exchange - coins[i]]
    sys.stdout.write(f'{dp[m]}\n')


if __name__ == '__main__':
    solution()