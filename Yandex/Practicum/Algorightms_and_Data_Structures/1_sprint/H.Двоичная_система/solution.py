import sys


def solution(x: str, y: str) -> None:
    """
    Time Complexity O(N), where N is the length of place values of the largest number
    Memory Complexity O(N), where N is the length of place values of the largest number
    """
    digits: list[str] = []
    x_n: int = len(x)
    y_n: int = len(y)
    if x_n < y_n:
        x, y = y, x
        x_n, y_n = y_n, x_n
    y_idx: int = y_n - 1
    addition: int = 0
    for x_idx in range(x_n - 1, -1, -1):
        if y_idx >= 0:
            bits: int = int(x[x_idx]) + int(y[y_idx])
            if addition:
                bits += 1
                addition -= 1
            if bits > 1:
                digits.append('1' if bits == 3 else '0')
                addition += 1
            else:
                digits.append(str(bits))
            y_idx -= 1
        elif addition:
            bits: int = int(x[x_idx]) + addition
            addition -= 1
            if bits == 2:
                addition += 1
            digits.append('0' if bits == 2 else str(bits))
        else:
            digits.append(x[x_idx])

    if addition:
        digits.append('1')
    n: int = len(digits)
    for idx in range(n - 1, -1, -1):
        sys.stdout.write(digits[idx])
    sys.stdout.write('\n')


if __name__ == '__main__':
    x: str = sys.stdin.readline().rstrip()
    y: str = sys.stdin.readline().rstrip()
    solution(x, y)
