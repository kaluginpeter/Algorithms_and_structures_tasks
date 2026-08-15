/*
You are given an integer array nums.

Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.



Example 1:

Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

Example 2:

Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.



Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
*/
// Solution
// C++ O(N) O(1) BitTheory
class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int overall = 0;
        for (int& num : nums) overall ^= num;
        if (overall) return nums.size();
        for (int& num : nums) {
            if (overall ^ num) return nums.size() - 1;
        }
        return 0;
    }
};
// Python O(N) O(1) BitTheory
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n: int = len(nums)
        output: int = 0
        for num in nums:
            output ^= num
        if output: return n
        for num in nums:
            if output ^ num: return n - 1
        return 0

// Go O(N) O(1) BitTheory
func longestSubsequence(nums []int) int {
    var output int = 0
    var n int = len(nums)
    for _, num := range(nums) {
        output ^= num
    }
    if output > 0 {
        return n
    }
    for _, num := range(nums) {
        if output ^ num > 0 {
            return n - 1
        }
    }
    return 0
}