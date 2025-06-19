import sys
from collections import deque


def solution() -> None:
    """
    Time Complexity O(1) for each operation
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    queue: deque[int] = deque()
    leaved: int = 0
    hashmap: dict[int, tuple[int, int]] = dict()
    for _ in range(n):
        event, *args = sys.stdin.readline().rstrip().split()
        if event == '1':
            queue.append(args[0])
            hashmap[args[0]] = (len(queue), leaved)
        elif event == '2':
            del hashmap[queue.popleft()]
            leaved += 1
        elif event == '3':
            del hashmap[queue.pop()]
        elif event == '4':
            sys.stdout.write(f'{hashmap[args[0]][0] - (leaved - hashmap[args[0]][1]) - 1}\n')
        else:
            sys.stdout.write(f'{queue[0]}\n')


if __name__ == '__main__':
    solution()