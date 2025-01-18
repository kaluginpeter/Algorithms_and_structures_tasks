import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root: 'Node') -> int:
    """
    Time Complexity O(N)
    Memory Complexity O(H)
    """
    max_depth: int = 0

    def dfs(root: 'Node', depth: int) -> int:
        if not root: return
        nonlocal max_depth
        depth += 1
        max_depth = max(max_depth, depth)
        dfs(root.left, depth)
        dfs(root.right, depth)

    dfs(root, 0)
    return max_depth


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == '__main__':
    test()