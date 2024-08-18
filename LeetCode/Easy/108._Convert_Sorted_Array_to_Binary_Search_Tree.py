# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced
#  binary search tree.
#
#
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.
# Solution Binary Search Tree Rercursion O(N) O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, arr: list[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right: return
        middle: int = (right + left) >> 1
        left_subtree = self.construct(arr, left, middle - 1)
        right_subtree = self.construct(arr, middle + 1, right)
        return TreeNode(arr[middle], left_subtree, right_subtree)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.construct(nums, 0, len(nums) - 1)