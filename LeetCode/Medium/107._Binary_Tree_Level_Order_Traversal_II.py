# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# Solution
# Python O(N) O(N + H) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, depth: int, output: list[list[int]]) -> None:
        if not root: return
        while depth >= len(output): output.append([])
        output[depth].append(root.val)
        if root.left: self.dfs(root.left, depth + 1, output)
        if root.right: self.dfs(root.right, depth + 1, output)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        output: list[list[int]] = []
        self.dfs(root, 0, output)
        output.reverse()
        return output

# C++ O(N) O(N + H) Depth-First-Search
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
    void dfs(TreeNode* root, size_t depth, std::vector<std::vector<int>> &output) {
        if (!root) return;
        while (depth >= output.size()) output.push_back(std::vector<int>());
        output[depth].push_back(root->val);
        if (root->left) dfs(root->left, depth + 1, output);
        if (root->right) dfs(root->right, depth + 1, output);
    }

    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        std::vector<std::vector<int>> output;
        dfs(root, 0, output);
        std::reverse(output.begin(), output.end());
        return output;
    }
};