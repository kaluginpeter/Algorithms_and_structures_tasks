import sys
from collections import deque


def solution() -> None:
    """
    Time Complexity O(|V| + |E|)
    Memory Complexity O(|V|)
    """
    m: int = int(sys.stdin.readline().rstrip())
    adj_list: dict[str, list[str]] = dict()
    for _ in range(m):
        convertation: str = sys.stdin.readline().rstrip()
        source, destination = convertation.split(' -> ')
        if destination not in adj_list:
            adj_list[destination] = []
        adj_list[destination].append(source)
    start: str = sys.stdin.readline().rstrip()
    target: str = sys.stdin.readline().rstrip()
    seen: set[str] = set()
    q: list[tuple[str, int]] = deque()
    q.append((target, 0))
    while q:
        vertex, path = q.popleft()
        if vertex == start:
            sys.stdout.write('{}\n'.format(path))
            return
        for neighbor in adj_list.get(vertex, []):
            if neighbor not in seen:
                seen.add(neighbor)
                q.append((neighbor, path + 1))
    sys.stdout.write('{}\n'.format(-1))


if __name__ == '__main__':
    solution()