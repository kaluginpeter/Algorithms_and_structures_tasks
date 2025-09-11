# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
#
#
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.
# Solution
# Python O(N) O(H) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output: int = 0
    def dfs(self, root: TreeNode, cur_sum: int) -> None:
        cur_sum = cur_sum * 10 + root.val
        if not root.left and not root.right:
            self.output += cur_sum
            return
        if root.left: self.dfs(root.left, cur_sum)
        if root.right: self.dfs(root.right, cur_sum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        self.dfs(root, 0)
        return self.output

# C++ O(N) O(H) Depth-First-Search
/**
 * Definition for a binary tree node.
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
    void dfs(TreeNode* root, int curSum, int &output) {
        curSum = curSum * 10 + root->val;
        if (!root->left && !root->right) {
            output += curSum;
            return;
        }
        if (root->left) dfs(root->left, curSum, output);
        if (root->right) dfs(root->right, curSum, output);
    }

    int sumNumbers(TreeNode* root) {
        int output = 0;
        dfs(root, 0, output);
        return output;
    }
};