import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    prefix_sum: list[int] = [0] * (n + 1)
    prefix_xor: list[int] = [0] * (n + 1)
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for i in range(n):
        num: int = next(nums)
        prefix_sum[i + 1] = prefix_sum[i] + num
        prefix_xor[i + 1] = prefix_xor[i] ^ num
    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        op, l, r = map(int, sys.stdin.readline().rstrip().split())
        if op == 1: sys.stdout.write('{}\n'.format(prefix_sum[r] - prefix_sum[l - 1]))
        else: sys.stdout.write('{}\n'.format(prefix_xor[r] ^ prefix_xor[l - 1]))


if __name__ == '__main__':
    solution()