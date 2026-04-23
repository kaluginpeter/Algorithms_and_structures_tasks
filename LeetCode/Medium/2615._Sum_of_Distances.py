# You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.
#
# Return the array arr.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1,1,2]
# Output: [5,0,3,4,0]
# Explanation:
# When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5.
# When i = 1, arr[1] = 0 because there is no other index with value 3.
# When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3.
# When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4.
# When i = 4, arr[4] = 0 because there is no other index with value 2.
#
# Example 2:
#
# Input: nums = [0,5,3]
# Output: [0,0,0]
# Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
#
#
# Note: This question is the same as 2121: Intervals Between Identical Elements.
# Solution
# Python O(N) O(N) PrefixSum
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left: dict[int, list[int]] = dict()
        right: dist[int, list[int]] = dict()
        n: int = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] not in right: right[nums[i]] = [0, 0]
            right[nums[i]][0] += i
            right[nums[i]][1] += 1
        output: list[int] = [0] * n
        for i in range(n):
            right[nums[i]][0] -= i
            right[nums[i]][1] -= 1
            if nums[i] not in left: left[nums[i]] = [0, 0]
            output[i] = (i * left[nums[i]][1] - left[nums[i]][0]) + (right[nums[i]][0] - i * right[nums[i]][1])
            left[nums[i]][0] += i
            left[nums[i]][1] += 1
        return output

# C++ O(N) O(N) PrefixSum
class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        std::unordered_map<int, std::pair<long long, int>> left, right;
        size_t n = nums.size();
        for (size_t i = n; i > 0; --i) {
            right[nums[i - 1]].first += i - 1;
            ++right[nums[i - 1]].second;
        }
        std::vector<long long> output(n, 0LL);
        for (size_t i = 0; i < n; ++i) {
            right[nums[i]].first -= i;
            --right[nums[i]].second;
            output[i] = (i * left[nums[i]].second - left[nums[i]].first) + (right[nums[i]].first - i * right[nums[i]].second);
            left[nums[i]].first += i;
            ++left[nums[i]].second;
        }
        return output;
    }
};