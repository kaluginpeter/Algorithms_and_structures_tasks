import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    A: list[int] = [0] * (n + 1)
    B: list[int] = [0] * (n + 1)
    C: list[int] = [0] * (n + 1)
    A[1] = B[1] = C[1] = 1
    for i in range(2, n + 1):
        A[i] = B[i - 1] + C[i - 1]
        B[i] = A[i - 1] + B[i - 1] + C[i - 1]
        C[i] = A[i - 1] + B[i - 1] + C[i - 1]
    sys.stdout.write('{}\n'.format(A[n] + B[n] + C[n]))


if __name__ == '__main__':
    solution()