import sys
import bisect


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.tree: list[int] = [0] * (self.size + 2)
    
    def update(self, index: int, delta: int = 1) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index: int) -> None:
        res: int = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline())
    nums: list[int] = list(map(int, sys.stdin.readline().split()))
    sorted_nums: list[int] = sorted(set(nums))
    compressed: dict[int, int] = {v: i + 1 for i, v in enumerate(sorted_nums)}
    max_compressed: int = len(sorted_nums)
    nums_compressed: list[int] = [compressed[v] for v in nums]
    left: list[int] = [0] * n
    ft_left: FenwickTree = FenwickTree(max_compressed)
    for i in range(n):
        left[i] = i - ft_left.query(nums_compressed[i])
        ft_left.update(nums_compressed[i])
    
    right: list[int] = [0] * n
    ft_right: FenwickTree = FenwickTree(max_compressed)
    for i in range(n - 1, -1, -1):
        right[i] = ft_right.query(nums_compressed[i] - 1)
        ft_right.update(nums_compressed[i])
    
    weakness: int = sum(left[i] * right[i] for i in range(n))
    sys.stdout.write('{}\n'.format(weakness))

if __name__ == "__main__":
    solution()