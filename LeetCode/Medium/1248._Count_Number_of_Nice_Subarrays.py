# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
#
#
# Constraints:
#
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
# Solutions
# HashTable and PrefixSum
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for idx in range(len(nums)):
            nums[idx] = 1 if nums[idx] % 2 != 0 else 0
        prefix_sum: int = 0
        ht: dict[int, int] = {0: 1}
        total: int = 0
        for cur in nums:
            prefix_sum += cur
            total += ht.get(prefix_sum - k, 0)
            ht[prefix_sum] = ht.get(prefix_sum, 0) + 1
        return total

# Sliding Window
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total_subarrays: int = 0
        possible_variations: int = 0
        odd_numbers_in_subarray: int = 0
        left_pointer: int = 0
        for right_pointer in range(len(nums)):
            odd_numbers_in_subarray += nums[right_pointer] & 1
            if odd_numbers_in_subarray == k:
                possible_variations = 0
                while odd_numbers_in_subarray == k:
                    odd_numbers_in_subarray -= nums[left_pointer] & 1
                    possible_variations += 1
                    left_pointer += 1
            total_subarrays += possible_variations
        return total_subarrays