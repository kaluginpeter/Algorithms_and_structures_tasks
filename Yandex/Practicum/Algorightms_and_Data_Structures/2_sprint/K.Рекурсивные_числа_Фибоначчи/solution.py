import sys


memo: dict[int, int] = dict()


def solution(n: int) -> int:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = 1
        return memo[n]
    memo[n] = solution(n - 1) + solution(n - 2)
    return memo[n]


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(solution(n)) + '\n')
