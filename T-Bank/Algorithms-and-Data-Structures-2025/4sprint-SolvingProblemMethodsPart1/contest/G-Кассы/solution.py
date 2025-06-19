import sys


def solution() -> None:
    """
    Time Complexity O(N + M)
    Memory Complexity O(M)
    """
    n: int = int(sys.stdin.readline().rstrip())
    seconds: list[int] = [0] * (24 * 60 * 60)
    for _ in range(n):
        s_h, s_m, s_s, e_h, e_m, e_s = map(int, sys.stdin.readline().rstrip().split())
        start: int = 3600 * s_h + 60 * s_m + s_s
        end: int = 3600 * e_h + 60 * e_m + e_s
        if start == end: seconds[0] += 1
        elif start < end:
            seconds[start] += 1
            seconds[end] -= 1
        else:
            seconds[0] += 1
            seconds[end] -= 1
            seconds[start] += 1
    output: int = 0 
    workers: int = 0
    for second in range(0, len(seconds)):
        workers += seconds[second]
        if workers == n: output += 1
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    solution()