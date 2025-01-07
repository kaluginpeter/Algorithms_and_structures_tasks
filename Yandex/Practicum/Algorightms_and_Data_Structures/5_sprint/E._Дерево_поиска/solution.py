import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root, min_value: int = float('-inf'), max_value: int = float('inf')) -> bool:
    """
    Time Complexity O(N)
    Memory Complexity O(H)
    """
    if not root:
        return True
    elif root.value <= min_value or root.value >= max_value:
        return False
    return solution(root.left, min_value, root.value) and solution(root.right, root.value, max_value)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()