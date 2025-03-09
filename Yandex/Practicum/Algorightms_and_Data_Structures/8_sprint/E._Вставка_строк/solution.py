import sys


def solution() -> None:
    """
    Time Complexity O(N + M)
    Memory Complexity O(M)
    """
    s: str = sys.stdin.readline().rstrip()
    n: int = int(sys.stdin.readline().rstrip())
    gifts: dict[int, str] = dict()
    for _ in range(n):
        t, k = sys.stdin.readline().rstrip().split()
        gifts[int(k)] = t
    for i in range(len(s)):
        if i in gifts:
            sys.stdout.write(gifts[i])
        sys.stdout.write(s[i])
    if len(s) in gifts:
        sys.stdout.write(gifts[len(s)])
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()