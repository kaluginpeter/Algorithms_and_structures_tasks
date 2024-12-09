import sys


def solution(n: int, nums: list[int]) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    blocks: int = 0
    threshold: int = 0
    for idx in range(n):
        if nums[idx] > idx:
            threshold = max(threshold, nums[idx])
        if idx >= threshold:
            blocks += 1
            threshold = 0
    sys.stdout.write(str(blocks) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, nums)
