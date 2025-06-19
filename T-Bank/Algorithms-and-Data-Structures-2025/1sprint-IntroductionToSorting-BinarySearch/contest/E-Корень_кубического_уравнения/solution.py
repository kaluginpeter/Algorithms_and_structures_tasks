import sys


def f(x: float, a: int, b: int, c: int, d: int) -> float:
    return a * x**3.0 + b * x**2.0 + c * x + d


def solution() -> None:
    """
    Time Complexity O(log(10^9))
    Memory Complexity O(1)
    """
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    left: float = -10**10
    right: float = 10**10

    while right - left > 1e-8:
        middle: float = left + (right - left) / 2.0
        root: float = f(middle, a, b, c, d)
        if root == 0:
            left = right = middle
            break
        elif f(left, a, b, c, d) * f(middle, a, b, c, d) < 0: right = middle
        else: left = middle

    sys.stdout.write(f'{left + (right - left) / 2:.4f}\n')


if __name__ == '__main__':
    solution()