import sys


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n
        self.min_value: list[int] = list(range(n))
        self.max_value: list[int] = list(range(n))
    
    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union_(self, u: int, v: int) -> None:
        u_parent: int = self.find(u)
        v_parent: int = self.find(v)
        if u_parent == v_parent: return
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
    for _ in range(m):
        args: list[str] = sys.stdin.readline().rstrip().split()
        if args[0] == 'union':
            uf.union_(*map(int, args[1:]))
        else:
            uf.get(int(args[1]))


if __name__ == '__main__':
    solution()