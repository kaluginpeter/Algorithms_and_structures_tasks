import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    dp: list[int] = [0] * (n + 1)
    dp[1] = nums[1]
    for level in range(2, n + 1):
        dp[level] = min(dp[level - 1], dp[level - 2]) + nums[level]
    sys.stdout.write('{}\n'.format(dp[n]))


if __name__ == '__main__':
    solution()