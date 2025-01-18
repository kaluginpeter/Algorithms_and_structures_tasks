import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def dfs(root1: 'Node', root2: 'Node') -> bool:
    if root1 == root2 == None: return True
    elif (
        (root1 and not root2)
        or (not root1 and root2)
        or (root1.value != root2.value)
    ): return False
    return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)


def solution(root) -> bool:
    """
    Time Complexity O(N)
    Memory Complexity O(H)
    """
    return dfs(root, root)


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)

if __name__ == '__main__':
    test()