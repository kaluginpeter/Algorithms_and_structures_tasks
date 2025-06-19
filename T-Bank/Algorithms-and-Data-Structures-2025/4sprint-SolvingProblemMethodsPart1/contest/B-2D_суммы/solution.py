import sys


def solution() -> None:
    """
    Time Complexity O(NM)
    Memory Complexity O(NM)
    """
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    prefix_sum: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
        for j in range(m):
            num: int = next(nums)
            prefix_sum[i + 1][j + 1] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] + num - prefix_sum[i][j]

    for _ in range(k):
        y1, x1, y2, x2 = map(int, sys.stdin.readline().rstrip().split())
        output: int = prefix_sum[y2][x2]
        output -= prefix_sum[y2][x1 - 1]
        output -= prefix_sum[y1 - 1][x2]
        output += prefix_sum[y1 - 1][x1 - 1]
        
        sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    solution()