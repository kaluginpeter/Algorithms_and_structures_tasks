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
    max_sum: int = float('-inf')
    def dfs(root: 'Node') -> int:
        if not root: return float('-inf')
        left_sum: int = max(dfs(root.left), 0)
        right_sum: int = max(dfs(root.right), 0)
        nonlocal max_sum
        max_sum = max(
            max_sum, root.value + left_sum + right_sum
        )
        return root.value + max(left_sum, right_sum)
    dfs(root)
    return max_sum


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == '__main__':
    test()