# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:
#
# Input: root = [1,2]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# Solution
# Python O(N) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter: int = 0

    def dfs_traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_part_depth: int = self.dfs_traverse(root.left)
        right_part_depth: int = self.dfs_traverse(root.right)
        self.diameter = max(self.diameter, left_part_depth + right_part_depth)
        return max(left_part_depth, right_part_depth) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs_traverse(root)
        return self.diameter

# C++ O(N) O(N) Depth-First-Search
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
    int diameter;
    int dfsTraversal(TreeNode* root) {
        if (!root) {
            return 0;
        }
        int depthLeftPart = dfsTraversal(root->left);
        int depthRightPart = dfsTraversal(root->right);
        diameter = std::max(diameter, depthLeftPart + depthRightPart);
        return std::max(depthLeftPart, depthRightPart) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        diameter = 0;
        dfsTraversal(root);
        return diameter;
    }
};