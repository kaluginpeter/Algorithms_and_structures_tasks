import sys


class SegmentTreeNode:
    __slots__ = ('l', 'r', 'left', 'right', 'min_val', 'add_lazy', 'assign_lazy', 'has_assignment', 'sum')
    def __init__(self, l: int, r: int) -> None:
        self.l: int = l
        self.r: int = r
        self.left: SegmentTreeNode = None
        self.right: SegmentTreeNode = None
        self.sum: int = 0
        self.min_val: int = 0
        self.add_lazy: int = 0
        self.assign_lazy: int = 0
        self.has_assignment: bool = False


class SegmentTree:
    __slots__ = ('root',)
    def __init__(self, nums: list[int]) -> None:
        self.root: SegmentTreeNode = SegmentTreeNode(0, len(nums) - 1)
        self.build(self.root, nums)
    
    def build(self, node: SegmentTreeNode, nums: list[int]) -> None:
        if node.l == node.r:
            node.min_val = nums[node.l]
            node.sum = nums[node.l]
            return
        middle: int = node.l + ((node.r - node.l) >> 1)
        node.left = SegmentTreeNode(node.l, middle)
        node.right = SegmentTreeNode(middle + 1, node.r)
        self.build(node.left, nums)
        self.build(node.right, nums)
        node.sum = node.left.sum + node.right.sum
        node.min_val = min(node.left.min_val, node.right.min_val)
    
    def push(self, node: SegmentTreeNode) -> None:
        if node.has_assignment:
            node.min_val = node.assign_lazy
            node.sum = (node.r - node.l + 1) * node.assign_lazy
            if node.left:
                node.left.assign_lazy = node.assign_lazy
                node.left.add_lazy = 0
                node.left.has_assignment = True
                node.right.assign_lazy = node.assign_lazy
                node.right.add_lazy = 0
                node.right.has_assignment = True
            node.has_assignment = False
        if node.add_lazy != 0:
            node.min_val += node.add_lazy
            node.sum += (node.r - node.l + 1) * node.add_lazy
            if node.left:
                node.left.add_lazy += node.add_lazy
                node.right.add_lazy += node.add_lazy
            node.add_lazy = 0
    
    def _range_add(self, node: SegmentTreeNode, l: int, r: int, v: int) -> None:
        self.push(node)
        if node.r < l or node.l > r: return
        if l <= node.l and node.r <= r:
            node.add_lazy += v
            self.push(node)
            return
        self._range_add(node.left, l, r, v)
        self._range_add(node.right, l, r, v)
        node.sum = node.left.sum + node.right.sum
        node.min_val = min(node.left.min_val, node.right.min_val)
    
    def _range_assign(self, node: SegmentTreeNode, l: int, r: int, v: int) -> None:
        self.push(node)
        if node.l > r or node.r < l: return
        if l <= node.l <= node.r <= r:
            node.assign_lazy = v
            node.has_assignment = True
            node.add_lazy = 0
            self.push(node)
            return
        self._range_assign(node.left, l, r, v)
        self._range_assign(node.right, l, r, v)
        node.sum = node.left.sum + node.right.sum
        node.min_val = min(node.left.min_val, node.right.min_val)
    
    def _range_min(self, node: SegmentTreeNode, l: int, r: int) -> int:
        self.push(node)
        if node.r < l or node.l > r:
            return float('inf')
        if l <= node.l <= node.r <= r:
            return node.min_val
        left_min: int = self._range_min(node.left, l, r)
        right_min: int = self._range_min(node.right, l, r)
        return min(left_min, right_min)
    
    def _range_sum(self, node: SegmentTreeNode, l: int, r: int) -> int:
        self.push(node)
        if node.l > r or node.r < l: return 0
        if l <= node.l <= node.r <= r: return node.sum
        return self._range_sum(node.left, l, r) + self._range_sum(node.right, l, r)
    
    def range_sum(self, l: int, r: int) -> int:
        return self._range_sum(self.root, l, r)
    
    def range_assign(self, l: int, r: int, v: int) -> None:
        self._range_assign(self.root, l, r, v)
    
    def range_min(self, l: int, r: int) -> int:
        return self._range_min(self.root, l, r)
    
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
            st.range_assign(l, r - 1, v)
        elif args[0] == 2:
            l, r, v = args[1:]
            st.range_add(l, r - 1, v)
        else:
            l, r = args[1:]
            sys.stdout.write(f"{st.range_sum(l, r - 1)}\n")


if __name__ == '__main__':
    solution()