import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n, r = map(int, sys.stdin.readline().rstrip().split())
    tree: list[tuple[int, int]] = []
    for node in range(n):
        left, right = map(int, sys.stdin.readline().rstrip().split())
        tree.append((left, right))
    is_valid: bool = True
    heights: list[int] = [0] * n 
    stack: list[tuple[int, bool, int, int]] = [(r, False, -1000000, 1000000)]
    while stack:
        node, is_visited, min_bound, max_bound = stack.pop()
        if not is_visited:
            if not min_bound < node < max_bound:
                is_valid = False
                break
            stack.append((node, True, min_bound, max_bound))
            if tree[node][0] != -1:
                stack.append((tree[node][0], False, min_bound, node))
            if tree[node][1] != -1:
                stack.append((tree[node][1], False, node, max_bound))
        else:
            left_depth: int = heights[tree[node][0]] if tree[node][0] != -1 else 0 
            right_depth: int = heights[tree[node][1]] if tree[node][1] != -1 else 0
            if abs(left_depth - right_depth) > 1:
                is_valid = False
                break
            heights[node] = max(left_depth, right_depth) + 1
    sys.stdout.write(f'{int(is_valid)}\n')


if __name__ == '__main__':
    solution()