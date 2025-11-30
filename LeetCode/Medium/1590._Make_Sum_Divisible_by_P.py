# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
#
# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
#
# A subarray is defined as a contiguous block of elements in the array.
#
#
#
# Example 1:
#
# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
# Example 2:
#
# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
# Example 3:
#
# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= p <= 109
# Solution
# Python O(N) O(N) HashMap Prefix Sum
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum: int = sum(num % p for num in nums) % p
        if not total_sum: return 0
        hashmap: dict[int, int] = {0: -1}
        cur_sum: int = 0
        length: int = len(nums)
        for idx in range(len(nums)):
            cur_sum = (cur_sum + nums[idx]) % p
            remainder: int = (cur_sum - total_sum + p) % p
            if remainder in hashmap:
                length = min(length, idx - hashmap[remainder])
            hashmap[cur_sum] = idx
        return length if length != len(nums) else -1


# Python O(N) O(min(N, K)) HashMap PrefixSum
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum: int = sum(num % p for num in nums) % p
        if not total_sum: return 0
        cur_sum: int = 0
        seen: dict[int, int] = dict()
        seen[0] = -1
        n: int = len(nums)
        output: int = n
        for i in range(n):
            cur_sum = (cur_sum + nums[i]) % p
            diff: int = (cur_sum - total_sum + p) % p
            if diff in seen: output = min(output, i - seen[diff])
            seen[cur_sum] = i
        return -1 if output == n else output

# C++ O(N) O(min(N, K)) PrefixSum HashMap
class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int totalSum = 0, curSum = 0;
        for (int& num : nums) totalSum = (totalSum + num) % p;
        if (!totalSum) return 0;
        std::unordered_map<int, int> seen;
        seen[0] = -1;
        int output = -1;
        for (int i = 0; i < nums.size(); ++i) {
            curSum = (curSum + nums[i]) % p;
            int diff = (curSum - totalSum + p) % p;
            if (seen.count(diff)) output = (output == -1 ? i - seen[diff] : std::min(output, i - seen[diff]));
            seen[curSum] = i;
        }
        return (output == nums.size() ? -1 : output);
    }
};