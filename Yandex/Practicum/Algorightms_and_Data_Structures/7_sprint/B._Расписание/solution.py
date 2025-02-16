import sys


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    events: list[tuple[float, float]] = []
    for _ in range(n):
        start, end = map(float, sys.stdin.readline().rstrip().split())
        events.append((start, end))
    events.sort(key=lambda pair: (pair[1], pair[0]))
    passed: int = 0
    output: list[tuple[float, float]] = []
    cur_end: int = float('-inf')
    for start, end in events:
        if start >= cur_end:
            passed += 1
            output.append((start, end))
            cur_end = end
    sys.stdout.write(f'{passed}\n')
    for start, end in output:
        sys.stdout.write(f'{int(start) if int(start) == start else start} {int(end) if int(end) == end else end}\n')


if __name__ == '__main__':
    solution()