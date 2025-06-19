import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    s: str = sys.stdin.readline().rstrip()
    n: int = len(s)
    t: str = s + s
    lcp: list[int] = [-1] * (2 * n)
    k: int = 0
    for right in range(1, 2 * n):
        left: int = lcp[right - k - 1]
        while left != -1 and t[right] != t[k + left + 1]:
            if t[right] < t[k + left + 1]: k = right - left - 1 
            left = lcp[left]
        if left == -1 and t[right] != t[k + left + 1]:
            if t[right] < t[k + left + 1]: k = right
            lcp[right - k] = -1
        else:
            lcp[right - k] = left + 1
    sys.stdout.write(''.join(s[k:]))
    sys.stdout.write(''.join(s[:k]))
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()