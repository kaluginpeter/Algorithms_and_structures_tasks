import sys
from collections import defaultdict


def solution(nums: list[int], target: int) -> None:
    """
    Time Complexity O(N**3)
    Memory Complexity O(N**4)
    """
    nums.sort()
    res: list[list[int]] = []
    n: int = len(nums)

    pair_sum: dict[int, list[tuple[int, int]]] = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            pair_sum[nums[i] + nums[j]].append((i, j))

    for k in range(n):
        for l in range(k + 1, n):
            complement: int = target - (nums[k] + nums[l])
            if complement in pair_sum:
                for i, j in pair_sum[complement]:
                    if i < k and j < k:
                        res.append([nums[i], nums[j], nums[k], nums[l]])

    res: list[list[int]] = sorted(map(list, set(map(tuple, res))))

    sys.stdout.write(f'{len(res)}\n')
    for quadruplet in res:
        print(' '.join(str(num) for num in quadruplet))


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    target: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(nums, target)
