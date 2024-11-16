import sys


def solution(n: int) -> None:
    """
    Time Complexity O(log4 N)
    Memory Complexity O(1)
    """
    cur_n: int = 1
    upper_bound: int = 10_001
    is_valid: bool = False
    while cur_n < upper_bound:
        if cur_n == n:
            is_valid = True
            break
        cur_n *= 4
    sys.stdout.write('True' if is_valid else 'False')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    solution(n)
