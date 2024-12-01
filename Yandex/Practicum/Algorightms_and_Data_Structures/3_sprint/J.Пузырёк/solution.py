import sys


def solution(n: int, nums: list[int]) -> None:
    """
    Time Complexity O(N**2)
    Memory Complexity O(1)
    """
    has_change: bool = False
    already_sorted: bool = True
    for i in range(n - 1, -1, -1):
        has_change = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                already_sorted = False
                has_change = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if has_change:
            sys.stdout.write(' '.join(map(str, nums)) + '\n')
    if already_sorted:
        sys.stdout.write(' '.join(map(str, nums)) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, nums)
