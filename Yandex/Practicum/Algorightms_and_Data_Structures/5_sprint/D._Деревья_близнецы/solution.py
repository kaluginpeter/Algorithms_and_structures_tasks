import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root1: 'Node', root2: 'Node') -> bool:
    """
    Time Complexity O(N)
    Memory Complexity O(H)"""
    if root1 == root2 == None: return  True
    elif (
        (root1 and not root2)
        or (not root1 and root2)
        or (root1.value != root2.value)
    ): return False
    return solution(root1.left, root2.left) and solution(root1.right, root2.right)


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()