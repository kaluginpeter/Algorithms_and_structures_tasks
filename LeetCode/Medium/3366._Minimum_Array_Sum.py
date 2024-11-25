# You are given an integer array nums and three integers k, op1, and op2.
#
# You can perform the following operations on nums:
#
# Operation 1: Choose an index i and divide nums[i] by 2, rounding up to the nearest whole number. You can perform this operation at most op1 times, and not more than once per index.
# Operation 2: Choose an index i and subtract k from nums[i], but only if nums[i] is greater than or equal to k. You can perform this operation at most op2 times, and not more than once per index.
# Note: Both operations can be applied to the same index, but at most once each.
#
# Return the minimum possible sum of all elements in nums after performing any number of operations.
#
#
#
# Example 1:
#
# Input: nums = [2,8,3,19,3], k = 3, op1 = 1, op2 = 1
#
# Output: 23
#
# Explanation:
#
# Apply Operation 2 to nums[1] = 8, making nums[1] = 5.
# Apply Operation 1 to nums[3] = 19, making nums[3] = 10.
# The resulting array becomes [2, 5, 3, 10, 3], which has the minimum possible sum of 23 after applying the operations.
# Example 2:
#
# Input: nums = [2,4,3], k = 3, op1 = 2, op2 = 1
#
# Output: 3
#
# Explanation:
#
# Apply Operation 1 to nums[0] = 2, making nums[0] = 1.
# Apply Operation 1 to nums[1] = 4, making nums[1] = 2.
# Apply Operation 2 to nums[2] = 3, making nums[2] = 0.
# The resulting array becomes [1, 2, 0], which has the minimum possible sum of 3 after applying the operations.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 105
# 0 <= k <= 105
# 0 <= op1, op2 <= nums.length
# Solution
# Python O(N * op1 * op2) O(N * op1 * op2) DynamicProgramming
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n: int = len(nums)
        dp: list[list[list[int]]] = [
            [
                [float('inf')] * (op2 + 1) for _ in range(op1 + 1)
            ] for _ in range(n + 1)
        ]
        for x in range(op1 + 1):
            for y in range(op2 + 1):
                dp[0][x][y] = 0
        for i in range(1, n + 1):
            for x in range(op1 + 1):
                for y in range(op2 + 1):
                    dp[i][x][y]: int = dp[i-1][x][y] + nums[i-1]
                    if x > 0: # Try to divide by 2
                        halved = (nums[i-1] + 1) // 2
                        dp[i][x][y] = min(dp[i][x][y], dp[i-1][x-1][y] + halved)
                    if y > 0 and nums[i-1] >= k: # Try to subtract k
                        reduced: int = nums[i-1] - k
                        dp[i][x][y] = min(dp[i][x][y], dp[i-1][x][y-1] + reduced)
                    if x > 0 and y > 0 and nums[i-1] >= k: # Try to subtract and divide by 2
                        reduced_then_halved: int = ((nums[i-1] - k + 1) // 2)
                        dp[i][x][y] = min(dp[i][x][y], dp[i-1][x-1][y-1] + max(reduced_then_halved, 0))
                    if x > 0 and y > 0 and (nums[i-1] + 1) // 2 >= k: # Try to divide by 2 and subtract
                        halved_then_reduced: int = ((nums[i-1] + 1) // 2) - k
                        dp[i][x][y] = min(dp[i][x][y], dp[i-1][x-1][y-1] + max(halved_then_reduced, 0))
        return dp[n][op1][op2]

# C++ O(N * op1 * op2) O(N * op1 * op2) DynamicProgramming
class Solution {
public:
    int minArraySum(vector<int>& nums, int k, int op1, int op2) {
        int n = nums.size();
        std::vector<std::vector<std::vector<int>>> dp(
            n + 1, std::vector<std::vector<int>>(
                op1 + 1, std::vector<int>(
                    op2 + 1, 100001
                )
            )
        );
        for (int x = 0; x < op1 + 1; ++x) {
            for (int y = 0; y < op2 + 1; ++y) {
                dp[0][x][y] = 0;
            }
        }
        for (int i = 1; i < n + 1; ++i) {
            for (int x = 0; x < op1 + 1; ++x) {
                for (int y = 0; y < op2 + 1; ++y) {
                    dp[i][x][y] = dp[i - 1][x][y] + nums[i - 1];
                    if (x > 0) { // Try to divide by 2
                        int halved = (nums[i - 1] + 1) / 2;
                        dp[i][x][y] = std::min(dp[i][x][y], dp[i - 1][x - 1][y] + halved);
                    }
                    if (y > 0 && nums[i - 1] >= k) { // Try to subract k
                        int reduced = nums[i - 1] - k;
                        dp[i][x][y] = std::min(dp[i][x][y], dp[i - 1][x][y - 1] + reduced);
                    }
                    if (x > 0 && y > 0 && nums[i - 1] >= k) { // Try to subtract and divide by 2
                        int reducedThanHalved = std::max((nums[i - 1] - k + 1) / 2, 0);
                        dp[i][x][y] = std::min(dp[i][x][y], dp[i - 1][x - 1][y - 1] + reducedThanHalved);
                    }
                    if (x > 0 && y > 0 && (nums[i - 1] + 1) / 2 >= k) { // Try to divide by 2 and subract
                        int halvedThanReduced = std::max((nums[i - 1] + 1) / 2 - k, 0);
                        dp[i][x][y] = std::min(dp[i][x][y], dp[i - 1][x - 1][y - 1] + halvedThanReduced);
                    }
                }
            }
        }
        return dp[n][op1][op2];
    }
};
