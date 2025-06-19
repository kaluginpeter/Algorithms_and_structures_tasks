import sys


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    segments: list[tuple[int, int]] = []
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        segments.append((start, end))
    segments.sort()
    output: int = 0
    prev_start: int = -2 * 10**9
    prev_end: int = -2 * 10**9
    for start, end in segments:
        if start <= prev_end: prev_end = max(prev_end, end)
        else:
            output += prev_end - prev_start
            prev_start, prev_end = start, end
    output += prev_end - prev_start
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    solution()