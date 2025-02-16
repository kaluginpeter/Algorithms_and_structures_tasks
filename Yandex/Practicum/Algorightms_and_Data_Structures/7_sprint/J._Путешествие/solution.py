import sys


def solution() -> None:
    """
    Time Complexity O(N^2)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    dp: list[int] = [0] * (n + 1)
    paths: list[list[int]] = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i):
            if nums[j - 1] < nums[i - 1] and dp[i] < dp[j]:
                dp[i] = dp[j]
                paths[i] = paths[j].copy()
        dp[i] += 1
        paths[i].append(i)
    lis_idx: int = 0
    for idx in range(1, n + 1):
        if dp[idx] > dp[lis_idx]: lis_idx = idx
    sys.stdout.write(str(dp[lis_idx]) + '\n')
    if dp[lis_idx]:
        sys.stdout.write(' '.join(str(idx) for idx in paths[lis_idx]) + '\n')


if __name__ == '__main__':
    solution()