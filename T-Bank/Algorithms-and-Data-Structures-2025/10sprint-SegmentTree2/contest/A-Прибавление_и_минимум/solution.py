import sys


class SegmentTreeNode:
    __slots__ = ('l', 'r', 'left', 'right', 'min_val', 'lazy')
    def __init__(self, l: int, r: int) -> None:
        self.l: int = l
        self.r: int = r
        self.left: SegmentTreeNode = None
        self.right: SegmentTreeNode = None
        self.min_val: int = 0
        self.lazy: int = 0


class SegmentTree:
    __slots__ = ('root',)
    def __init__(self, nums: list[int]) -> None:
        self.root: SegmentTreeNode = SegmentTreeNode(0, len(nums) - 1)
        self.build(self.root, nums)
    
    def build(self, node: SegmentTreeNode, nums: list[int]) -> None:
        if node.l == node.r:
            node.min_val = nums[node.l]
            return
        middle: int = node.l + ((node.r - node.l) >> 1)
        node.left = SegmentTreeNode(node.l, middle)
        node.right = SegmentTreeNode(middle + 1, node.r)
        self.build(node.left, nums)
        self.build(node.right, nums)
        node.min_val = min(node.left.min_val, node.right.min_val)
    
    def push(self, node: SegmentTreeNode) -> None:
        if node.lazy != 0:
            node.min_val += node.lazy
            if node.left:
                node.left.lazy += node.lazy
            if node.right:
                node.right.lazy += node.lazy
            node.lazy = 0
    
    def _range_add(self, node: SegmentTreeNode, l: int, r: int, v: int) -> None:
        self.push(node)
        if node.r < l or node.l > r:
            return
        if l <= node.l and node.r <= r:
            node.lazy += v
            self.push(node)
            return
        self._range_add(node.left, l, r, v)
        self._range_add(node.right, l, r, v)
        node.min_val = min(node.left.min_val, node.right.min_val)
    
    def _min_on_range(self, node: SegmentTreeNode, l: int, r: int) -> int:
        self.push(node)
        if node.r < l or node.l > r:
            return float('inf')
        if l <= node.l and node.r <= r:
            return node.min_val
        left_min = self._min_on_range(node.left, l, r)
        right_min = self._min_on_range(node.right, l, r)
        return min(left_min, right_min)
    
    def min_on_range(self, l: int, r: int) -> int:
        return self._min_on_range(self.root, l, r)
    
    def range_add(self, l: int, r: int, v: int) -> None:
        self._range_add(self.root, l, r, v)


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    st: SegmentTree = SegmentTree([0] * n)
    for _ in range(m):
        args: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        if args[0] == 1:
            l, r, v = args[1:]
            st.range_add(l, r - 1, v)
        else:
            l, r = args[1:]
            sys.stdout.write(f"{st.min_on_range(l, r - 1)}\n")


if __name__ == '__main__':
    solution()