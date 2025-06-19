import sys


def get_le(middle: int, n: int) -> int:
    le: int = 0
    for num in range(1, n + 1):
        le += min(middle // num, n)
    return le


def solution() -> None:
    """
    Time Complexity O(Nlog(N^2))
    Memory Complexity O(1)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    left: int = 1
    right: int = n * n
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if get_le(middle, n) < k: left = middle + 1 
        else: right = middle - 1 
    sys.stdout.write('{}\n'.format(left))


if __name__ == '__main__':
    solution()