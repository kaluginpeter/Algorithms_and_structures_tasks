import sys

PRECISE: float = 0.000001

def solution() -> None:
    """
    Time Complexity O(logN)
    Memory Complexity O(1)
    """
    c: float = float(sys.stdin.readline().rstrip())
    left: float = 0
    right: float = c
    while abs(left - right) != 0:
        middle: float = left + (right - left) / 2
        c_prime: float = middle**2 + (middle + 1)**.5
        if abs(c - c_prime) <= PRECISE:
            sys.stdout.write(f'{middle}\n')
            return
        elif c_prime > c: right = middle
        else: left = middle


if __name__ == '__main__':
    solution()
