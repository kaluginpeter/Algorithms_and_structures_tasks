import sys


def solution() -> None:
    """
    Time Complexity O(V^2)
    Memory Complexity O(V^2)
    """
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj_matrix: list[list[int]] = [[0] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        source, destination = map(int, sys.stdin.readline().rstrip().split())
        adj_matrix[source][destination] = 1
    for source in range(1, v + 1):
        for destination in range(1, v + 1):
            if destination > 1: sys.stdout.write(' ')
            sys.stdout.write(str(adj_matrix[source][destination]))
        sys.stdout.write('\n')


if __name__ == '__main__':
    solution()