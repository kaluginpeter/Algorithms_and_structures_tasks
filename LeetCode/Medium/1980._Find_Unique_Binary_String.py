# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
#
#
#
# Example 1:
#
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:
#
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:
#
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.
# Solution
class Solution(object):
    def findDifferentBinaryString(self, nums):
        top = ''
        for i in range(len(nums)):
            top += '1' if nums[i][i] == '0' else '0'
        return top


# C++ O(N) O(1) String
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        std::string output = "";
        for (int i = 0; i < nums.size(); ++i) {
            output.push_back((nums[i][i] == '0'? '1' : '0'));
        }
        return output;
    }
};

# Python O(N) O(1) String
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        output: list[str] = []
        for i in range(len(nums)):
            output.append('1' if nums[i][i] == '0' else '0')
        return ''.join(output)