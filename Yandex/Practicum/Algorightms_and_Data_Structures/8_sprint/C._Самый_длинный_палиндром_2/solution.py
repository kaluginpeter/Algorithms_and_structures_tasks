import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(M) -> O(1)
    """
    sequence: str = sys.stdin.readline().rstrip()
    histogram: dict[int, int] = dict()
    for letter in sequence:
        histogram[ord(letter)] = histogram.get(ord(letter), 0) + 1
    part: list[str] = []
    median: str = ''
    for idx in range(97, 123):
        if idx not in histogram: continue
        for _ in range(histogram[idx] // 2): part.append(chr(idx))
        if histogram[idx] & 1 and not median: median = chr(idx)

    sys.stdout.write('{}{}{}\n'.format(''.join(part), median, ''.join(reversed(part))))


if __name__ == '__main__':
    solution()