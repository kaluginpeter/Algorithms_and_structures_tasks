import sys


def solution() -> None:
    """
    Time Complexity O(L)
    Memory Complexity O(M)
    """
    n: int = int(sys.stdin.readline().rstrip())
    pattern: str = ''
    p_n: int = 0
    for i in range(n):
        word: str = sys.stdin.readline().rstrip()
        if not i:
            pattern = word
            p_n = len(pattern)
        else:
            idx: int = 0
            while idx < min(p_n, len(word)):
                if pattern[idx] == word[idx]:
                    idx += 1
                else:
                    break
            p_n = idx
    sys.stdout.write('{}\n'.format(p_n))


if __name__ == '__main__':
    solution()
