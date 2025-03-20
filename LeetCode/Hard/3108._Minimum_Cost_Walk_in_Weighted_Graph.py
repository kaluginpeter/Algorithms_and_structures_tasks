# There is an undirected weighted graph with n vertices labeled from 0 to n - 1.
#
# You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.
#
# A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.
#
# The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.
#
# You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.
#
# Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.
#
#
#
# Example 1:
#
# Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]
#
# Output: [1,-1]
#
# Explanation:
#
#
# To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).
#
# In the second query, there is no walk between nodes 3 and 4, so the answer is -1.
#
# Example 2:
#
# Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]
#
# Output: [0]
#
# Explanation:
#
#
# To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).
#
#
#
# Constraints:
#
# 2 <= n <= 105
# 0 <= edges.length <= 105
# edges[i].length == 3
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= wi <= 105
# 1 <= query.length <= 105
# query[i].length == 2
# 0 <= si, ti <= n - 1
# si != ti
# Solution
# Python O(ElogV) O(V) DisjointSetUnion Graph
class DSU:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = [-1] * n
        self.cost: list[int] = [2097151] * n
        self.rank: list[int] = [1] * n

    def find_parent(self, x: int) -> int:
        if self.parent[x] == -1: self.parent[x] = x
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x: int, y: int, weight: int) -> None:
        parent_x: int = self.find_parent(x)
        parent_y: int = self.find_parent(y)
        if parent_x == parent_y:
            self.cost[parent_x] &= weight
            return
        if self.rank[parent_x] > self.rank[parent_y]:
            self.rank[parent_x] += self.rank[parent_y]
            self.parent[parent_y] = parent_x
            self.cost[parent_x] &= weight & self.cost[parent_y]
        else:
            self.rank[parent_y] += self.rank[parent_x]
            self.parent[parent_x] = parent_y
            self.cost[parent_y] &= weight & self.cost[parent_x]

    def get_min_path(self, x: int, y: int) -> int:
        parent_x: int = self.find_parent(x)
        parent_y: int = self.find_parent(y)
        if parent_x != parent_y: return -1
        return self.cost[parent_x]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu: DSU = DSU(n)
        for u, v, weight in edges:
            dsu.union(u, v, weight)
        output: list[int] = [-1] * len(query)
        for i in range(len(query)):
            output[i] = dsu.get_min_path(*query[i])
        return output

# C++ O(ElogV) O(V) DisjointSetUnion Graph
class DSU {
private:
    vector<int> parent;
    vector<int> rank;
    vector<unsigned int> costs;
public:
    DSU(int n) {
        parent.resize(n, -1);
        rank.resize(n, 1);
        costs.resize(n, -1);
    };

    int findParent(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return parent[x];
    }

    void union_(int& x, int& y, int& weight) {
        if (parent[x] == -1) parent[x] = x;
        if (parent[y] == -1) parent[y] = y;
        int parentX = findParent(x);
        int parentY = findParent(y);
        if (parentX == parentY) {
            costs[parentX] = costs[parentX] & weight & costs[parentY];
            return;
        }
        if (rank[parentX] > rank[parentY]) {
            rank[parentX] += rank[parentY];
            parent[parentY] = parentX;
            costs[parentX] = costs[parentX] & weight & costs[parentY];
        } else {
            rank[parentY] += rank[parentX];
            parent[parentX] = parentY;
            costs[parentY] = costs[parentY] & weight & costs[parentX];
        }
    }
    int findMinPath(int& u, int& v) {
        if (parent[u] == -1) parent[u] = u;
        if (parent[v] == -1) parent[v] = v;
        int parentX = findParent(u);
        int parentY = findParent(v);
        if (parentX != parentY) return -1;
        return costs[parentX];
    }
};


class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        DSU dsu (n);
        for (vector<int>& edge : edges) {
            int& u = edge[0];
            int& v = edge[1];
            int& w = edge[2];
            dsu.union_(u, v, w);
        }
        vector<int> output (query.size(), -1);
        for (int i = 0; i < query.size(); ++i) {
            output[i] = dsu.findMinPath(query[i][0], query[i][1]);
        }
        return output;
    }
};