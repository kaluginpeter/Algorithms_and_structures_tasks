import sys


def dfs(v: int, adj_list: list[list[int]], dp: list[list[int]], time_in: list[int], time_out: list[int], t: list[int]) -> None:
    time_in[v] = t[0]
    t[0] += 1
    for u in adj_list[v]:
        dp[u][0] = v
        dfs(u, adj_list, dp, time_in, time_out, t)
    time_out[v] = t[0]
    t[0] += 1


def is_ancestor(u: int, v: int, time_in: list[int], time_out: list[int]) -> bool:
    return time_in[u] <= time_in[v] and time_out[v] <= time_out[u]


def lca(u: int, v: int, dp: list[list[int]], time_in: list[int], time_out: list[int]) -> int:
    if is_ancestor(u, v, time_in, time_out): return u
    elif is_ancestor(v, u, time_in, time_out): return v
    for level in range(30, -1, -1):
        if not is_ancestor(dp[u][level], v, time_in, time_out):
            u = dp[u][level]
    return dp[u][0]


def solution() -> None:
    """
    Time Complexity O(NlogN + MlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    adj_list: list[list[int]] = [[] for _ in range(n)]
    vertices: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for i in range(1, n):
        parent: int = next(vertices)
        adj_list[parent].append(i)
    time_in: list[int] = [0] * n
    time_out: list[int] = [0] * n
    dp: list[list[int]] = [[0] * 31 for _ in range(n)]
    dfs(0, adj_list, dp, time_in, time_out, [0])
    for v in range(n):
        for level in range(1, 31):
            dp[v][level] = dp[dp[v][level - 1]][level - 1]
    m: int = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write('{}\n'.format(lca(u, v, dp, time_in, time_out)))
    


if __name__ == '__main__':
    solution()