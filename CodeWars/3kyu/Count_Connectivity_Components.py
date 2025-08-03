# The following figure shows a cell grid with 6 cells (2 rows by 3 columns), each cell separated from the others by walls:
#
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |  |  |  |
# +--+--+--+
# This grid has 6 connectivity components of size 1. We can describe the size and number of connectivity components by the list [(1, 6)], since there are 6 components of size 1.
#
# If we tear down a couple of walls, we obtain:
#
# +--+--+--+
# |  |     |
# +  +--+--+
# |  |  |  |
# +--+--+--+
# , which has two connectivity components of size 2 and two connectivity components of size 1. The size and number of connectivity components is described by the list [(2, 2), (1, 2)].
#
# Given the following grid:
#
# +--+--+--+
# |     |  |
# +  +--+--+
# |     |  |
# +--+--+--+
# we have the connectivity components described by [(4, 1), (1, 2)].
#
# Your job is to define a function components(grid) that takes as argument a string representing a grid like in the above pictures and returns a list describing the size and number of the connectivity components. The list should be sorted in descending order by the size of the connectivity components. The grid may have any number of rows and columns.
#
# Note: The grid is always rectangular and will have all its outer walls. Only inner walls may be missing. The + are considered bearing pillars, and are always present.
#
# StringsAlgorithmsGraph Theory
# Solution
class DSU:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        x_p: int = self.find(x)
        y_p: int = self.find(y)
        if x_p == y_p: return
        if self.rank[x_p] >= self.rank[y_p]:
            self.rank[x_p] += self.rank[y_p]
            self.parent[y_p] = x_p
        else:
            self.rank[y_p] += self.rank[x_p]
            self.parent[x_p] = y_p

    def get_components(self) -> list[tuple[int, int]]:
        components: dict[int, int] = dict()
        for i in range(len(self.parent)):
            x: int = self.find(i)
            components[x] = components.get(x, 0) + 1
        counter: dict[int, int] = dict()
        for p, size in components.items():
            counter[size] = counter.get(size, 0) + 1
        return sorted([i for i in counter.items()], reverse=True)


def components(grid: str) -> list[tuple[int, int]]:
    matrix: list[str] = grid.split('\n')
    m: int = len(matrix[0]) // 3
    n: int = len(matrix) // 2
    dsu: DSU = DSU(n * m)
    for i in range(1, len(matrix), 2):
        for j in range(1, len(matrix[0]), 3):
            if j + 3 < len(matrix[0]) and matrix[i][j + 2] != '|':
                dsu.union((i // 2) * m + (j // 3), (i // 2) * m + (j // 3 + 1))
            if i + 2 < len(matrix[0]) and matrix[i + 1][j] != '-':
                dsu.union((i // 2) * m + (j // 3), (i // 2 + 1) * m + (j // 3))
    return dsu.get_components()