import sys


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n
        self.min_value: list[int] = list(range(n))
        self.max_value: list[int] = list(range(n))
        self.total_weight: int = 0
    
    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union_(self, u: int, v: int, weight: int) -> None:
        u_parent: int = self.find(u)
        v_parent: int = self.find(v)
        if u_parent == v_parent: return
        self.total_weight += weight
        if self.rank[u_parent] >= self.rank[v_parent]:
            self.parent[v_parent] = u_parent
            self.rank[u_parent] += self.rank[v_parent]
            self.min_value[u_parent] = min(self.min_value[u_parent], self.min_value[v_parent])
            self.max_value[u_parent] = max(self.max_value[u_parent], self.max_value[v_parent])
        else:
            self.parent[u_parent] = v_parent
            self.rank[v_parent] += self.rank[u_parent]
            self.min_value[v_parent] = min(self.min_value[v_parent], self.min_value[u_parent])
            self.max_value[v_parent] = max(self.max_value[v_parent], self.max_value[u_parent])
    
    def get(self, x: int) -> None:
        x_parent: int = self.find(x)
        sys.stdout.write('{} {} {}\n'.format(self.min_value[x_parent], self.max_value[x_parent], self.rank[x_parent]))


def solution() -> None:
    """
    Time Complexity O(MlogN)
    Memory Complexity O(N)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    uf: UnionFind = UnionFind(n + 1)
    edges: list[tuple[int, int, int]] = []
    for _ in range(m):
        edge: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        edges.append((edge[2], edge[0], edge[1]))
    edges.sort()
    for edge in edges:
        uf.union_(edge[1], edge[2], edge[0])
    sys.stdout.write('{}\n'.format(uf.total_weight))


if __name__ == '__main__':
    solution()