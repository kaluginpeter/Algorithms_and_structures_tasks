import sys


def solution(num: int) -> None:
    """
    Time Complexity O(N), where N is length of place values
    Memory Complexity O(N), where N is length of place values
    """
    if not num:
        sys.stdout.write('0\n')
        return
    base: int = 2
    digits: list[int] = []
    while num:
        digits.append(num % base)
        num //= base
    digits_length: int = len(digits)
    for idx in range(digits_length - 1, -1, -1):
        sys.stdout.write(str(digits[idx]))
    sys.stdout.write('\n')


if __name__ == '__main__':
    num: int = int(sys.stdin.readline().rstrip())
    solution(num)
