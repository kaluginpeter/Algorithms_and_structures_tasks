import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    """
    Time Complexity O(N)
    Memory Complexity O(H)
    """
    max_val: int = float('-inf')
    cur_nodes: list[Node] = [root]
    next_nodes: list[Node] = []
    while cur_nodes:
        for node in cur_nodes:
            max_val = max(max_val, node.value)
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)
        cur_nodes = next_nodes
        next_nodes = []
    return max_val


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()