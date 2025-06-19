import sys


def solution() -> None:
    """
    Time Complexity O(|S|)
    Memory Complexity O(|S|)
    """
    s: str = sys.stdin.readline().rstrip()
    transformed: str = '#'.join('^{}$'.format(s))
    n: int = len(transformed)
    p: list[int] = [0] * n
    center = right = 0
    
    for i in range(1, n - 1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        while transformed[i + p[i] + 1] == transformed[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right: center, right = i, i + p[i]

    total: int = 0
    for length in p: total += (length + 1) // 2
    sys.stdout.write('{}\n'.format(total))


if __name__ == '__main__':
    solution()