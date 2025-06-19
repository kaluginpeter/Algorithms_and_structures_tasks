import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    Q: int = 100000009
    M: int = 100000003
    pattern: str = sys.stdin.readline().rstrip()
    n: int = len(pattern)
    prefix_sum: list[int] = [0]
    h: int = 0
    for ch in pattern:
        h = (h * Q + ord(ch)) % M
        prefix_sum.append(h)
    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
        if (b - a + 1) != (d - c + 1):
            sys.stdout.write('No\n')
            continue
        q_pow: int = pow(Q, b - a + 1, M)
        x: int = (prefix_sum[b] - prefix_sum[a - 1] * q_pow % M + M) % M
        q_pow: int = pow(Q, d - c + 1, M)
        y: int = (prefix_sum[d] - prefix_sum[c - 1] * q_pow % M + M) % M
        sys.stdout.write('{}\n'.format('Yes' if x == y else 'No'))


if __name__ == '__main__':
    solution()