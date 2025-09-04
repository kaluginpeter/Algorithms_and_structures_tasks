# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:
#
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
# Solution
# Python O(N) O(H) Tree Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, targetSum: int, path: list[int], output: list[list[int]]) -> None:
        targetSum -= root.val
        path.append(root.val)
        if not targetSum and not root.left and not root.right:
            output.append(path.copy())
            path.pop()
            return
        if root.left: self.dfs(root.left, targetSum, path, output)
        if root.right: self.dfs(root.right, targetSum, path, output)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output: list[list[int]] = []
        path: list[int] = []
        if root: self.dfs(root, targetSum, path, output)
        return output

# C++ O(N) O(H) Tree Depth-First-Search
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
    void dfs(TreeNode *root, int targetSum, std::vector<int> &path, std::vector<std::vector<int>> &output) {
        targetSum -= root->val;
        path.push_back(root->val);
        if (!targetSum && !root->left && !root->right) {
            output.push_back(std::vector<int>(path.begin(), path.end()));
            path.pop_back();
            return;
        }
        if (root->left) dfs(root->left, targetSum, path, output);
        if (root->right) dfs(root->right, targetSum, path, output);
        path.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        std::vector<std::vector<int>> output;
        std::vector<int> path;
        if (root) dfs(root, targetSum, path, output);
        return output;
    }
};