# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
#
# You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
#
# Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:
#
# Get the XOR of all the values of the nodes for each of the three components respectively.
# The difference between the largest XOR value and the smallest XOR value is the score of the pair.
# For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
# Return the minimum score of any possible pair of edge removals on the given tree.
#
#
#
# Example 1:
#
#
# Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
# Output: 9
# Explanation: The diagram above shows a way to make a pair of removals.
# - The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
# - The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
# - The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
# The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
# It can be shown that no other pair of removals will obtain a smaller score than 9.
# Example 2:
#
#
# Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
# Output: 0
# Explanation: The diagram above shows a way to make a pair of removals.
# - The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
# - The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
# - The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
# The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
# We cannot obtain a smaller score than 0.
#
#
# Constraints:
#
# n == nums.length
# 3 <= n <= 1000
# 1 <= nums[i] <= 108
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges represents a valid tree.
# Solution
# Python O(N^2) O(N) Depth-First-Search
class Solution:
    subtree_xor: list[int] = []
    adj: list[list[int]] = []
    tin: list[int] = []
    tout: list[int] = []
    timer: int = 0

    def dfs(self, u: int, p: int, nums: list[int]) -> None:
        self.timer += 1
        self.tin[u] = self.timer
        self.subtree_xor[u] = nums[u]
        for v in self.adj[u]:
            if v == p: continue
            self.dfs(v, u, nums)
            self.subtree_xor[u] ^= self.subtree_xor[v]
        self.timer += 1
        self.tout[u] = self.timer

    def is_ancestor(self, u: int, v: int) -> bool:
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n: int = len(nums)
        self.subtree_xor = [0] * n
        self.tin = [0] * n
        self.tout = [0] * n
        self.timer = 0
        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.dfs(0, -1, nums)
        total_xor: int = self.subtree_xor[0]
        output: int = float('inf')
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                u1, v1 = edges[i]
                u2, v2 = edges[j]
                if self.tin[u1] > self.tin[v1]: u1, v1 = v1, u1
                if self.tin[u2] > self.tin[v2]: u2, v2 = v2, u2
                child1: int = v1
                child2: int = v2
                score1: int = 0
                score2: int = 0
                score3: int = 0
                if self.is_ancestor(child1, child2):
                    score1 = self.subtree_xor[child2]
                    score2 = self.subtree_xor[child1] ^ self.subtree_xor[child2]
                    score3 = total_xor ^ self.subtree_xor[child1]
                elif self.is_ancestor(child2, child1):
                    score1 = self.subtree_xor[child1]
                    score2 = self.subtree_xor[child2] ^ self.subtree_xor[child1]
                    score3 = total_xor ^ self.subtree_xor[child2]
                else:
                    score1 = self.subtree_xor[child1]
                    score2 = self.subtree_xor[child2]
                    score3 = total_xor ^ score1 ^ score2
                output = min(output, max(score1, score2, score3) - min(score1, score2, score3))
        return output

# C++ O(N^2) O(N) Depth-First-Search
class Solution {
public:
    std::vector<int> subtree_xor;
    std::vector<std::vector<int>> adj;
    std::vector<int> tin, tout;
    int timer;
    void dfs(int u, int p, const std::vector<int>& nums) {
        tin[u] = ++timer;
        subtree_xor[u] = nums[u];
        for (int v : adj[u]) {
            if (v != p) {
                dfs(v, u, nums);
                subtree_xor[u] ^= subtree_xor[v];
            }
        }
        tout[u] = ++timer;
    }
    bool is_ancestor(int u, int v) {
        return tin[u] <= tin[v] && tout[u] >= tout[v];
    }
    int minimumScore(std::vector<int>& nums, std::vector<std::vector<int>>& edges) {
        int n = nums.size();
        adj.assign(n, {});
        subtree_xor.assign(n, 0);
        tin.assign(n, 0);
        tout.assign(n, 0);
        timer = 0;
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        dfs(0, -1, nums);
        int total_xor = subtree_xor[0];
        int min_score_diff = INT_MAX;
        for (int i = 0; i < edges.size(); ++i) {
            for (int j = i + 1; j < edges.size(); ++j) {
                int u1 = edges[i][0], v1 = edges[i][1];
                int u2 = edges[j][0], v2 = edges[j][1];
                if (tin[u1] > tin[v1]) std::swap(u1, v1);
                if (tin[u2] > tin[v2]) std::swap(u2, v2);
                int child1 = v1;
                int child2 = v2;
                int score1, score2, score3;
                if (is_ancestor(child1, child2)) {
                    score1 = subtree_xor[child2];
                    score2 = subtree_xor[child1] ^ subtree_xor[child2];
                    score3 = total_xor ^ subtree_xor[child1];
                } else if (is_ancestor(child2, child1)) {
                    score1 = subtree_xor[child1];
                    score2 = subtree_xor[child2] ^ subtree_xor[child1];
                    score3 = total_xor ^ subtree_xor[child2];
                } else {
                    score1 = subtree_xor[child1];
                    score2 = subtree_xor[child2];
                    score3 = total_xor ^ score1 ^ score2;
                }
                int max_val = std::max({score1, score2, score3});
                int min_val = std::min({score1, score2, score3});
                min_score_diff = std::min(min_score_diff, max_val - min_val);
            }
        }
        return min_score_diff;
    }
};