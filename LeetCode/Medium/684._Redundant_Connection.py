# In this problem, a tree is an undirected graph that is connected and has no cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
#
#
#
# Example 1:
#
#
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:
#
#
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#
#
# Constraints:
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
# Solution Union Find O(N) O(N)
class UnionFind:
    def __init__(self, count_nodes: int) -> None:
        self.parents: list[int] = list(range(count_nodes + 1))
        self.ranks: list[int] = [1] * (count_nodes + 1)
        self.connections: int = count_nodes

    def find(self, node: int) -> int:
        while node != self.parents[node]:
            node = self.parents[node]
            self.parents[node] = self.parents[self.parents[node]]
        return self.parents[node]

    def union(self, node_x: int, node_y: int) -> bool:
        parent_x, parent_y = self.find(node_x), self.find(node_y)
        if parent_x == parent_y:
            return False
        elif self.ranks[parent_x] > self.ranks[parent_y]:
            self.ranks[parent_x] += self.ranks[parent_y]
            self.parents[parent_y] = parent_x
        else:
            self.ranks[parent_y] += self.ranks[parent_x]
            self.parents[parent_x] = parent_y
        self.connections -= 1
        return True

    def is_connected(self) -> bool:
        return self.connections <= 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoints_set = UnionFind(len(edges))
        for start_vertex, end_vertex in edges:
            if not disjoints_set.union(start_vertex, end_vertex):
                return [start_vertex, end_vertex]

# Python O(N) O(N) Disjoint Set Union
class DSU:
    def __init__(self, n: int) -> None:
        self.ranks: list[int] = [1] * (n + 1)
        self.parents: list[int] = list(range(n + 1))
    def find_parent(self, x: int) -> int:
        while self.parents[x] != self.parents[self.parents[x]]:
            self.parents[x] = self.parents[self.parents[x]]
        return self.parents[x]
    def union(self, x: int, y: int) -> bool:
        x_root: int = self.find_parent(x)
        y_root: int = self.find_parent(y)
        if x_root == y_root: return False
        if self.ranks[x_root] >= self.ranks[y_root]:
            self.parents[y_root] = x_root
            self.ranks[x_root] += self.ranks[y_root]
        else:
            self.parents[x_root] = y_root
            self.ranks[y_root] += self.ranks[x_root]
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n: int = len(edges)
        dsu: DSU = DSU(n)
        for edge in edges:
            if not dsu.union(*edge):
                return edge

# C++ O(N) O(N) Disjoint Set Union
class DSU {
public:
    std::vector<int> ranks;
    std::vector<int> parents;
    DSU(int n) {
        ranks = std::vector<int>(n + 1);
        parents = std::vector<int>(n + 1, 1);
        for (int i = 0; i <= n; ++i) {
            parents[i] = i;
        }
    };
    int findParent(int x) {
        while (parents[x] != parents[parents[x]]) {
            parents[x] = parents[parents[x]];
        }
        return parents[x];
    }
    bool unionFind(int x, int y) {
        int xRoot = findParent(x);
        int yRoot = findParent(y);
        if (xRoot == yRoot) return false;
        if (ranks[xRoot] >= ranks[yRoot]) {
            ranks[xRoot] += ranks[yRoot];
            parents[yRoot] = xRoot;
        } else {
            ranks[yRoot] += ranks[xRoot];
            parents[xRoot] = yRoot;
        }
        return true;
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        DSU dsu = DSU(n);
        for (std::vector<int>& edge : edges) {
            if (!dsu.unionFind(edge[0], edge[1])) return edge;
        }
        return {0, 0};
    }
};