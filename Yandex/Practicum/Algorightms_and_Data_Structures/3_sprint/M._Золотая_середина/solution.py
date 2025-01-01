import sys


def solution() -> None:
    """
    Time Complexity O(log(min(A, B)))
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    A: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    B: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    if n > m:
        A, B = B, A
        n, m = m, n
    half: int = (n + m) // 2
    left: int = 0
    right: int = n - 1
    while left < n:
        middle: int = left + (right - left) // 2
        second_middle: int = half - middle - 2
        A_left: int = A[middle] if middle >= 0 else float('-inf')
        A_right: int = A[middle + 1] if middle + 1 < n else float('inf')
        B_left: int = B[second_middle] if second_middle >= 0 else float('-inf')
        B_right: int = B[second_middle + 1] if second_middle + 1 < m else float('inf')
        if A_left <= B_right and B_left <= A_right:
            if (n + m) & 1:
                sys.stdout.write(f'{min(A_right, B_right)}\n')
                return
            else:
                median: float = (max(A_left, B_left) + min(A_right, B_right)) / 2
                if int(median) == median:
                    median = int(median)
                sys.stdout.write(f'{median}\n')
                return
        elif A_left > B_right:
            right = middle - 1
        else:
            left = middle + 1


if __name__ == '__main__':
    solution()