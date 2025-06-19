import sys


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.interval: list[int] = [0] * (3 * 100000)
    
    def build(self, sequence: list[int]) -> None:
        for i in range(self.n):
            self.interval[self.n + i] = sequence[i]
        for i in range(self.n - 1, 0, -1):
            self.interval[i] = self.interval[i << 1] + self.interval[i << 1 | 1]
    
    def update(self, idx: int, val: int) -> None:
        idx += self.n
        self.interval[idx] = val
        while idx > 1:
            self.interval[idx >> 1] = self.interval[idx] + self.interval[idx ^ 1]
            idx >>= 1
    
    def range_sum(self, left: int, right: int) -> int:
        output: int = 0
        left += self.n 
        right += self.n
        while left < right:
            if left & 1:
                output += self.interval[left]
                left += 1
            if right & 1:
                right -= 1
                output += self.interval[right]
            left >>= 1
            right >>= 1 
        return output
            


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    st: SegmentTree = SegmentTree(n)
    sequence: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    st.build(sequence)
    for _ in range(m):
        op, x, y = map(int, sys.stdin.readline().rstrip().split())
        if op == 1: st.update(x, y)
        else: sys.stdout.write('{}\n'.format(st.range_sum(x, y)))


if __name__ == '__main__':
    solution()