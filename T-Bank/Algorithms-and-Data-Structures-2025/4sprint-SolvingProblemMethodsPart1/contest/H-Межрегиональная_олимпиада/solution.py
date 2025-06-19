import sys


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    n, c = map(int, sys.stdin.readline().rstrip().split())
    segments: list[tuple[int, int, int]] = []
    for i in range(1, n + 1):
        start, duration = map(int, sys.stdin.readline().rstrip().split())
        segments.append((start, start + duration, i))
    segments.sort(key=lambda task: (task[1], task[0]))
    outcome: int = 0
    prev_end: int = 0
    task_id: int = 0
    path: list[int] = []
    for segment in segments:
        if segment[0] >= prev_end:
            if prev_end:
                path.append(task_id)
                outcome += c
            prev_end = segment[1]
            task_id = segment[2]
    outcome += c 
    path.append(task_id)
    sys.stdout.write('{}\n{}\n'.format(outcome, len(path)))
    sys.stdout.write(' '.join(str(task) for task in path) + '\n')


if __name__ == '__main__':
    solution()