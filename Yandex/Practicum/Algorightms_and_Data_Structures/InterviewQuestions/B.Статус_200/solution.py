from __future__ import annotations
import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    total_pairs: int = 0
    hashmap: list[int] = [0] * 200
    for num in nums:
        remainder: int = num % 200
        total_pairs += hashmap[remainder]
        hashmap[remainder] += 1
    sys.stdout.write('{}\n'.format(total_pairs))


if __name__ == '__main__':
    solution()