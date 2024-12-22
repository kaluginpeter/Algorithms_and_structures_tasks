import sys


def solution(n: int, points: list[str]) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    hashmap: dict[int, int] = dict()
    hashmap[0] = 0
    cur_sum: int = 0
    max_sub: int = 0
    for idx in range(n):
        if points[idx] == '0':
            cur_sum -= 1
        else:
            cur_sum += 1
        if cur_sum == 0:
            max_sub = max(max_sub, idx - hashmap[cur_sum] + 1)
        if cur_sum in hashmap:
            max_sub = max(max_sub, idx - hashmap[cur_sum])
        else:
            hashmap[cur_sum] = idx
    sys.stdout.write(str(max_sub) + '\n')


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    points: list[str] = sys.stdin.readline().rstrip().split()
    solution(n, points)
