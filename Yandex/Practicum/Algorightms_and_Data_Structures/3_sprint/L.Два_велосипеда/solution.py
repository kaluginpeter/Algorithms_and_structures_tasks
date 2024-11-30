import sys


def leftmost_binary_search(days: list[int], bike_cost: int) -> int:
    left: int = 0
    right: int = len(days) - 1
    is_found = False
    while left <= right:
        middle: int = left + (right - left) // 2
        if days[middle] >= bike_cost:
            is_found = True
            right = middle - 1
        else:
            left = middle + 1
    return (right + 1) + 1 if is_found else -1


def solution() -> None:
    """
    Time Complexity O(logN)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    days: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    bike_cost: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(leftmost_binary_search(days, bike_cost)) + ' ')
    sys.stdout.write(str(leftmost_binary_search(days, bike_cost * 2)) + '\n')


if __name__ == '__main__':
    solution()