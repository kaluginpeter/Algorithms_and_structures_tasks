import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    words: list[str] = sys.stdin.readline().rstrip().split()
    left: int = 0
    right: int = len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    sys.stdout.write(' '.join(words) + '\n')


if __name__ == '__main__':
    solution()