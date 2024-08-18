# A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
#
# For example, these are arithmetic sequences:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic:
#
# 1, 1, 2, 5, 7
# You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.
#
# Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
# Output: [true,false,true]
# Explanation:
# In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
# In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
# In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
# Example 2:
#
# Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
# Output: [false,true,false,false,true,true]
#
#
# Constraints:
#
# n == nums.length
# m == l.length
# m == r.length
# 2 <= n <= 500
# 1 <= m <= 500
# 0 <= l[i] < r[i] < n
# -105 <= nums[i] <= 105
# Sorting
# Complexity
# Time complexity: O(N**2 * log(N))
# Space complexity: O(N)
# Code
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output: list[bool] = []
        for idx in range(len(l)):
            d: int = None
            invalid: bool = False
            inner_range = sorted(nums[l[idx]:r[idx] + 1])
            for x, y in zip(inner_range, inner_range[1:]):
                if d is None:
                    d = y - x
                elif y - x != d:
                    invalid = True
                    output.append(False)
                    break
            if not invalid: output.append(True)
        return output

# Without sorting, by arithmetic properties
# Complexity
# Time complexity: O(N**2)
# Space complexity: O(N)
# Code
class Solution:
    def check(self, sequence: list[int]) -> bool:
        min_el: int = min(sequence)
        max_el: int = max(sequence)
        if (max_el - min_el) % (len(sequence) - 1) != 0: return False
        diff: int = (max_el - min_el) / (len(sequence) - 1)
        storage: set[int] = set(sequence)
        current_el: int = min_el + diff
        while current_el < max_el:
            if current_el not in storage: return False
            current_el += diff
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output: list[bool] = []
        for idx in range(len(l)):
            output.append(self.check(nums[l[idx]:r[idx] + 1]))
        return output