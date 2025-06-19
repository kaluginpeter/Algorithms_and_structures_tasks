import sys


def dfs(v: int, p: int, d: int, edge_weight: int, adj_list: list[list[tuple[int, int]]], dp: list[list[int]], min_edge: list[list[int]], depth: list[int]) -> None:
    dp[v][0] = p
    min_edge[v][0] = edge_weight
    depth[v] = d
    for edge in adj_list[v]:
        if (edge[0] != p): dfs(edge[0], v, d + 1, edge[1], adj_list, dp, min_edge, depth)
    

def preprocess(
    n: int,
    depth: list[int],
    dp: list[list[int]],
    min_edge: list[list[int]],
    adj_list: list[list[tuple[int, int]]]
):
    dfs(0, -1, 0, float('inf'), adj_list, dp, min_edge, depth)
    for j in range(1, 31):
        for v in range(n):
            if dp[v][j - 1] != -1:
                dp[v][j] = dp[dp[v][j - 1]][j - 1]
                min_edge[v][j] = min(min_edge[v][j - 1], min_edge[dp[v][j - 1]][j - 1])



def lca(u: int, v: int, depth: list[int], dp: list[list[int]]) -> int:
    if depth[u] < depth[v]: u, v = v, u
    for j in range(30, -1, -1):
        if depth[u] - (1 << j) >= depth[v]: u = dp[u][j]
    if u == v: return u
    for j in range(30, -1, -1):
        if dp[u][j] != dp[v][j]:
            u = dp[u][j]
            v = dp[v][j]
    return dp[u][0]


def get_min_edge(u: int, l: int, depth: list[int], min_edge: list[list[int]], dp: list[list[int]]) -> int:
    min_w: int = float('inf')
    for j in range(30, -1, -1):
        if depth[u] - (1 << j) >= depth[l]:
            min_w = min(min_w, min_edge[u][j])
            u = dp[u][j]
    return min_w


def solution() -> None:
    """
    Time complexity O(NlogN + MlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    adj_list: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for i in range(1, n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        adj_list[x].append((i, y))
    depth: list[int] = [0] * n
    min_edge: list[list[int]] = [[float('inf')] * 31 for _ in range(n)]
    dp: list[list[int]] = [[0] * 31 for _ in range(n)]
    preprocess(n, depth, dp, min_edge, adj_list)
    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        ancestor: int = lca(u, v, depth, dp)
        min_u: int = get_min_edge(u, ancestor, depth, min_edge, dp)
        min_v: int = get_min_edge(v, ancestor, depth, min_edge, dp)
        sys.stdout.write('{}\n'.format(min(min_u, min_v)))
    


if __name__ == '__main__':
    solution()