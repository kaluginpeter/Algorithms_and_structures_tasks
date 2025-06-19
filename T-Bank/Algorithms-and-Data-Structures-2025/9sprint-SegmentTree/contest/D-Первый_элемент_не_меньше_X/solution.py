import sys

class SegmentTreeNode:
    def __init__(self, l: int, r: int) -> None:
        self.l: int = l
        self.r: int = r
        self.left: SegmentTreeNode = None
        self.right: SegmentTreeNode = None
        self.min_val: int = 0
        self.min_num_count: int = 0
        self.range_sum: int = 0
        self.max_val: int = 0

class SegmentTree:
    def __init__(self, data: list[int]) -> None:
        self.n: int = len(data)
        self.data: list[int] = data.copy()
        self.root: SegmentTreeNode = self.build(0, self.n - 1)

    def build(self, l: int, r: int) -> SegmentTreeNode:
        node: SegmentTreeNode = SegmentTreeNode(l, r)
        if l == r:
            node.min_val = self.data[l]
            node.min_num_count = 1
            node.range_sum = self.data[l]
            node.max_val = self.data[l]
        else:
            mid: int = (l + r) // 2
            node.left = self.build(l, mid)
            node.right = self.build(mid + 1, r)
            self._push_up(node)
        return node

    def _push_up(self, node: SegmentTreeNode) -> None:
        if node.left.min_val < node.right.min_val:
            node.min_val = node.left.min_val
            node.min_num_count = node.left.min_num_count
        elif node.left.min_val > node.right.min_val:
            node.min_val = node.right.min_val
            node.min_num_count = node.right.min_num_count
        else:
            node.min_val = node.left.min_val
            node.min_num_count = node.left.min_num_count + node.right.min_num_count
        node.range_sum = node.left.range_sum + node.right.range_sum
        node.max_val = max(node.left.max_val, node.right.max_val)

    def update_val(self, pos: int, val: int) -> None:
        self._update_helper(self.root, pos, val)

    def _update_helper(self, node: SegmentTreeNode, pos: int, val: int) -> None:
        if node.l == node.r:
            self.data[node.l] = val
            node.min_val = val
            node.min_num_count = 1
            node.max_val = val
            node.range_sum = val
            return
        mid: int = (node.l + node.r) // 2
        if pos <= mid:
            self._update_helper(node.left, pos, val)
        else:
            self._update_helper(node.right, pos, val)
        self._push_up(node)

    def min_on_range(self, l: int, r: int) -> int:
        return self._min_on_range_helper(self.root, l, r)

    def _min_on_range_helper(self, node: SegmentTreeNode, l: int, r: int) -> tuple[int, int]:
        if node.r < l or node.l > r:
            return (float('inf'), 0)
        if l <= node.l and node.r <= r:
            return (node.min_val, node.min_num_count)
        left_min, left_count = self._min_on_range_helper(node.left, l, r)
        right_min, right_count = self._min_on_range_helper(node.right, l, r)
        if left_min < right_min:
            return (left_min, left_count)
        elif left_min > right_min:
            return (right_min, right_count)
        else:
            return (left_min, left_count + right_count)
    
    def _k_one(self, node: SegmentTreeNode, k: int) -> int:
        if node.l == node.r: return node.l
        elif node.left.range_sum > k: return self._k_one(node.left, k)
        return self._k_one(node.right, k - node.left.range_sum)
    
    def k_one(self, k: int) -> int:
        return self._k_one(self.root, k)
    
    def _leftmost_greater(self, node: SegmentTreeNode, x: int, l: int) -> None:
        if node.r < l: return -1
        elif node.max_val < x: return -1
        elif node.l == node.r: return node.l
        
        left: int = self._leftmost_greater(node.left, x, l)
        if left != -1: return left
        return self._leftmost_greater(node.right, x, l)
    
    def leftmost_greater(self, x: int, l: int) -> int:
        return self._leftmost_greater(self.root, x, l)


def solution():
    """
    Time Complexity O(N + MLogN)
    Memory Complexity O(N)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    data: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    st: SegmentTree = SegmentTree(data)
    for _ in range(m):
        cmd, x, y = map(int, sys.stdin.readline().rstrip().split())
        if cmd == 1: st.update_val(x, y)
        else: sys.stdout.write('{}\n'.format(st.leftmost_greater(x, y)))

if __name__ == '__main__':
    solution()