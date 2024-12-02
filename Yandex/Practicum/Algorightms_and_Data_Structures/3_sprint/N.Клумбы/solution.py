import sys


def solution(n: int, pairs: list[list[int, int]]) -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    pairs.sort()
    main_idx: int = 0
    current_idx: int = 0
    for idx in range(n):
        if pairs[current_idx][1] >= pairs[idx][0]:
            pairs[current_idx][1] = max(pairs[current_idx][1], pairs[idx][1])
        else:
            pairs[main_idx] = pairs[current_idx]
            current_idx = idx
            main_idx += 1
    pairs[main_idx] = pairs[current_idx]
    main_idx += 1
    for idx in range(main_idx):
        sys.stdout.write(' '.join(map(str, pairs[idx])) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    pairs: list[list[int, int]] = []
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        pairs.append([start, end])
    solution(n, pairs)