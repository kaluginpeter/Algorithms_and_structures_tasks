import sys
from collections import deque


def solution() -> None:
    """
    Time Complexity O(|V| + |E|)
    Memory Complexity O(|V| + |E|)
    """
    n: int = int(sys.stdin.readline().rstrip())
    x1, y1 = map(int, sys.stdin.readline().rstrip().split())
    x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    moves: list[tuple[int, int]] = [
        (-2, -1), (-2, 1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)
    ]
    seen: list[list[bool]] = [[False] * (n + 1) for _ in range(n + 1)]
    seen[x1][y1] = True
    q: list[tuple[tuple[int, int], list[tuple[int, int]]]] = deque()
    q.append(((x1, y1), [(x1, y1)]))
    while q:
        cur_pos, path = q.popleft()
        if cur_pos == (x2, y2):
            sys.stdout.write('{}\n'.format(len(path) - 1))
            sys.stdout.write('{}\n'.format('\n'.join('{} {}'.format(x, y) for x, y in path)))
            return
        for m_x, m_y in moves:
            next_x, next_y = cur_pos[0] + m_x, cur_pos[1] + m_y
            if min(next_x, next_y) < 1 or max(next_x, next_y) > n or seen[next_x][next_y]:
                continue
            next_path: list[tuple[int, int]] = path + [(next_x, next_y)]
            seen[next_x][next_y] = True
            q.append(((next_x, next_y), next_path))


if __name__ == '__main__':
    solution()