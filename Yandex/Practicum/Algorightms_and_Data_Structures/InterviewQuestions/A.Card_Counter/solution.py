from __future__ import annotations
import sys


def solution() -> None:
    """
    Time Complexity O(k)
    Memory Complexity O(k)
    """
    n: int = int(sys.stdin.readline().rstrip())
    k: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    cur_sum: int = sum(nums[:k])
    max_sum: int = cur_sum
    right: int = n - 1
    for left in range(k - 1, -1, -1):
        cur_sum -= nums[left]
        cur_sum += nums[right]
        right -= 1
        if cur_sum > max_sum: max_sum = cur_sum
    sys.stdout.write('{}\n'.format(max_sum))


if __name__ == '__main__':
    solution()