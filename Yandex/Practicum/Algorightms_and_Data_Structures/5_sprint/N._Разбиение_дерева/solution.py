import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size


def split(root: "Node", k: int) -> tuple['Node', 'Node']:
    """
    Time Complexity O(H)
    Memory Complexity O(H)
    """
    if k == 0: return None, root
    left_size: int = root.left.size if root.left else 0
    if left_size < k:
        left_root, right_root = split(root.right, k - left_size - 1)
        root.right = left_root
        root.size = (left_root.size if left_root else 0) + (root.left.size if root.left else 0) + 1
        return root, right_root
    else:
        left_root, right_root = split(root.left, k)
        root.left = right_root
        root.size = (right_root.size if right_root else 0) + (root.right.size if root.right else 0) + 1
        return left_root, root


def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    assert (left.size == 4)
    assert (right.size == 2)


if __name__ == '__main__':
    test()