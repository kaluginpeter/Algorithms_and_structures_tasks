import sys


def solution() -> None:
    """
    Time Complexity O(N^2)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    prev: list[int] = [-1] * n
    dp: list[int] = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    i: int = 0
    for j in range(1, n):
        if dp[i] < dp[j]: i = j
    path: list[int] = [nums[i]]
    while prev[i] != -1:
        path.append(nums[prev[i]])
        i = prev[i]
    sys.stdout.write('{}\n'.format(len(path)))
    sys.stdout.write('{}\n'.format(' '.join(str(move) for move in reversed(path))))


if __name__ == '__main__':
    solution()