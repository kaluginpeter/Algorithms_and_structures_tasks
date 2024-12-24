import sys


def solution(q: int, m: int, s: str) -> None:
    """
    Time Complexity O(s)
    Memory Complexity O(1)
    """
    h: int = 0
    for idx in range(len(s)):
        ch: str = s[idx]
        h += ord(ch) % m
        if idx != len(s) - 1:
            h = h * q % m
    sys.stdout.write(str(h % m) + '\n')


if __name__ == '__main__':
    a: int = int(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    s: str = sys.stdin.readline().rstrip()
    solution(a, m, s)
