# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].
#
# Each queries[i] represents the following action on nums:
#
# Decrement the value at each index in the range [li, ri] in nums by at most 1.
# The amount by which the value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.
#
# Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.
#
#
#
# Example 1:
#
# Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
#
# Output: 1
#
# Explanation:
#
# After removing queries[2], nums can still be converted to a zero array.
#
# Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
# Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
# Example 2:
#
# Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]
#
# Output: 2
#
# Explanation:
#
# We can remove queries[2] and queries[3].
#
# Example 3:
#
# Input: nums = [1,2,3,4], queries = [[0,3]]
#
# Output: -1
#
# Explanation:
#
# nums cannot be converted to a zero array even after using all the queries.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105
# 1 <= queries.length <= 105
# queries[i].length == 2
# 0 <= li <= ri < nums.length
# Solution
# Python O(MlogM + N) O(N + M) PriorityQueue Greedy
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda query: query[0])
        max_heap: list[int] = []
        sweep_line: list[int] = [0] * (len(nums) + 1)
        counter: int = 0
        j: int = 0
        for i in range(len(nums)):
            counter += sweep_line[i]
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(max_heap, -queries[j][1])
                j += 1
            while counter < nums[i] and max_heap and -max_heap[0] >= i:
                counter += 1
                sweep_line[-heapq.heappop(max_heap) + 1] -= 1
            if counter < nums[i]: return -1
        return len(max_heap)

# C++ O(MlogM + N) O(N + M) PriorityQueue Greedy
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        sort(queries.begin(), queries.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[0] < b[0];
             });
        priority_queue<int> maxHeap;
        vector<int> sweepLine(nums.size() + 1, 0);
        int operations = 0;
        for (int i = 0, j = 0; i < nums.size(); ++i) {
            operations += sweepLine[i];
            while (j < queries.size() && queries[j][0] == i) {
                maxHeap.push(queries[j][1]);
                ++j;
            }
            while (operations < nums[i] && !maxHeap.empty() && maxHeap.top() >= i) {
                ++operations;
                sweepLine[maxHeap.top() + 1] -= 1;
                maxHeap.pop();
            }
            if (operations < nums[i]) return -1;
        }
        return maxHeap.size();
    }
};