import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    a: str = sys.stdin.readline().rstrip()
    b: str = sys.stdin.readline().rstrip()
    n: int = len(a)
    m: int = len(b)
    if abs(n - m) > 1:
        sys.stdout.write('FAIL\n')
        return
    if n < m:
        a, b = b, a
        n, m = m, n
    left: int = 0
    right: int = 0
    already_skipped: bool = False
    while left < n and right < m:
        if a[left] == b[right]:
            left += 1
            right += 1
        elif not already_skipped:
            already_skipped = True
            if n != m: left += 1
            else:
                left += 1
                right += 1
        else:
            sys.stdout.write('FAIL\n')
            return
    sys.stdout.write(['FAIL', 'OK'][(left == n and right == m) or not already_skipped] + '\n')


if __name__ == '__main__':
    solution()