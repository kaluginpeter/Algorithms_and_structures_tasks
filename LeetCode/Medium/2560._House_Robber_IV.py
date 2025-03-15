# There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.
#
# The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.
#
# You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.
#
# You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.
#
# Return the minimum capability of the robber out of all the possible ways to steal at least k houses.
#
#
#
# Example 1:
#
# Input: nums = [2,3,5,9], k = 2
# Output: 5
# Explanation:
# There are three ways to rob at least 2 houses:
# - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
# - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
# - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
# Therefore, we return min(5, 9, 9) = 5.
# Example 2:
#
# Input: nums = [2,7,9,3,1], k = 2
# Output: 2
# Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= (nums.length + 1)/2
# Solution
# Python O(NlogM) O(N) DynamicProgramming BinarySearch
class Solution:

    def can_get(self, nums: list[int], k: int, middle: int) -> bool:
        n: int = len(nums)
        dp: list[int] = [0] * (n + 1)
        for i in range(n):
            if nums[i] > middle: dp[i + 1] = dp[i]
            else: dp[i + 1] = max((dp[i - 1] if i else 0) + 1, dp[i])
        return dp[n] >= k

    def minCapability(self, nums: List[int], k: int) -> int:
        left: int = 1
        right: int = 10**10
        answer: int = right
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.can_get(nums, k, middle):
                answer = middle
                right = middle - 1
            else: left = middle + 1
        return answer

# C++ O(NlogM) O(N) DynamicProgramming BinarySearch
class Solution {
public:
    bool canGet(vector<int>& nums, int& k, long long& middle) {
        int n = nums.size();
        vector<int> dp (n + 1, 0);
        for (int i = 0; i < n; ++i) {
            if (nums[i] > middle) dp[i + 1] = dp[i];
            else dp[i + 1] = max((i > 0? dp[i - 1] : 0) + 1, dp[i]);
        }
        return dp[n] >= k;
    }
    int minCapability(vector<int>& nums, int k) {
        long long left = 1;
        long long right = 10000000000;
        int answer = INT32_MAX;
        while (left <= right) {
            long long middle = left + ((right - left) >> 1);
            if (canGet(nums, k, middle)) {
                answer = middle;
                right = middle - 1;
            } else left = middle + 1;
        }
        return answer;
    }
};