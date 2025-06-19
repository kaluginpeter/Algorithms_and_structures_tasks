import sys
import random
from collections import defaultdict

def generate_random_weights(max_num: int) -> list[int]:
    return [random.randint(1, 10**18) for _ in range(max_num + 1)]

def generate_substrings(arr: list[int], weights1: list[int], weights2: list[int]):
    hash_map: dict[tuple[int, int], set[int]] = defaultdict(set)
    n: int = len(arr)
    for i in range(n):
        hash1, hash2 = 0, 0
        for j in range(i, n):
            hash1 += weights1[arr[j]]
            hash2 += weights2[arr[j]]
            length: int = j - i + 1
            hash_map[(hash1, hash2)].add(length)
    return hash_map

def solution():
    """
    Time Complexity O(N**2 + M**2)
    Memory Complexity O(N**2)
    """
    n: int = int(sys.stdin.readline())
    a: list[int] = list(map(int, sys.stdin.readline().split()))
    m: int = int(sys.stdin.readline())
    b: list[int] = list(map(int, sys.stdin.readline().split()))

    max_num: int = 10**5
    weights1: list[int] = generate_random_weights(max_num)
    weights2: list[int] = generate_random_weights(max_num)

    hash_map: dict[tuple[int, int], set[int]] = generate_substrings(a, weights1, weights2)

    prefix_sum1: list[int] = [0] * (m + 1)
    prefix_sum2: list[int] = [0] * (m + 1)
    for i in range(m):
        prefix_sum1[i + 1] = prefix_sum1[i] + weights1[b[i]]
        prefix_sum2[i + 1] = prefix_sum2[i] + weights2[b[i]]

    max_len: int = 0
    for i in range(m):
        for j in range(i + 1, m + 1):
            hash1: int = prefix_sum1[j] - prefix_sum1[i]
            hash2: int = prefix_sum2[j] - prefix_sum2[i]
            length: int = j - i
            if (hash1, hash2) in hash_map and length in hash_map[(hash1, hash2)]:
                max_len = max(max_len, length)

    sys.stdout.write('{}\n'.format(max_len))

if __name__ == "__main__":
    solution()