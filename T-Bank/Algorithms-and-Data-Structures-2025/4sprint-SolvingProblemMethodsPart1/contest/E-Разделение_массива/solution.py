import sys


def can_distribute(n: int, k: int, nums: list[int], bound: int) -> bool:
    k -= 1
    cur_sum: int = 0
    for num in nums:
        if cur_sum + num > bound:
            k -= 1
            cur_sum = num
        else: cur_sum += num
    return k >= 0


def solution() -> None:
    """
    Time Complexity O(NlogM)
    Memory Complexity O(1)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    left: int = max(nums)
    right: int = sum(nums)
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if can_distribute(n, k, nums, middle): right = middle - 1
        else: left = middle + 1
    sys.stdout.write('{}\n'.format(left))


if __name__ == '__main__':
    solution()