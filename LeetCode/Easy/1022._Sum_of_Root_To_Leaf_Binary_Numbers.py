# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
#
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
#
# The test cases are generated so that the answer fits in a 32-bits integer.
#
#
#
# Example 1:
#
#
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:
#
# Input: root = [0]
# Output: 0
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.
#
# Solution
# Python O(N) O(h) DepthFirstSearch
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output: int = 0
    def dfs(self, root: TreeNode, acc: int) -> None:
        acc <<= 1
        if root.val: acc += 1
        if not root.left and not root.right:
            self.output += acc
            return
        if root.left: self.dfs(root.left, acc)
        if root.right: self.dfs(root.right, acc)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        self.dfs(root, 0)
        return self.output

# C++ O(N) O(h) DepthFirstSearch
/**
 * Definition for a binary tree nodes.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* root, int& output, int acc) {
        acc <<= 1;
        if (root->val) ++acc;
        if (!root->left && !root->right) {
            output += acc;
            return;
        }
        if (root->left) dfs(root->left, output, acc);
        if (root->right) dfs(root->right, output, acc);
    }
    int sumRootToLeaf(TreeNode* root) {
        int output = 0;
        dfs(root, output, 0);
        return output;
    }
};