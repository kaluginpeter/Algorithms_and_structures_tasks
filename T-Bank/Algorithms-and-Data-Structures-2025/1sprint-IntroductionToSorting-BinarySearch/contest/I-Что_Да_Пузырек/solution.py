import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    seen: list[bool] = [False] * (n + 1)
    last: int = n
    zeros: int = 0
    sys.stdout.write('1')
    for num in nums:
        sys.stdout.write(' ')
        seen[num] = True
        zeros += 1
        while seen[last]:
            last -= 1
            zeros -= 1
        sys.stdout.write(str(zeros + 1))
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()