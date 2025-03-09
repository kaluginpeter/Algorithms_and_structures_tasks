import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    sequence: str = sys.stdin.readline().rstrip()
    n: int = len(sequence)
    lcp: list[int] = [0] * n
    for i in range(1, n):
        k: int = lcp[i - 1]
        while k and sequence[k] != sequence[i]: k = lcp[k - 1]
        if sequence[k] == sequence[i]: k += 1
        lcp[i] = k
    sys.stdout.write('{}\n'.format([1, n // (n - lcp[-1])][n % (n - lcp[-1]) == 0]))


if __name__ == '__main__':
    solution()