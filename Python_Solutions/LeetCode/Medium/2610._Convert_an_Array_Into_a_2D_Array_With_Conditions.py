# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
#
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
#
# Note that the 2D array can have a different number of elements on each row.
#
#
#
# Example 1:
#
# Input: nums = [1,3,4,1,2,3,1]
# Output: [[1,3,4,2],[1,3],[1]]
# Explanation: We can create a 2D array that contains the following rows:
# - 1,3,4,2
# - 1,3
# - 1
# All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: [[4,3,2,1]]
# Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= nums.length
# Solution 1 - HashTable O(N**2) O(N)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d: dict = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        ans: list = list()
        while d:
            top: list = []
            for i in d.copy():
                top.append(i)
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
            ans.append(top)
        return ans
# Solution 2 - Flag O(N * len(ans)), O(N)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans: list = [[]]
        for i in nums:
            flag: bool = False
            for l in ans:
                if i not in l:
                    l.append(i)
                    flag: bool = True
                    break
            if not flag:
                ans += [[i]]
        return  ans
# Solution 3 - HashTable O(N) O(N)
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        sq: list = [0] * (len(nums) + 1)
        ans: list = []
        for i in nums:
            if sq[i] >= len(ans):
                ans.append([])
            ans[sq[i]].append(i)
            sq[i] += 1
        return ans