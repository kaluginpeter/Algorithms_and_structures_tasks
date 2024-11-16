import sys


def solution(n: int, nums: list[int]) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    output: int = 0
    for idx in range(n):
        if (not idx or nums[idx - 1] < nums[idx]) and (idx + 1 == n or nums[idx] > nums[idx + 1]):
            output += 1
    sys.stdout.write(str(output) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, nums)
