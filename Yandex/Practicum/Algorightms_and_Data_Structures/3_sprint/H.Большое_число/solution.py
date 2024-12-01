import sys
from functools import cmp_to_key

def comparator(x: str, y: int) -> bool:
    if x + y > y + x:
        return -1
    return 1

def solution(n: int, nums: list[str]) -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    sys.stdout.write(''.join(sorted(nums, key=cmp_to_key(comparator))) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[str] = sys.stdin.readline().rstrip().split()
    solution(n, nums)
