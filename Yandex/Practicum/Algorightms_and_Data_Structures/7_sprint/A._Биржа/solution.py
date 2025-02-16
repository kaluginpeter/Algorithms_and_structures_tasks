import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(1)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    profit: int = 0
    cur_price: int = 0
    for idx in range(n):
        if not idx or nums[idx] < cur_price:
            cur_price = nums[idx]
        else:
            profit += nums[idx] - cur_price
            cur_price = nums[idx]
    sys.stdout.write(f'{profit}\n')


if __name__ == '__main__':
    solution()