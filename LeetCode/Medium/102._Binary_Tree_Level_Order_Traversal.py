# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
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
# C++ O(N) O(N) Breadth-First-Search
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> output;
        std::vector<TreeNode*> curNodes;
        if (root) {
            curNodes.push_back(root);
        }
        std::vector<TreeNode*> nextNodes;
        while (curNodes.size()) {
            std::vector<int> levelValues;
            for (TreeNode* node : curNodes) {
                if (node->left) {
                    nextNodes.push_back(node->left);
                }
                if (node->right) {
                    nextNodes.push_back(node->right);
                }
                levelValues.push_back(node->val);
            }
            if (levelValues.size()) {
                output.push_back(levelValues);
            }
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return output;
    }
};
# Python O(N) O(N) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output: list[list[int]] = []
        cur_nodes: list[TreeNode] = []
        if root:
            cur_nodes.append(root)
        next_nodes: list[TreeNode] = []
        while cur_nodes:
            level_values: list[int] = []
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
                level_values.append(node.val)
            if level_values:
                output.append(level_values)
            cur_nodes = next_nodes
            next_nodes = []
        return output