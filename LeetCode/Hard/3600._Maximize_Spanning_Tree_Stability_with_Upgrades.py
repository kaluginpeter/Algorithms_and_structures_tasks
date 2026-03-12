# You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:
#
# ui and vi indicates an undirected edge between nodes ui and vi.
# si is the strength of the edge.
# musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.
# You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.
#
# The stability of a spanning tree is defined as the minimum strength score among all edges included in it.
#
# Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.
#
# Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.
#
#
#
# Example 1:
#
# Input: n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1
#
# Output: 2
#
# Explanation:
#
# Edge [0,1] with strength = 2 must be included in the spanning tree.
# Edge [1,2] is optional and can be upgraded from 3 to 6 using one upgrade.
# The resulting spanning tree includes these two edges with strengths 2 and 6.
# The minimum strength in the spanning tree is 2, which is the maximum possible stability.
# Example 2:
#
# Input: n = 3, edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]], k = 2
#
# Output: 6
#
# Explanation:
#
# Since all edges are optional and up to k = 2 upgrades are allowed.
# Upgrade edges [0,1] from 4 to 8 and [1,2] from 3 to 6.
# The resulting spanning tree includes these two edges with strengths 8 and 6.
# The minimum strength in the tree is 6, which is the maximum possible stability.
# Example 3:
#
# Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0
#
# Output: -1
#
# Explanation:
#
# All edges are mandatory and form a cycle, which violates the spanning tree property of acyclicity. Thus, the answer is -1.
#
#
# Constraints:
#
# 2 <= n <= 105
# 1 <= edges.length <= 105
# edges[i] = [ui, vi, si, musti]
# 0 <= ui, vi < n
# ui != vi
# 1 <= si <= 105
# musti is either 0 or 1.
# 0 <= k <= n
# There are no duplicate edges.
#
# Solution
# Python O(ElogE) O(E + N) PriorityQueue DSU
class Solution:
    components: int
    parent: list[int]
    size: list[int]
    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, u: int, v: int) -> bool:
        pu: int = self.find(u)
        pv: int = self.find(v)
        if pu == pv: return 0
        self.components -= 1
        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return 1

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        self.components = n
        self.parent = list(range(n))
        self.size = [1] * n
        must: list[int] = []
        flex: list[int] = []
        for it in edges:
            if it[3]: must.append(it)
            else: flex.append(it)
        bound: int = float('inf')
        for u, v, w, _ in must:
            bound = min(bound, w)
            if not self.union(u, v): return -1
        flex.sort(key=lambda x: -x[2])
        pq: list[int] = []
        for u, v, w, _ in flex:
            if self.union(u, v): heapq.heappush(pq, w)
        for _ in range(k):
            if not pq: break
            x: int = heapq.heappop(pq)
            bound = min(bound, 2 * x)
        if self.components != 1: return -1
        if pq: return min(bound, pq[0])
        return bound

# C++ O(ElogE) O(E + N) DSU PriorityQueue
class Solution {
public:
    int components;
    std::vector<int> parent, size;

    int union_(int u, int v){
        int pu = find(u);
        int pv = find(v);
        if (pu == pv) return 0;
        --components;
        if(size[pu] > size[pv]){
            size[pu] += size[pv];
            parent[pv] = pu;
        } else {
            size[pv] += size[pu];
            parent[pu] = pv;
        }
        return 1;
    }

    int find(int x){
        while (x != parent[parent[x]]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    int maxStability(int n, vector<vector<int>>& edges, int k) {
        components = n;
        parent.resize(n);
        size.resize(n, 1);
        for (int i = 0; i < n; ++i) parent[i] = i;
        std::vector<std::vector<int>> must, flex;
        for (auto &it : edges){
            if (it[3] == 1) must.emplace_back(it);
            else flex.emplace_back(it);
        }
        int bound = INT_MAX;
        for(auto &it : must){
            int u = it[0], v = it[1], w = it[2];
            bound = std::min(bound, w);
            if (!union_(u, v)) return -1;
        }
        std::sort(flex.begin(), flex.end(), [](vector<int>& a, vector<int>& b){
            return a[2] > b[2]; // by strength in descending order
        });
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        for (auto &it : flex){
            int u = it[0];
            int v = it[1];
            int w = it[2];
            if (union_(u, v)) pq.push(w);
        }
        while(k-- && !pq.empty()){
            int x = pq.top();
            pq.pop();
            bound = std::min(bound, 2 * x);
        }
        if (components != 1) return -1;
        if (!pq.empty()) return std::min(bound, pq.top());
        return bound;
    }
};