import sys


class SegmentInfo:
    __slots__ = ('count', 'left_color', 'right_color', 'total_length', 'length')
    def __init__(self) -> None:
        self.count: int = 0
        self.left_color: int = 0
        self.right_color: int = 0
        self.total_length: int = 0
        self.length: int = 0


class SegmentTreeNode:
    __slots__ = ('l', 'r', 'left', 'right', 'min_val', 'add_lazy', 'assign_lazy', 'has_assignment', 'sum', 'info')
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
        self.info: SegmentInfo = SegmentInfo()
        self.info.length = r - l + 1


class SegmentTree:
    __slots__ = ('root',)
    def __init__(self, nums: list[int]) -> None:
        self.root: SegmentTreeNode = SegmentTreeNode(0, len(nums) - 1)
        self.build(self.root, nums)
    
    def build(self, node: SegmentTreeNode, nums: list[int]) -> None:
        if node.l == node.r:
            node.info.length = 1
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
        node.info = self.merge(node.left.info, node.right.info)
    
    def merge(self, left: SegmentInfo, right: SegmentInfo) -> SegmentInfo:
        output: SegmentInfo = SegmentInfo()
        output.left_color = left.left_color
        output.right_color = right.right_color
        output.total_length = left.total_length + right.total_length
        output.length = left.length + right.length
        output.count = left.count + right.count
        if left.right_color == 1 and right.left_color == 1:
            output.count -= 1
        return output
    
    def push(self, node: SegmentTreeNode) -> None:
        if node.has_assignment:
            node.info.left_color = node.assign_lazy
            node.info.right_color = node.assign_lazy
            node.info.count = node.assign_lazy
            node.info.total_length = node.assign_lazy * node.info.length
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
        node.info = self.merge(node.left.info, node.right.info)
    
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
        node.info = self.merge(node.left.info, node.right.info)
    
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
    
    def _range_query(self, node: SegmentTreeNode, l: int, r: int) -> SegmentInfo:
        self.push(node)
        if node.l > r or node.r < l: return SegmentInfo()
        if l <= node.l <= node.r <= r: return node.info
        left: SegmentInfo = self._range_query(node.left, l, r)
        right: SegmentInfo = self._range_query(node.right, l, r)
        return self.merge(left, right)
    
    def get_info(self) -> SegmentInfo():
        return self._range_query(self.root, self.root.l, self.root.r)
    
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
    n: int = int(sys.stdin.readline().rstrip())
    st: SegmentTree = SegmentTree([0] * 1_000_000)
    for _ in range(n):
        args: list[int] = sys.stdin.readline().rstrip().split()
        l, r = map(int, args[1:])
        l += 500_000
        if args[0] == 'W':
            st.range_assign(l, l + r - 1, 0)
        else:
            st.range_assign(l, l + r - 1, 1)
        output: SegmentInfo = st.get_info()
        sys.stdout.write('{} {}\n'.format(output.count, output.total_length))


if __name__ == '__main__':
    solution()