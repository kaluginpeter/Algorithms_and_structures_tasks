import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    a: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    m: int = int(sys.stdin.readline().rstrip())
    b: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    for left in range(n - m + 1):
        match: bool = True
        diff: int = a[left] - b[0]
        if all(a[left + right] - b[right] == diff for right in range(1, m)):
            sys.stdout.write(f'{left + 1} ')
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()