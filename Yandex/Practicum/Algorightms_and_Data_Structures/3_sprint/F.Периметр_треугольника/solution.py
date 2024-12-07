import sys


def solution(n: int, stripes: list[int]) -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    """
    stripes.sort(reverse=True)
    for idx in range(n):
        if stripes[idx] < stripes[idx + 1] + stripes[idx + 2]:
            sys.stdout.write(str(stripes[idx] + stripes[idx + 1] + stripes[idx + 2]) + '\n')
            break


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    stripes: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, stripes)
