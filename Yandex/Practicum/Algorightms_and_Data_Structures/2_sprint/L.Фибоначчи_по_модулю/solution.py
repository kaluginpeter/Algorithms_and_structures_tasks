import sys


def solution(n: int, k: int) -> int:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    x = y = 1
    bound: int = 10**k
    for _ in range(1, n):
        x, y = y % bound, (x + y) % bound
    return y % bound


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(n, k)) + '\n')

