import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    a: str = sys.stdin.readline().rstrip()
    n: int = len(a)
    lcp: list[int] = [0] * n
    for i in range(1, n):
        k: int = lcp[i - 1]
        while k and a[k] != a[i]: k = lcp[k - 1]
        if a[k] == a[i]: k += 1
        lcp[i] = k
    sys.stdout.write(' '.join(str(p) for p in lcp) + '\n')


if __name__ == '__main__':
    solution()