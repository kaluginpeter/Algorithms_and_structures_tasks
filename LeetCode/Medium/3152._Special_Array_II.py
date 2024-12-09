# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#
# You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that
# subarray
#  nums[fromi..toi] is special or not.
#
# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
#
#
#
# Example 1:
#
# Input: nums = [3,4,1,2,6], queries = [[0,4]]
#
# Output: [false]
#
# Explanation:
#
# The subarray is [3,4,1,2,6]. 2 and 6 are both even.
#
# Example 2:
#
# Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
#
# Output: [false,true]
#
# Explanation:
#
# The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
# The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
# Solution Sorting O(NlogN) O(N)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n: int = len(queries)
        output: list[bool] = [True] * n
        for i in range(n):
            queries[i].append(i)
        queries.sort(key=lambda x: (x[0], -x[1]))
        idx: int = 0
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                while idx < n:
                    if i - 1 < queries[idx][0]:
                        break
                    if i <= queries[idx][1]:
                        output[queries[idx][-1]] = False
                        idx += 1
                    else:
                        idx += 1
        return output
# Solution Prefix Sum O(N) O(N)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n: int = len(queries)
        output: list[int] = [1]
        for item in range(1, len(nums)):
            x: int = output[-1]
            output.append(x if nums[item - 1] % 2 == nums[item] % 2 else x + 1)
        for i in range(n):
            x, y = queries[i]
            queries[i] = output[y] - output[x] == y - x
        return queries

# Solution 12.09.2024
# C++ O(N) O(N) PrefixSum
class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        std::vector<int> prefixSum;
        int nonSpecials = 0;
        for (int idx = 0; idx < nums.size(); ++idx) {
            if (idx && (nums[idx - 1] % 2 == nums[idx] % 2)) {
                ++nonSpecials;
            }
            prefixSum.push_back(nonSpecials);
        }
        std::vector<bool> output;
        for (std::vector<int>& query : queries) {
            int start = query[0];
            int end = query[1];
            int invalids = prefixSum[end] - prefixSum[start];
            output.push_back(invalids == 0);
        }
        return output;
    }
};

# Python O(N) O(N) PrefixSum
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_sum: list[int] = []
        non_specials: int = 0
        for idx in range(len(nums)):
            if idx and nums[idx - 1] & 1 == nums[idx] & 1:
                non_specials += 1
            prefix_sum.append(non_specials)
        output: list[bool] = []
        for query in queries:
            start, end = query
            invalids: int = prefix_sum[end]
            invalids -= prefix_sum[start]
            output.append(invalids == 0)
        return output