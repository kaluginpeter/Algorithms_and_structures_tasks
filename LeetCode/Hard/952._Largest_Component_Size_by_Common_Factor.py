# You are given an integer array of unique positive integers nums. Consider the following graph:
#
# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.
#
#
#
# Example 1:
#
#
# Input: nums = [4,6,15,35]
# Output: 4
# Example 2:
#
#
# Input: nums = [20,50,9,63]
# Output: 2
# Example 3:
#
#
# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 105
# All the values of nums are unique.
# Solution
# C++ O(Nsqrt(M)) O(M) Union Find
class DSU {
public:
    vector<int> rank, parent;
    DSU(int n) {
        rank.resize(n, 0);
        parent.resize(n, 0);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (x == parent[x])
            return x;
        return parent[x] = find(parent[x]);
    }
    void UnionByRank(int x, int y) {
        int x_parent = find(x);
        int y_parent = find(y);

        if (x_parent == y_parent)
            return;

        if (rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;
        } else if (rank[y_parent] > rank[x_parent]) {
            parent[x_parent] = y_parent;
        } else {
            parent[x_parent] = y_parent;
            rank[y_parent]++;
        }
    }
};

class Solution {
public:
    int largestComponentSize(vector<int>& nums) {
        int n = *max_element(nums.begin(), nums.end()) + 1;
        DSU dsu(n);
        for (int& num : nums) {
            for (int factor = 2; factor * factor <= num; factor++) {
                if (num % factor == 0) {
                    dsu.UnionByRank(num, factor);
                    dsu.UnionByRank(num, num / factor);
                }

            }
        }
        int result = 0;
        unordered_map<int, int> mp;
        for (int& val : nums) {
            int parent = dsu.find(val);
            mp[parent]++;
            result = max(result, mp[parent]);
        }
        return result;
    }
};

# Python O(Nsqrt(M)) O(M) UnionFind
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unionFind(self, x: int, y: int) -> None:
        parent_x: int = self.find(x)
        parent_y: int = self.find(y)
        if parent_x == parent_y:
            return
        if self.rank[parent_x] >= self.rank[parent_y]:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += self.rank[parent_y]
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += self.rank[parent_x]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        UF: UnionFind = UnionFind(max(nums) + 1)
        for num in nums:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    UF.unionFind(num, factor)
                    UF.unionFind(num, num // factor)
        answer: int = 0
        hashmap: dict[int, int] = dict()
        for num in nums:
            parent: int = UF.find(num)
            hashmap[parent] = hashmap.get(parent, 0) + 1
            answer = max(answer, hashmap[parent])
        return answer