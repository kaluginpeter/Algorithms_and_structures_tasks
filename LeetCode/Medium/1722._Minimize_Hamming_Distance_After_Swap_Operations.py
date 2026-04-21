# You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.
#
# The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).
#
# Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.
#
#
#
# Example 1:
#
# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
# Example 2:
#
# Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# Output: 2
# Explanation: There are no allowed swaps.
# The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
# Example 3:
#
# Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
# Output: 0
#
#
# Constraints:
#
# n == source.length == target.length
# 1 <= n <= 105
# 1 <= source[i], target[i] <= 105
# 0 <= allowedSwaps.length <= 105
# allowedSwaps[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
# Solution
# Python O(Na(N) + E) O(NV) DisjointSetUnion
class DSU:
    def __init__(self, n: int, source: list[int]) -> None:
        self.rank: list[int] = [1] * n
        self.parent: list[int] = [0] * n
        self.component: list[dict[int, int]] = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            self.parent[i] = i
            self.component[i][source[i]] = 1

    def find(self, x) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, u: int, v: int) -> None:
        pu: int = self.find(u)
        pv: int = self.find(v)
        if pu == pv: return
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
            for node, freq in self.component[pv].items():
                self.component[pu][node] += freq
            self.component[pv].clear()
        else:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]
            for node, freq in self.component[pu].items():
                self.component[pv][node] += freq
            self.component[pu].clear()


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n: int = len(source)
        dsu: DSU = DSU(n, source)
        for u, v in allowedSwaps: dsu.union(u, v)
        output: int = 0
        for i in range(n):
            parent: int = dsu.find(i)
            if dsu.component[parent][target[i]]:
                dsu.component[parent][target[i]] -= 1
            else:
                output += 1
        return output

# C++ O(Na(N) + E) O(NV) DisjointSetUnion
class DSU {
private:
    std::vector<int> rank, parent;
    std::vector<std::unordered_map<int, int>> component;
public:
    DSU (int n, std::vector<int>& source) {
        rank.resize(n, 1);
        parent.resize(n);
        component.resize(n);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
            ++component[i][source[i]];
        }
    };

    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    void union_(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return;
        if (rank[px] > rank[py]) {
            rank[px] += rank[py];
            parent[py] = px;
            for (auto& node : component[py]) {
                component[px][node.first] += node.second;
            }
            component[py].clear();
        } else {
            rank[py] += rank[px];
            parent[px] = py;
            for (auto& node : component[px]) {
                component[py][node.first] += node.second;
            }
            component[px].clear();
        }
    }

    std::unordered_map<int, int>& getComponent(int x) {
        return component[x];
    }
};

class Solution {
public:
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        DSU dsu = DSU(n, source);
        for (std::vector<int>& edge : allowedSwaps) {
            dsu.union_(edge[0], edge[1]);
        }
        int output = 0;
        for (int i = 0; i < n; ++i) {
            int parent = dsu.find(i);
            std::unordered_map<int, int>& component = dsu.getComponent(parent);
            if (component[target[i]]) --component[target[i]];
            else ++output;
        }
        return output;
    }
};