# You are given an array nums consisting of positive integers.
#
# We call two integers x and y in this problem almost equal if both integers can become equal after performing the following operation at most once:
#
# Choose either x or y and swap any two digits within the chosen number.
# Return the number of indices i and j in nums where i < j such that nums[i] and nums[j] are almost equal.
#
# Note that it is allowed for an integer to have leading zeros after performing an operation.
#
#
#
# Example 1:
#
# Input: nums = [3,12,30,17,21]
#
# Output: 2
#
# Explanation:
#
# The almost equal pairs of elements are:
#
# 3 and 30. By swapping 3 and 0 in 30, you get 3.
# 12 and 21. By swapping 1 and 2 in 12, you get 21.
# Example 2:
#
# Input: nums = [1,1,1,1,1]
#
# Output: 10
#
# Explanation:
#
# Every two elements in the array are almost equal.
#
# Example 3:
#
# Input: nums = [123,231]
#
# Output: 0
#
# Explanation:
#
# We cannot swap any two digits of 123 or 231 to reach the other.
#
#
#
# Constraints:
#
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 106
# Solution Simulation String
# Fully Simulation
# Complexity
# Time complexity O(N**4)
# Space complexity:O(N)
# Code
class Solution:
    def is_almost_equal(self, x: int, y: int) -> int:
        str_x = str(x)
        str_y = str(y)
        if len(str_x) < len(str_y):
            str_x, str_y = str_y, str_x
        # Case when needed zeros to make pairs equal
        if len(str_x) - len(str_y) != 0:
            if '0' not in str_x: return 0
            list_x = list(str_x)
            zero_idxs: list[int] = [idx for idx in range(len(list_x)) if list_x[idx] == '0']
            for zero_idx in zero_idxs:
                list_x[zero_idx], list_x[0] = list_x[0], list_x[zero_idx]
                idx_x: int = 0
                while list_x[idx_x] == '0':
                    idx_x += 1
                if str_y == ''.join(list_x[idx_x:]):
                    return 1
                list_x[zero_idx], list_x[0] = list_x[0], list_x[zero_idx]
            return 0

        diff_indices = [i for i in range(len(str_x)) if str_x[i] != str_y[i]]
        # Case when integers already equal
        if not diff_indices: return 1
        # Case when need only one swap between integers
        elif len(diff_indices) == 2:
            i, j = diff_indices
            if (str_x[i] == str_y[j] and str_x[j] == str_y[i]):
                return 1
        return 0

    def countPairs(self, nums: List[int]) -> int:
        count: int = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count += self.is_almost_equal(nums[i], nums[j])
        return count

# Greedy Choice
# Complexity
# Time complexity O(N**3logN)
# Space complexity:O(N)
# Code
class Solution:
	def countPairs(self, nums: List[int]) -> int:
		almost_equals: int = 0
		for i in range(len(nums)):
			for j in range(i + 1 , len(nums)):
				str_i: str = str(nums[i])
				str_j: str = str(nums[j])
				if len(str_i) < len(str_j):
					str_i = '0' * (len(str_j) - len(str_i)) + str_i
				elif len(str_i) > len(str_j):
					str_j = '0' * (len(str_i) - len(str_j)) + str_j
				needed: int = 0
				for index in range(len(str_j)):
					if str_i[index] != str_j[index]:
						needed += 1
				if needed <= 2 and sorted(str_i) == sorted(str_j):
					almost_equals += 1
		return almost_equals