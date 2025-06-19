import sys


def fill_bfs_tree(tree: dict[int, list[int]], depth: dict[int, int], parent: dict[int, int]) -> None:
    cur_nodes: list[int] = [0]
    parent[0] = -1
    next_nodes: list[int] = []
    cur_depth: int = -1
    while cur_nodes:
        cur_depth += 1
        for node in cur_nodes:
            depth[node] = cur_depth
            for child in tree.get(node, []):
                parent[child] = node
                next_nodes.append(child)
        cur_nodes = next_nodes
        next_nodes = []


def get_lca(u: int, v: int, depth: dict[int, int], parent: dict[int, int]) -> int:
    while depth[u] > depth[v]: u = parent[u]
    while depth[v] > depth[u]: v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    tree: dict[int, list[int]] = dict()
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for node in range(1, n):
        parent: int = next(nums)
        if parent not in tree: tree[parent] = []
        tree[parent].append(node)
    parent: dict[int, int] = dict()
    depth: dict[int, int] = dict()
    fill_bfs_tree(tree, depth, parent)
    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write('{}\n'.format(get_lca(u, v, depth, parent)))


if __name__ == '__main__':
    solution()