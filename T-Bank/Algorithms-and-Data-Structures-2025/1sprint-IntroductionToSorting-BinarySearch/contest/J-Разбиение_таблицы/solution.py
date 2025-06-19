import sys

def f(n: int, a: int, d: int) -> int:
    return int(n / 2 * (2 * a + (n - 1) * d))


def vertically(n: int, m: int) -> tuple[str, int, int]:
    answer_col: int = float('inf')
    answer_diff: int = float('inf')
    left: int = 0
    right: int = m
    while left <= right:
        middle: int = left + (right - left) // 2
        left_sum: int = f(n, f(middle - 1, 1, 1), m * (middle - 1))
        right_sum: int = f(n, f(m - middle + 1, middle, 1), m * (m - middle + 1))
        diff: int = right_sum - left_sum
        if abs(diff) <= answer_diff:
            if abs(diff) == answer_diff: answer_col = min(answer_col, middle)
            else: answer_col = middle
            answer_diff = abs(diff)
        
        if diff < 0: right = middle - 1
        else: left = middle + 1
    return ('V', answer_col, answer_diff)


def horizontally(n: int, m: int) -> tuple[str, int, int]:
    answer_col: int = float('inf')
    answer_diff: int = float('inf')
    left: int = 0
    right: int = n
    m_square: int = m * m
    while left <= right:
        middle: int = left + (right - left) // 2
        left_sum: int = f(middle - 1, f(m, 1, 1), m_square) if middle > 1 else 0
        right_sum: int = f(n - middle + 1, f(m, (middle - 1) * m + 1, 1), m_square)
        diff: int = right_sum - left_sum
        if abs(diff) < answer_diff:
            answer_col = middle
            answer_diff = abs(diff)
        
        if diff < 0: right = middle - 1
        else: left = middle + 1
    return ('H', answer_col, answer_diff)


def solution() -> None:
    """
    Time Complexity O(logN + logM)
    Memory Complexity O(1)
    """
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        row, col, diff = vertically(n, m)
        gor_row, gor_col, gor_diff = horizontally(n, m)
        if gor_diff < diff:
            row, col = gor_row, gor_col
        sys.stdout.write(f'{row} {col}\n')


if __name__ == '__main__':
    solution()