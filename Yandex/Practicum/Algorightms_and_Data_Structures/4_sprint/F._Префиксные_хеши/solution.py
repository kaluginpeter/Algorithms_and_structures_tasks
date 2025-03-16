import sys


def solution(q: int, m: int, s: str) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    prefix: list[int] = [0]
    h: int = 0
    for idx in range(len(s)):
        ch: str = s[idx]
        h = (h % m * q % m + ord(ch)) % m
        prefix.append(h)

    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        l, r = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str(
            (prefix[r] - prefix[l-1] * pow(q, r-l+1, m) % m + m) % m
        )
        )
        sys.stdout.write('\n')


if __name__ == '__main__':
    q: int = int(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    s: str = sys.stdin.readline().rstrip()
    solution(q, m, s)


