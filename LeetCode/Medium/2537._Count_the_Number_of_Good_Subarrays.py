# Given an integer array nums and an integer k, return the number of good subarrays of nums.
#
# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,1,1], k = 10
# Output: 1
# Explanation: The only good subarray is the array nums itself.
# Example 2:
#
# Input: nums = [3,1,4,3,2,2,4], k = 2
# Output: 4
# Explanation: There are 4 different good subarrays:
# - [3,1,4,3,2,2] that has 2 pairs.
# - [3,1,4,3,2,2,4] that has 3 pairs.
# - [1,4,3,2,2,4] that has 2 pairs.
# - [4,3,2,2,4] that has 2 pairs.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i], k <= 109
# Solution
# Python O(N) O(D) SlidingWindow Greedy
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        hashmap: dict[int, int] = dict()
        output: int = 0
        left: int = 0
        cur_pairs: int = 0
        for right in range(n):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
            cur_pairs += hashmap[nums[right]] - 1
            while left <= right and cur_pairs >= k:
                output += n - right
                cur_pairs -= hashmap[nums[left]] - 1
                hashmap[nums[left]] -= 1
                left += 1
        return output

# C++ O(N) O(D) SlidingWindow Greedy
class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        int n = nums.size(), curPairs = 0;
        long long output = 0;
        int left = 0;
        unordered_map<int, int> hashmap;
        for (int right = 0; right < n; ++right) {
            ++hashmap[nums[right]];
            curPairs += hashmap[nums[right]] - 1;
            while (left <= right && curPairs >= k) {
                output += n - right;
                curPairs -= hashmap[nums[left]] - 1;
                --hashmap[nums[left]];
                ++left;
            }
        }
        return output;
    }
};