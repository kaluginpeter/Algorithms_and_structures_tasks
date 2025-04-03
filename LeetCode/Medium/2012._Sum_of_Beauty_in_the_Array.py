# You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:
#
# 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
# 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
# 0, if none of the previous conditions holds.
# Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation: For each index i in the range 1 <= i <= 1:
# - The beauty of nums[1] equals 2.
# Example 2:
#
# Input: nums = [2,4,6,4]
# Output: 1
# Explanation: For each index i in the range 1 <= i <= 2:
# - The beauty of nums[1] equals 1.
# - The beauty of nums[2] equals 0.
# Example 3:
#
# Input: nums = [3,2,1]
# Output: 0
# Explanation: For each index i in the range 1 <= i <= 1:
# - The beauty of nums[1] equals 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 105
# 1 <= nums[i] <= 105
# Solution
# Python O(N) O(N) PrefixSum Suffix Array
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n: int = len(nums)
        left_part: list[int] = [0]
        left_max: int = 0
        for right in range(1, n):
            if nums[left_max] < nums[right]: left_part.append(2)
            elif nums[right - 1] < nums[right]: left_part.append(1)
            else: left_part.append(0)
            if nums[left_max] < nums[right]: left_max = right
        score: int = 0
        right_part: list[int] = []
        right_min: int = n - 1
        for left in range(n - 2, 0, -1):
            if nums[left] < nums[right_min]: right_part.append(2)
            elif nums[left] < nums[left + 1]: right_part.append(1)
            else: right_part.append(0)
            if nums[left] < nums[right_min]: right_min = left
            if left_part[left] == 2 and right_part[-1] == 2: score += 2
            elif left_part[left] and right_part[-1]: score += 1
        return score

# C++ O(N) O(N) PrefixSum SuffixArray
class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        int n = nums.size();
        vector<int> leftPart = {0}, rightPart;
        int leftMax = 0;
        for (int right = 1; right < n; ++right) {
            if (nums[leftMax] < nums[right]) leftPart.push_back(2);
            else if (nums[right] > nums[right - 1]) leftPart.push_back(1);
            else leftPart.push_back(0);
            if (nums[right] > nums[leftMax]) leftMax = right;
        }
        int score = 0, rightMin = n - 1;
        for (int left = n - 2; left > 0; --left) {
            if (nums[rightMin] > nums[left]) rightPart.push_back(2);
            else if (nums[left] < nums[left + 1]) rightPart.push_back(1);
            else rightPart.push_back(0);
            if (nums[left] < nums[rightMin]) rightMin = left;
            if (leftPart[left] == 2 && rightPart.back() == 2) score += 2;
            else if (leftPart[left] && rightPart.back()) ++score;
        }
        return score;
    }
};