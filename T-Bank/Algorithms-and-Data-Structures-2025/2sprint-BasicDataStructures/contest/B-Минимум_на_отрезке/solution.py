import sys
from collections import deque


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(K)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    output: list[int] = []
    dq: deque[int] = deque()
    for idx in range(n):
        if dq and idx - dq[0] + 1 > k:
            dq.popleft()
        while dq and nums[dq[-1]] > nums[idx]:
            dq.pop()
        dq.append(idx)
        if idx >= k - 1:
            output.append(nums[dq[0]])
    sys.stdout.write(' '.join(str(min_num) for min_num in output))
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution() 