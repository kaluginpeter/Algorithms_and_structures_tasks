# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].
#
# For each queries[i]:
#
# Select a subset of indices within the range [li, ri] in nums.
# Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.
#
# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.
#
# A subset of an array is a selection of elements (possibly none) of the array.
#
#
#
# Example 1:
#
# Input: nums = [1,0,1], queries = [[0,2]]
#
# Output: true
#
# Explanation:
#
# For i = 0:
# Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
# The array will become [0, 0, 0], which is a Zero Array.
# Example 2:
#
# Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
#
# Output: false
#
# Explanation:
#
# For i = 0:
# Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
# The array will become [4, 2, 1, 0].
# For i = 1:
# Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
# The array will become [3, 1, 0, 0], which is not a Zero Array.
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
# Python O(N) O(N) Sweep Line
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n: int = len(nums)
        diff_arr: list[int] = [0] * n
        for query in queries:
            left, right = query
            diff_arr[left] += 1
            if right + 1 < n:
                diff_arr[right + 1] -= 1
        counter: int = 0
        for idx in range(n):
            counter += diff_arr[idx]
            if counter < nums[idx]:
                return False
        return True

# C++ O(N) O(N) Sweep Line
class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        std::vector<int> diffArr(n, 0);
        for (std::vector<int>& query : queries) {
            int left = query[0];
            int right = query[1];
            ++diffArr[left];
            if (right + 1 < n) {
                --diffArr[right + 1];
            }
        }
        int counter = 0;
        for (int index = 0; index < n; ++index) {
            counter += diffArr[index];
            if (counter < nums[index]) {
                return false;
            }
        }
        return true;
    }
};

# Python O(N + M) O(N) SweepLine
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n: int = len(nums)
        sweep_line: list[int] = [0] * (n + 1)
        for left, right in queries:
            sweep_line[left] += 1
            sweep_line[right + 1] -= 1
        counter: int = 0
        for i in range(n):
            counter += sweep_line[i]
            if nums[i] > counter: return False
        return True

# C++ O(N + M) O(N) SweepLine
class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> sweepLine(n + 1, 0);
        for (vector<int> &query : queries) {
            ++sweepLine[query[0]];
            --sweepLine[query[1] + 1];
        }
        int counter = 0;
        for (int idx = 0; idx < n; ++idx) {
            counter += sweepLine[idx];
            if (nums[idx] > counter) return false;
        }
        return true;
    }
};