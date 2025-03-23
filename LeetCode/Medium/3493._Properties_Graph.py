# You are given a 2D integer array properties having dimensions n x m and an integer k.
#
# Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.
#
# Construct an undirected graph where each index i corresponds to properties[i]. There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k, where i and j are in the range [0, n - 1] and i != j.
#
# Return the number of connected components in the resulting graph.
#
#
#
# Example 1:
#
# Input: properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1
#
# Output: 3
#
# Explanation:
#
# The graph formed has 3 connected components:
#
#
#
# Example 2:
#
# Input: properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2
#
# Output: 1
#
# Explanation:
#
# The graph formed has 1 connected component:
#
#
#
# Example 3:
#
# Input: properties = [[1,1],[1,1]], k = 2
#
# Output: 2
#
# Explanation:
#
# intersect(properties[0], properties[1]) = 1, which is less than k. This means there is no edge between properties[0] and properties[1] in the graph.
#
#
#
# Constraints:
#
# 1 <= n == properties.length <= 100
# 1 <= m == properties[i].length <= 100
# 1 <= properties[i][j] <= 100
# 1 <= k <= m
# Solution
# O(NND) O(N) UnionFind Set
class DSU:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n
        self.components: int = n

    def find_parent(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        parent_x: int = self.find_parent(x)
        parent_y: int = self.find_parent(y)
        if parent_x == parent_y: return
        self.components -= 1
        if self.rank[parent_x] > self.rank[parent_y]:
            self.rank[parent_x] += self.rank[parent_y]
            self.parent[parent_y] = parent_x
        else:
            self.rank[parent_y] += self.rank[parent_x]
            self.parent[parent_x] = parent_y


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n: int = len(properties)
        dsu: DSU = DSU(n)
        us_n: list[set[int]] = [set(properties[i]) for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if len(us_n[i] & us_n[j]) >= k:
                    dsu.union(i, j)
        return dsu.components

# C++ O(NND) O(N) UnionFind Set
class DSU {
private:
    vector<int> parent;
    vector<int> rank;
    int components;
public:
    DSU(int n) {
        parent.resize(n, -1);
        rank.resize(n, 1);
        components = n;
    };

    int findParent(int x) {
        if (parent[x] == -1) parent[x] = x;
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return parent[x];
    }

    int getComponents() {
        return components;
    }

    void union_(int& x, int& y) {
        int parentX = findParent(x);
        int parentY = findParent(y);
        if (parentX == parentY) return;
        --components;
        if (rank[parentX] > rank[parentY]) {
            rank[parentX] += rank[parentY];
            parent[parentY] = parentX;
        } else {
            rank[parentY] += rank[parentX];
            parent[parentX] = parentY;
        }
    }
};

class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        DSU dsu (n);
        vector<unordered_set<int>> usN;
        for (int i = 0; i < n; ++i) {
            usN.push_back(unordered_set<int>(properties[i].begin(), properties[i].end()));
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                int both = 0;
                for (auto& num : usN[j]) {
                    if (usN[i].count(num)) ++both;
                }
                if (both >= k) dsu.union_(i, j);
            }
        }
        return dsu.getComponents();
    }
};