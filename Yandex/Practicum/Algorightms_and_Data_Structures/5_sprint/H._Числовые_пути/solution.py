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
    Memory Complexity O(N)
    """
    total_sum: int = 0
    path: list[str] = list()
    def dfs(root: 'Node', path: list[str]) -> None:
        path.append(str(root.value))
        if not root.left and not root.right:
            nonlocal total_sum
            total_sum += int(''.join(path))
        if root.left: dfs(root.left, path)
        if root.right: dfs(root.right, path)
        path.pop()
    if root: dfs(root, path)
    return total_sum


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == '__main__':
    test()