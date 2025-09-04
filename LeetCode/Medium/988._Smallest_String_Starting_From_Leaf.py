# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
#
# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
#
# As a reminder, any shorter prefix of a string is lexicographically smaller.
#
# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.
#
#
#
# Example 1:
#
#
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"
# Example 2:
#
#
# Input: root = [25,1,3,1,3,0,2]
# Output: "adz"
# Example 3:
#
#
# Input: root = [2,2,1,null,1,0,null,0]
# Output: "abc"
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 8500].
# 0 <= Node.val <= 25
# Solution
# Python O(N + DH) O(H) String Depth-First-Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output: str = ''
    def dfs(self, root: TreeNode, path: list[str]) -> None:
        path.append(chr(root.val + 97))
        if not root.left and not root.right:
            path.reverse()
            if not self.output or ''.join(path) < self.output: self.output = ''.join(path)
            path.reverse()
            path.pop()
            return
        if root.left: self.dfs(root.left, path)
        if root.right: self.dfs(root.right, path)
        path.pop()

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.output = ''
        path: list[str] = []
        self.dfs(root, path)
        return self.output

# C++ O(N + DH) O(H) String Tree Depth-First-Search
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
    void dfs(TreeNode *root, std::string &path, std::string &output) {
        path.push_back(static_cast<char>(root->val + 'a'));
        if (!root->left && !root->right) {
            std::reverse(path.begin(), path.end());
            if (output.empty() || path < output) output = std::string(path);
            std::reverse(path.begin(), path.end());
            path.pop_back();
            return;
        };
        if (root->left) dfs(root->left, path, output);
        if (root->right) dfs(root->right, path, output);
        path.pop_back();
    }

    string smallestFromLeaf(TreeNode* root) {
        std::string output = "", path = "";
        dfs(root, path, output);
        return output;
    }
};