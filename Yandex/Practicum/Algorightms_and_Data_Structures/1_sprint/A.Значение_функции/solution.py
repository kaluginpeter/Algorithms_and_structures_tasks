import sys


def solution(a: int, x: int, b: int, c: int) -> int:
    """
    Time Complexity O(1)
    Memory Complexity O(1)
    """
    return a * x**2 + b * x + c


if __name__ == '__main__':
    a, x, b, c = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(a, x, b, c)))