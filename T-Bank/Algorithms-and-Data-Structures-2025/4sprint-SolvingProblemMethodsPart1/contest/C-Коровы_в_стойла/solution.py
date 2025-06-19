import sys


def can_place(dist: int, k: int, nums: list[int]) -> bool:
    prev: int = 0
    for num in nums:
        if num >= prev:
            k -= 1 
            prev = num + dist
    return k <= 0


def solution() -> None:
    """
    Time Complexity O(NlogM)
    Memory Complexity O(1)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    left: int = 1
    right: int = nums[-1]
    answer: int = 0
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if can_place(middle, k, nums):
            answer = middle
            left = middle + 1 
        else: right = middle - 1 
    sys.stdout.write('{}\n'.format(answer))


if __name__ == '__main__':
    solution()