import sys


def solution(n: int, nums: list[int]) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    zeros_idx: int = 0
    twos_idx: int = n - 1
    ones_idx: int = 0
    while ones_idx <= twos_idx:
        if nums[ones_idx] == 0:
            nums[ones_idx], nums[zeros_idx] = nums[zeros_idx], nums[ones_idx]
            if zeros_idx == ones_idx:
                ones_idx += 1
            else:
                zeros_idx += 1
        elif nums[ones_idx] == 2:
            nums[ones_idx], nums[twos_idx] = nums[twos_idx], nums[ones_idx]
            twos_idx -= 1
        else:
            ones_idx += 1

    for idx in range(n):
        if idx:
            sys.stdout.write(' ')
        sys.stdout.write(str(nums[idx]))


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, nums)
