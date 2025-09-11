# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Example 2:
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
# Solution
# Python O(N) O(N) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output: list[float] = []
        cur_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        while cur_nodes:
            cur_level_sum: float = 0
            level_size: int = len(cur_nodes)
            for node in cur_nodes:
                cur_level_sum += node.val
                if node.left: next_nodes.append(node.left)
                if node.right: next_nodes.append(node.right)
            output.append(cur_level_sum / level_size)
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
    vector<double> averageOfLevels(TreeNode* root) {
        std::vector<double> output;
        std::vector<TreeNode*> curNodes = {root}, nextNodes;
        while (!curNodes.empty()) {
            double curLevelSum = 0;
            size_t levelSize = curNodes.size();
            for (TreeNode *node : curNodes) {
                curLevelSum += node->val;
                if (node->left) nextNodes.push_back(node->left);
                if (node->right) nextNodes.push_back(node->right);
            }
            output.push_back(curLevelSum / levelSize);
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return output;
    }
};