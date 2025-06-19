import sys


def solution() -> None:
    """
    Time Complexity O(logN)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    left: int = 1
    right: int = n
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        sys.stdout.write(f'{middle}\n')
        sys.stdout.flush()
        sign: str = sys.stdin.readline().rstrip()
        if sign == '>=':
            left = middle + 1
        else:
            right = middle - 1
    sys.stdout.write(f'! {right}\n')


if __name__ == '__main__':
    solution()