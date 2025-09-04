# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:
#
# Input: root = [1]
# Output: ["1"]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
#
# Solution
# Python O(N) O(H) Tree Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, path: list[str], output: list[str]) -> None:
        path.append(str(root.val))
        if not root.left and not root.right:
            output.append('->'.join(path))
            path.pop()
            return
        if root.left: self.dfs(root.left, path, output)
        if root.right: self.dfs(root.right, path, output)
        path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output: list[str] = []
        path: list[str] = []
        self.dfs(root, path, output)
        return output

# C++ O(N) O(H) Tree Depth-Frist-Search
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
    void dfs(TreeNode *root, std::string &path, std::vector<std::string> &output) {
        std::string value = std::to_string(root->val);
        path += value;
        if (!root->left && !root->right) {
            output.push_back(std::string(path.begin(), path.end()));
            for (size_t i = 0; i < value.size(); ++i) path.pop_back();
            return;
        }
        path += "->";
        if (root->left) dfs(root->left, path, output);
        if (root->right) dfs(root->right, path, output);
        for (size_t i = 0; i < value.size() + 2; ++i) path.pop_back();
        return;
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        std::vector<std::string> output;
        std::string path = "";
        dfs(root, path, output);
        return output;
    }
};