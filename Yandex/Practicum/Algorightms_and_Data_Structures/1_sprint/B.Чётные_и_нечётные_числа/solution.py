import sys


def solution(a: int, b: int, c: int) -> str:
    """
    Time Complexity O(1)
    Memory Complexity O(1)
    """
    diff: int = abs(a % 2) + abs(b % 2) + abs(c % 2)
    return 'WIN' if diff == 3 or diff == 0 else 'FAIL'


if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(solution(a, b, c))