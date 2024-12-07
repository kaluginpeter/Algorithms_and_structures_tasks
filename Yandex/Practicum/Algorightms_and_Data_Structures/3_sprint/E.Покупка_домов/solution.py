import sys


def solution(n: int, k: int, homes: list[int]) -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    purchased: int = 0
    homes.sort()
    for home in homes:
        if k - home < 0:
            break
        k -= home
        purchased += 1
    sys.stdout.write(str(purchased) + '\n')


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().rstrip().split())
    homes: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, k, homes)