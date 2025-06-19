import sys


def solution() -> None:
    """
    Time Complexity O(Q(L + N))
    Memory Complexity O(L + N)
    """
    text: str = sys.stdin.readline().rstrip()
    n: int = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        pattern: str = sys.stdin.readline().rstrip()
        S: str = pattern + '#' + text
        lcp: list[int] = [0] * len(pattern)
        prev_k: int = 0
        freq: int = 0
        positions: list[int] = []
        for idx in range(1, len(S)):
            k: int = prev_k
            while k and S[k] != S[idx]: k = lcp[k - 1]
            if S[k] == S[idx]: k += 1
            if idx < len(pattern): lcp[idx] = k
            prev_k = k 
            if k == len(pattern):
                freq += 1
                positions.append(idx - 2 * len(pattern))
        sys.stdout.write('{} {}\n'.format(freq, ' '.join(str(pos) for pos in positions)))


if __name__ == '__main__':
    solution()