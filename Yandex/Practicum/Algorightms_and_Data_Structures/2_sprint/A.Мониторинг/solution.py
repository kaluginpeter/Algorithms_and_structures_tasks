import sys

def solution(n: int, m: int, matrix: list[list[str]]) -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(1)
    """
    for col in range(m):
        for row in range(n):
            if row:
                sys.stdout.write(' ')
            sys.stdout.write(matrix[row][col])
        sys.stdout.write('\n')

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    matrix: list[list[str]] = []
    for _ in range(n):
        row: str = sys.stdin.readline().rstrip().split()
        matrix.append(row)
    solution(n, m, matrix)