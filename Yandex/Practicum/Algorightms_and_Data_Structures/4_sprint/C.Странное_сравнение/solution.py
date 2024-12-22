import sys


def solution(a: str, b: str) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    is_valid: bool = True
    a_left: int = 0
    a_right: int = 0
    b_left: int = 0
    b_right: int = 0
    while a_right < len(a) and b_right < len(b):
        while a_right < len(a) and a[a_left] == a[a_right]:
            a_right += 1
        while b_right < len(b) and b[b_left] == b[b_right]:
            b_right += 1
        if a_right - a_left != b_right - b_left:
            is_valid = False
            break
        else:
            a_left = a_right
            b_left = b_right
    sys.stdout.write(['NO', 'YES'][is_valid and a_right == len(a) and b_right == len(b)] + '\n')


if __name__ == '__main__':
    a: str = sys.stdin.readline().rstrip()
    b: str = sys.stdin.readline().rstrip()
    solution(a, b)
