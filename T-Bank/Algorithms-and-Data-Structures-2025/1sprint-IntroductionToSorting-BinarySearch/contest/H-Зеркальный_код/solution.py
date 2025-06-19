import sys


def solution() -> int:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    letters: str = sys.stdin.readline().rstrip()
    chunks: list[int] = [0] * 26
    for letter in letters:
        chunks[ord(letter) - 65] += 1
    output: list[str] = []
    median: str = ''
    for i in range(26):
        if chunks[i]:
            if chunks[i] & 1 and not median: median = chr(i + 65)
            output.append(chr(i + 65) * (chunks[i] // 2))
    palindrom: str = ''.join(output)
    if median: palindrom += median
    palindrom += ''.join(reversed(output))
    sys.stdout.write(f'{palindrom}\n')


if __name__ == '__main__':
    solution()