import sys

def get_pairs_less_or_equal_that_diff(diff: int, nums: list[int]) -> int:
    pairs: int = 0
    right: int = 0
    for left in range(len(nums)):
        while (right < len(nums) and nums[right] - nums[left] <= diff):
            right += 1
        pairs += right - left - 1
    return pairs

def solution(n: int, nums: list[int], k: int) -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    nums.sort()
    left: int = 0
    right: int = nums[-1] - nums[0]
    while left <= right:
        middle: int = left + (right - left) // 2
        if get_pairs_less_or_equal_that_diff(middle, nums) < k:
            left = middle + 1
        else:
            right = middle - 1
    sys.stdout.write(str(right + 1) + '\n')

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    k: int = int(sys.stdin.readline().rstrip())
    solution(n, nums, k)