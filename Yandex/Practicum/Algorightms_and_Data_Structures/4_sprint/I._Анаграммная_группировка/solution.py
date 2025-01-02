import sys


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    words: list[str] = sys.stdin.readline().rstrip().split()
    hashmap: dict[str, list[int]] = dict()
    for idx in range(n):
        base: str = ''.join(sorted(words[idx]))
        if base not in hashmap:
            hashmap[base] = list()
        hashmap[base].append(idx)
    groups: list[list[int]] = sorted(hashmap.values())
    for row_idx in range(len(groups)):
        if row_idx:
            sys.stdout.write('\n')
        for col_idx in range(len(groups[row_idx])):
            if col_idx:
                sys.stdout.write(' ')
            sys.stdout.write(str(groups[row_idx][col_idx]))


if __name__ == '__main__':
    solution()
