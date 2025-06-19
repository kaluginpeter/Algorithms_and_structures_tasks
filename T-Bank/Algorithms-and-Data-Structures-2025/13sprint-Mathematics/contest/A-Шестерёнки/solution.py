import sys


def gcd(x: int, y: int) -> int:
    if x == 0: return y
    return gcd(y % x, x)


def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)


def solution() -> None:
    """
    Time Complexity O(log(N))
    Memory Complexity O(log(N))
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write('{}\n'.format(lcm(n, k)))


if __name__ == '__main__':
    solution()