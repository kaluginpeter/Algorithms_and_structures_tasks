import sys


def binary_search(nums: list[int], target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    answer_diff: int = float('inf')
    answer: int = float('inf')
    while left <= right:
        middle: int = left + ((right - left) >> 1)

        middle_diff: int = abs(nums[middle] - target)
        if answer_diff > middle_diff:
            answer = nums[middle]
            answer_diff = middle_diff
        elif answer_diff == middle_diff:
            answer = min(answer, nums[middle])

        if nums[middle] >= target:
            right = middle - 1
        else:
            left = middle + 1

    return answer


def solution() -> None:
    """
    Time Complexity O(logN)
    Memory Complexity O(1)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    queries: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(k):
        target: int = next(queries)
        sys.stdout.write(str(binary_search(nums, target)) + '\n')


if __name__ == '__main__':
    solution()