# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
#
# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
#
#
#
# Example 1:
#
# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.
# Example 2:
#
# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we return -1.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# Solution
# Python O(NlogM + NlogN) O(N) HashMap Math
class Solution:
    def get_corresponding_value(self, num: int) -> int:
        accumulate: int = 0
        while num:
            accumulate += num % 10
            num //= 10
        return accumulate
#         return sum(int(digit) for digit in str(num))

    def maximumSum(self, nums: List[int]) -> int:
        hashmap: dict[int, list[int]] = dict()
        for num in nums:
            cor_value: int = self.get_corresponding_value(num)
            if cor_value not in hashmap: hashmap[cor_value] = []
            hashmap[cor_value].append(num)
        mx_num: int = -1
        for group, elements in hashmap.items():
            if len(elements) > 1:
                elements.sort()
                mx_num = max(mx_num, elements[-1] + elements[-2])
        return mx_num

# C++ O(NlogM + NlogN) O(N) HashMap Math
class Solution {
public:
    int correspondingValue(int num) {
        int accumulate = 0;
        while (num) {
            accumulate += num % 10;
            num /= 10;
        }
        return accumulate;
    }
    int maximumSum(vector<int>& nums) {
        std::unordered_map<int, std::vector<int>> hashmap;
        for (int& num : nums) {
            hashmap[correspondingValue(num)].push_back(num);
        }
        int mxNum = -1;
        for (auto& p : hashmap) {
            if (p.second.size() > 1) {
                std::sort(p.second.begin(), p.second.end());
                int n = p.second.size();
                mxNum = std::max(mxNum, p.second[n - 2] + p.second[n - 1]);
            }
        }
        return mxNum;
    }
};