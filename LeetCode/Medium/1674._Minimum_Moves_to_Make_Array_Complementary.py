# You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.
#
# The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.
#
# Return the minimum number of moves required to make nums complementary.
#
#
#
# Example 1:
#
# Input: nums = [1,2,4,3], limit = 4
# Output: 1
# Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
# Example 2:
#
# Input: nums = [1,2,2,1], limit = 2
# Output: 2
# Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
# Example 3:
#
# Input: nums = [1,2,1,2], limit = 2
# Output: 0
# Explanation: nums is already complementary.
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 105
# 1 <= nums[i] <= limit <= 105
# n is even.
# Solution
# Python O(N + L) O(L) ScanLine
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n: int = len(nums)
        diff: list[int] = [0] * 200_002
        for i in range(n >> 1):
            x: int = min(nums[i], nums[n - 1 - i])
            y: int = max(nums[i], nums[n - 1 - i])
            diff[2] += 2 # lower bound
            diff[x + 1] -= 1
            diff[x + y] -= 1
            diff[x + y + 1] += 1
            diff[y + limit + 1] += 1
        output: int = n
        counter: int = 0
        for c in range(2, (limit << 1) + 1):
            counter += diff[c]
            output = min(output, counter)
        return output

# C++ O(N + L) O(L) ScanLine
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        size_t n = nums.size();
        std::array<int, 200002> diff{};
        for (size_t i = 0; i < (n >> 1); ++i) {
            int a = std::min(nums[i], nums[n - 1 - i]);
            int b = std::max(nums[i], nums[n - 1 - i]);
            diff[2] += 2;
            diff[a + 1] -= 1;
            diff[a + b] -= 1;
            diff[a + b + 1] += 1;
            diff[b + limit + 1] += 1;
        }
        size_t output = n, counter = 0;
        for (size_t c = 2; c <= (limit << 1); ++c) {
            counter += diff[c];
            output = std::min(output, counter);
        }
        return output;
    }
};