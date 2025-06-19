import sys


def binary_search(nums: list[int], target: int) -> str:
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if nums[middle] == target: return 'YES'
        elif nums[middle] > target: right = middle - 1
        else: left = middle + 1
    return 'NO'


def solution() -> None:
    """
    Time Complexity O(log(N))
    Memory Complexity O(1)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    queries: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(k):
        target: int = next(queries)
        sys.stdout.write(binary_search(nums, target) + '\n')


if __name__ == '__main__':
    solution()