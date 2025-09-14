# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
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
# -100 <= Node.val <= 100
# Solution
# Python O(N) O(N) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output: list[list[int]] = []
        i: int = 0
        cur_nodes: list[int] = [root]
        next_nodes: list[int] = []
        while cur_nodes:
            level: list[int] = []
            for node in cur_nodes:
                if not node: continue
                level.append(node.val)
                if node.left: next_nodes.append(node.left)
                if node.right: next_nodes.append(node.right)
            if i & 1: level.reverse()
            if level: output.append(level)
            i += 1
            cur_nodes = next_nodes.copy()
            next_nodes.clear()
        return output

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        std::vector<std::vector<int>> output;
        std::vector<TreeNode*> curNodes = {root}, nextNodes = {};
        size_t i = 0;
        while (!curNodes.empty()) {
            std::vector<int> level;
            for (TreeNode* node : curNodes) {
                if (!node) continue;
                level.push_back(node->val);
                if (node->left) nextNodes.push_back(node->left);
                if (node->right) nextNodes.push_back(node->right);
            }
            if (i & 1) std::reverse(level.begin(), level.end());
            if (!level.empty()) output.push_back(level);
            ++i;
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return output;
    }
};