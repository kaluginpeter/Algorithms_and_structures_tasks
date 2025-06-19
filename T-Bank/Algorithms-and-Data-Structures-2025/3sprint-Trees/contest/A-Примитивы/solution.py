import sys


def solution() -> None:
    """
    Time Compelxity O(N)
    Memory Complexity O(N)
    """
    # Parse data
    n: int = int(sys.stdin.readline().rstrip())
    tree: dict[int, list[int]] = dict()
    nodes: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for child in range(1, n):
        parent: int = next(nodes)
        if parent not in tree: tree[parent] = []
        tree[parent].append(child)
    # Calculate depth of the tree and for each node
    heights: list[int] = [0] * n
    cur_nodes: list[int] = [0]
    next_nodes: list[int] = []
    tree_depth: int = -1
    while cur_nodes:
        tree_depth += 1
        for parent in cur_nodes:
            for child in tree.get(parent, []):
                next_nodes.append(child)
            heights[parent] = tree_depth
        cur_nodes = next_nodes
        next_nodes = []
    # Calculate max diameter of a tree
    max_diameter: int = 0
    max_heights: list[int] = [0] * n
    stack: list[tuple[int, bool]] = [(0, False)]
    while stack:
        parent, is_visited = stack.pop()
        if not is_visited:
            stack.append((parent, True))
            for child in tree.get(parent, []):
                stack.append((child, False))
        else:
            left_depth: int = 0
            right_depth: int = 0
            for child in tree.get(parent, []):
                if max_heights[child] > left_depth:
                    right_depth = left_depth
                    left_depth = max_heights[child]
                elif max_heights[child] > right_depth:
                    right_depth = max_heights[child]
            max_diameter = max(max_diameter, left_depth + right_depth)
            max_heights[parent] = max(left_depth, right_depth) + 1
    # Print results
    sys.stdout.write(f'{tree_depth} {max_diameter}\n')
    sys.stdout.write(' '.join(str(node_height) for node_height in heights))
    sys.stdout.write('\n')


if __name__ == '__main__':
    solution()