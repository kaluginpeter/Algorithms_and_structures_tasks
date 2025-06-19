import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(range(1, n + 1))
    for idx in range(2, n):
        nums[idx], nums[idx // 2] = nums[idx // 2], nums[idx]
    sys.stdout.write(' '.join(str(num) for num in nums))
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()