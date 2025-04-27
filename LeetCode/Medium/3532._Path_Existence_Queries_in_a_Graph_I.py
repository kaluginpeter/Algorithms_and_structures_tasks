# You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.
#
# You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.
#
# An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).
#
# You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.
#
# Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.
#
#
#
# Example 1:
#
# Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]
#
# Output: [true,false]
#
# Explanation:
#
# Query [0,0]: Node 0 has a trivial path to itself.
# Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |1 - 3| = 2, which is greater than maxDiff.
# Thus, the final answer after processing all the queries is [true, false].
# Example 2:
#
# Input: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]
#
# Output: [false,false,true,true]
#
# Explanation:
#
# The resulting graph is:
#
#
#
# Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |2 - 5| = 3, which is greater than maxDiff.
# Query [0,2]: There is no edge between Node 0 and Node 2 because |nums[0] - nums[2]| = |2 - 6| = 4, which is greater than maxDiff.
# Query [1,3]: There is a path between Node 1 and Node 3 through Node 2 since |nums[1] - nums[2]| = |5 - 6| = 1 and |nums[2] - nums[3]| = |6 - 8| = 2, both of which are within maxDiff.
# Query [2,3]: There is an edge between Node 2 and Node 3 because |nums[2] - nums[3]| = |6 - 8| = 2, which is equal to maxDiff.
# Thus, the final answer after processing all the queries is [false, false, true, true].
#
#
# Constraints:
#
# 1 <= n == nums.length <= 105
# 0 <= nums[i] <= 105
# nums is sorted in non-decreasing order.
# 0 <= maxDiff <= 105
# 1 <= queries.length <= 105
# queries[i] == [ui, vi]
# 0 <= ui, vi < n
# Solution
# Python O(MlogN) O(N) UnionFind Graph
class DSU:
    def __init__(self, n: int) -> None:
        self.rank: list[int] = [0] * n
        self.parent: list[int] = list(range(n))

    def find(self, i: int) -> int:
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, x: int, y: int) -> None:
        x_parent: int = self.find(x)
        y_parent: int = self.find(y)
        if x_parent == y_parent: return

        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[y_parent] < self.rank[x_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ds: DSU = DSU(n)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                ds.union(i, i + 1)
        output: list[bool] = []
        for v, u in queries:
            output.append(ds.find(v) == ds.find(u))
        return output

# C++ O(MlogN) O(N) Graph UnionFind
class DSU {
private:
    vector<int> parents;
    vector<int> rank;
    int n;
public:
    DSU (int n_) : n(n_), rank(n_, 1), parents(n_, 0) {
        for (int i = 0; i < n; ++i) parents[i] = i;
    }

    int find(int x) {
        while (x != parents[x]) {
            parents[x] = parents[parents[x]];
            x = parents[x];
        }
        return x;
    }

    void union_(int x, int y) {
        int xParent = find(x);
        int yParent = find(y);
        if (xParent == yParent) return;
        if (rank[xParent] >= rank[yParent]) {
            rank[xParent] += rank[yParent];
            parents[yParent] = xParent;
        } else {
            rank[yParent] += rank[xParent];
            parents[xParent] = yParent;
        }
    }
};


class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        DSU ds(n);
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i + 1] - nums[i] <= maxDiff) ds.union_(i, i + 1);
        }
        vector<bool> output;
        for (vector<int> &query : queries) {
            output.push_back(ds.find(query[0]) == ds.find(query[1]));
        }
        return output;
    }
};