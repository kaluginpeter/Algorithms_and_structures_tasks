import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    s: str = sys.stdin.readline().rstrip()
    p: str = sys.stdin.readline().rstrip()
    t: str = sys.stdin.readline().rstrip()
    sentinel: str = ''.join([p, '#', s])
    matching: list[int] = []
    lcp: list[int] = [0] * len(p)
    prev_k: int = 0
    for i in range(1, len(sentinel)):
        k: int = prev_k
        while k and sentinel[k] != sentinel[i]: k = lcp[k - 1]
        if sentinel[k] == sentinel[i]: k += 1
        if i < len(p): lcp[i] = k
        prev_k = k
        if k == len(p): matching.append(i - 2 * len(p))
    matching.reverse()
    i: int = 0
    while i < len(s):
        if matching and matching[-1] == i:
            sys.stdout.write(t)
            matching.pop()
            i += len(p)
        else:
            sys.stdout.write(s[i])
            i += 1
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()