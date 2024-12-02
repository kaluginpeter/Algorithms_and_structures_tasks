import sys


def solution(x: str, y: str) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    x_idx: int = 0
    y_idx: int = 0
    while x_idx < len(x) and y_idx < len(y):
        if x[x_idx] == y[y_idx]:
            x_idx += 1
        y_idx += 1
    sys.stdout.write(str(x_idx == len(x)) + '\n')


if __name__ == '__main__':
    x: str = sys.stdin.readline().rstrip()
    y: str = sys.stdin.readline().rstrip()
    solution(x, y)

