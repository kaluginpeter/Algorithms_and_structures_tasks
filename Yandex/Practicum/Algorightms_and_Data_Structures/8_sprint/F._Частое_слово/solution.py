import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(D)
    """
    n: int = int(sys.stdin.readline().rstrip())
    histogram: dict[str, int] = dict()
    max_freq: int = 0
    max_freq_word: str = ''
    for _ in range(n):
        word: str = sys.stdin.readline().rstrip()
        histogram[word] = histogram.get(word, 0) + 1
        if histogram[word] > max_freq:
            max_freq = histogram[word]
            max_freq_word = word
        elif histogram[word] == max_freq and word < max_freq_word:
            max_freq_word = word
    sys.stdout.write('{}\n'.format(max_freq_word))


if __name__ == '__main__':
    solution()