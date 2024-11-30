import sys


def backtracking(n: int, current_sequence: list[str], open_brackets: int, close_brackets: int) -> None:
    if open_brackets + close_brackets == n:
        sys.stdout.write(''.join(current_sequence) + '\n')
        return
    if open_brackets < n // 2:
        current_sequence.append('(')
        backtracking(n, current_sequence, open_brackets + 1, close_brackets)
        current_sequence.pop()
    if close_brackets < open_brackets:
        current_sequence.append(')')
        backtracking(n, current_sequence, open_brackets, close_brackets + 1)
        current_sequence.pop()


def solution(n: int) -> None:
    """
    Time Complexity O(4**N / N**(3 / 2))
    Memory Complexity O(N)
    """
    current_sequence: list[str] = []
    backtracking(n * 2, current_sequence, 0, 0)


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    solution(n)
