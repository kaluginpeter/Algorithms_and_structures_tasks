import sys

class SegmentTreeNode:
    def __init__(self, l: int, r: int) -> None:
        self.l: int = l
        self.r: int = r
        self.left: SegmentTreeNode = None
        self.right: SegmentTreeNode = None
        self.min_val: int = 0
        self.min_num_count: int = 0

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

    def update_val(self, pos: int, val: int) -> None:
        self._update_helper(self.root, pos, val)

    def _update_helper(self, node: SegmentTreeNode, pos: int, val: int) -> None:
        if node.l == node.r:
            self.data[node.l] = val
            node.min_val = val
            node.min_num_count = 1
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


def solution():
    """
    Time Complexity O(N + MlogN)
    Memory Complexity O(N)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    data: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    st: SegmentTree = SegmentTree(data)
    for _ in range(m):
        cmd, x, y = map(int, sys.stdin.readline().rstrip().split())
        if cmd == 1: st.update_val(x, y)
        else:
            min_val, min_freq = st.min_on_range(x, y - 1)
            sys.stdout.write('{} {}\n'.format(min_val, min_freq))

if __name__ == '__main__':
    solution()