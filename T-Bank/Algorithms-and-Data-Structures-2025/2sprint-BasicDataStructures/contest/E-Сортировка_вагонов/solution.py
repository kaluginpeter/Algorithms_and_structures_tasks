import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    moves: list[str] = []
    deadlock: list[int] = []
    left: int = 0
    right: int = 0
    target: int = 1
    while target <= n:
        while right < n and nums[right] != target:
            right += 1
        if right < n:
            moves.append(f'1 {right - left + 1}')
            for idx in range(left, right + 1):
                deadlock.append(nums[idx])
            right += 1
            left = right
        else:
            sys.stdout.write('0\n')
            return
        
        deadlock_to_second_station: int = 0
        while deadlock and deadlock[-1] == target:
            deadlock_to_second_station += 1 
            target += 1 
            deadlock.pop()
        if deadlock_to_second_station:
            moves.append(f'2 {deadlock_to_second_station}')
    sys.stdout.write(f'{len(moves)}\n')
    sys.stdout.write('\n'.join(moves))
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()