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
    


def solution() -> None:
    """
    Time Complexity O((NM)log(NM))
    Memory Complexity O(NM)
    """
    n, m = map(int, sys.stdin.readline().rstrip().split())
    uf: UnionFind = UnionFind(n * m + 2)
    grid: list[list[int]] = [[]]
    for _ in range(n):
        row: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        grid.append([0] + row)
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if grid[r][c] == 1:
                uf.union_((r - 1) * m + c, (r - 1) * m + c + m)
            elif grid[r][c] == 2:
                uf.union_((r - 1) * m + c, (r - 1) * m + c + 1)
            elif grid[r][c] == 3:
                uf.union_((r - 1) * m + c, (r - 1) * m + c + m)
                uf.union_((r - 1) * m + c, (r - 1) * m + c + 1)
    score: int = 0
    moves: list[tuple[int, int, int]] = []
    for r in range(1, n):
        for c in range(1, m + 1):
            if uf.find((r - 1) * m + c) != uf.find((r - 1) * m + c + m):
                score += 1
                moves.append((r, c, 1))
                uf.union_((r - 1) * m + c, (r - 1) * m + c + m)
    for r in range(1, n + 1):
        for c in range(1, m):
            if uf.find((r - 1) * m + c) != uf.find((r - 1) * m + c + 1):
                score += 2
                moves.append((r, c, 2))
                uf.union_((r - 1) * m + c, (r - 1) * m + c + 1)
    sys.stdout.write('{} {}\n'.format(len(moves), score))
    if not score: return
    sys.stdout.write('{}'.format('\n'.join((' '.join(map(str, move))) for move in moves)))

if __name__ == '__main__':
    solution()