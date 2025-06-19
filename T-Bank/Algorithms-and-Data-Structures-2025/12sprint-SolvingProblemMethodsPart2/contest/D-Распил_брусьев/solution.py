import sys


def solution() -> None:
    """
    Time Complexity O(N^2)
    Memory Complexity O(N^2)
    """
    L, N = map(int, sys.stdin.readline().rstrip().split())
    cuts: list[int] = [0]
    cuts.extend(map(int, sys.stdin.readline().rstrip().split()))
    cuts.append(L)
    dp: list[list[int]] = [[0] * (N + 2) for _ in range(N + 2)]
    for length in range(2, N + 2):
        for left in range(N + 1 - length + 1):
            right: int = left + length
            dp[left][right] = float('inf')
            for k in range(left + 1, right):
                dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + cuts[right] - cuts[left])
    sys.stdout.write('{}\n'.format(dp[0][N + 1]))


if __name__ == '__main__':
    solution()