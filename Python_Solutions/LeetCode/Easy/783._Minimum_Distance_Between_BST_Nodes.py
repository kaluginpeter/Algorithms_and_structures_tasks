# Given the root of a Binary Search Tree (BST),
# return the minimum difference between the values of any two different nodes in the tree.
#
# Example 1:
#
# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
# Constraints:
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 105
# Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Solution
class Solution(object):
    def minDiffInBST(self, root):
        tmp = []
        if root.left:
            curr = root.left
            while curr.right:
                curr = curr.right
            tmp.append(root.val - curr.val)
            if root.left.left or root.left.right:
                tmp.append(self.minDiffInBST(root.left))
        if root.right:
            curr = root.right
            while curr.left:
                curr = curr.left
            tmp.append(curr.val - root.val)
            if root.right.left or root.right.right:
                tmp.append(self.minDiffInBST(root.right))
        return min(tmp)