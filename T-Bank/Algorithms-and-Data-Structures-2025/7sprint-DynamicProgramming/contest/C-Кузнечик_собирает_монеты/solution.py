import sys
from collections import deque


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = [0, 0] + list(map(int, sys.stdin.readline().rstrip().split()))
    nums.append(0)
    dp: list[int] = [float('inf')] * (n + 1)
    dp[1] = 0
    q: list[int] = deque()
    q.append(1)
    prev: list[int] = [-1] * (n + 1)
    for i in range(2, n + 1):
        if q and q[0] < i - k: q.popleft()
        dp[i] = dp[q[0]] + nums[i]
        prev[i] = q[0]
        while q and dp[q[-1]] <= dp[i]: q.pop()
        q.append(i)
    path: list[int] = [n]
    i: int = n
    while prev[i] != -1:
        path.append(prev[i])
        i = prev[i]
    sys.stdout.write('{}\n{}\n{}\n'.format(dp[n], len(path) - 1, ' '.join(str(move) for move in reversed(path))))


if __name__ == '__main__':
    solution()