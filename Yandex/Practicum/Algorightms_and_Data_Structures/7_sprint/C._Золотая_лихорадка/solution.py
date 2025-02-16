import sys


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    m: int = int(sys.stdin.readline().rstrip())
    n: int = int(sys.stdin.readline().rstrip())
    coins: list[tuple[int, int]] = []
    for _ in range(n):
        cost, freq = map(int, sys.stdin.readline().rstrip().split())
        coins.append((cost, freq))
    coins.sort(reverse=True)
    profit: int = 0
    for cost, freq in coins:
        t: int = min(m, freq)
        profit += cost * t
        m -= t
        if not m: break
    sys.stdout.write(f'{profit}\n')


if __name__ == '__main__':
    solution()