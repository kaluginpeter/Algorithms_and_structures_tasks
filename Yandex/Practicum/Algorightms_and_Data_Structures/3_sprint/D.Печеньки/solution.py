import sys


def solution(n: int, greedy: list[int], m: int, cookies: list[int]) -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    happy: int = 0
    greedy.sort()
    cookies.sort()
    cookies_idx: int = 0
    for gred in greedy:
        while cookies_idx < m and cookies[cookies_idx] < gred:
            cookies_idx += 1
        if cookies_idx < m:
            happy += 1
            cookies_idx += 1
        else:
            break
    sys.stdout.write(str(happy) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    greedy: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    m: int = int(sys.stdin.readline().rstrip())
    cookies: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, greedy, m, cookies)
