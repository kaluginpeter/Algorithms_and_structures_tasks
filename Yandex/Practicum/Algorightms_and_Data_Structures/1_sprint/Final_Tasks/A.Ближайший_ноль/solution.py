import sys


def solution(n: int, nums: list[int]) -> list[int]:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    Topics: Prefix/Suffix Approach
    """
    prefix: list[int] = []
    nearest_prefix_zero_idx: int = -n
    for cur_idx in range(n):
        if nums[cur_idx] == 0:
            nearest_prefix_zero_idx = cur_idx
        distance: int = cur_idx - nearest_prefix_zero_idx
        prefix.append(distance)

    nearest_suffix_zero_idx = 0
    for cur_idx in range(n - 1, -1, -1):
        if nums[cur_idx] == 0:
            nearest_suffix_zero_idx = cur_idx
        distance: int = abs(cur_idx - nearest_suffix_zero_idx)
        nums[cur_idx] = min(prefix[cur_idx], distance)
    return nums


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    print(*solution(n, nums))