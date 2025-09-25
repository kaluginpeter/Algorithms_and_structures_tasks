# Given the root of a binary tree, return the sum of all left leaves.
#
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:
#
# Input: root = [1]
# Output: 0
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
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
    def dfs(self, root: TreeNode, direction: str) -> None:
        if not root: return
        elif not root.left and not root.right and direction == 'l': self.output += root.val
        if root.left: self.dfs(root.left, 'l')
        if root.right: self.dfs(root.right, 'r')

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        self.dfs(root, 'r')
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
    void dfs(TreeNode* root, int& output, char direction) {
        if (!root) return;
        else if (!root->left && !root->right) output += (direction == 'l' ? root->val : 0);
        if (root->left) dfs(root->left, output, 'l');
        if (root->right) dfs(root->right, output, 'r');
    }
    int sumOfLeftLeaves(TreeNode* root) {
        int output = 0;
        dfs(root, output, 'r');
        return output;
    }
};