# You are given an integer array nums and two integers k and numOperations.
#
# You must perform an operation numOperations times on nums, where in each operation you:
#
# Select an index i that was not selected in any previous operations.
# Add an integer in the range [-k, k] to nums[i].
# Return the maximum possible frequency of any element in nums after performing the operations.
#
#
#
# Example 1:
#
# Input: nums = [1,4,5], k = 1, numOperations = 2
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1]. nums becomes [1, 4, 5].
# Adding -1 to nums[2]. nums becomes [1, 4, 4].
# Example 2:
#
# Input: nums = [5,11,20,20], k = 5, numOperations = 1
#
# Output: 2
#
# Explanation:
#
# We can achieve a maximum frequency of two by:
#
# Adding 0 to nums[1].
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
# 0 <= k <= 105
# 0 <= numOperations <= nums.length
#
# Solution
# C++ O(N + M) O(M) SweepLine
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        std::sort(nums.begin(), nums.end());
        size_t n = nums.size();
        std::vector<int> sweepLine(nums.back() + 1, 0);
        std::unordered_map<int, int> hashmap;
        for (int& num : nums) {
            ++hashmap[num];
            ++sweepLine[std::max(0, num - k)];
            if (num + k + 1 < nums.back() + 1) --sweepLine[num + k + 1];
        }
        int cnt = 0, output = 0;
        for (int i = 0; i < sweepLine.size(); ++i) {
            cnt += sweepLine[i];
            output = std::max(output, std::min(numOperations, cnt - hashmap[i]) + hashmap[i]);
        }
        return output;
    }
};

# Python O(N + M) O(M) SweepLine
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n: int = len(nums)
        sweep_line: list[int] = [0] * (nums[-1] + 1)
        hashmap: dict[int, int] = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            sweep_line[max(0, num - k)] += 1
            if num + k + 1 <= nums[-1]: sweep_line[num + k + 1] -= 1
        cnt: int = 0
        output: int = 0
        for i in range(len(sweep_line))
            cnt += sweep_line[i]
            x: int = hashmap.get(i, 0)
            output = max(output, min(numOperations, cnt - x) + x)
        return output