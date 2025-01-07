import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def dfs(root) -> int:
    if not root:
        return 0
    left_depth: int = dfs(root.left)
    right_depth: int = dfs(root.right)
    if left_depth == float('inf') or right_depth == float('inf') or abs(left_depth - right_depth) > 1:
        return float('inf')
    return max(left_depth, right_depth) + 1


def solution(root) -> bool:
    """
    Time Complexity O(N)
    Memory Complexity O(H)
    """
    return dfs(root) != float('inf')


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()