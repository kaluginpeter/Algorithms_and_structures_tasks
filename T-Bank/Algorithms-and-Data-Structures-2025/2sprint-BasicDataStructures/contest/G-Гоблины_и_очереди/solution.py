import sys
from collections import deque


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    queue: deque[int] = deque()
    output: deque[int] = deque()
    total_size: int = 0
    for _ in range(n):
        operation, *args = sys.stdin.readline().rstrip().split()
        if operation == '-':
            total_size -= 1
            if output:
                sys.stdout.write(f'{output.popleft()}\n')
            else:
                sys.stdout.write(f'{queue.popleft()}\n')
            continue
        if operation == '+':
            queue.append(int(args[0]))
        else:
            place: int = total_size // 2
            if total_size & 1: place += 1
            place -= len(output)
            for _ in range(place):
                output.append(queue.popleft());
            queue.appendleft(int(args[0]))
        total_size += 1


if __name__ == '__main__':
    solution()