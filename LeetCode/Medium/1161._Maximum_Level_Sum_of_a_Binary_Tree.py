# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
#
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
#
#
#
# Example 1:
#
#
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:
#
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
#
# Solution
# Python O(N) O(N) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        cur_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        output: int = 0
        bound: int = float('-inf')
        depth: int = 0
        while cur_nodes:
            depth += 1
            cur_level: int = 0
            for node in cur_nodes:
                cur_level += node.val
                if node.left: next_nodes.append(node.left)
                if node.right: next_nodes.append(node.right)
            if cur_level > bound:
                bound = cur_level
                output = depth
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
    int maxLevelSum(TreeNode* root) {
        std::vector<TreeNode*> curNodes = {root}, nextNodes;
        int output = 0, bound = INT32_MIN, depth = 0;
        while (!curNodes.empty()) {
            ++depth;
            int curLevel = 0;
            for (TreeNode* node : curNodes) {
                curLevel += node->val;
                if (node->left) nextNodes.push_back(node->left);
                if (node->right) nextNodes.push_back(node->right);
            }
            if (curLevel > bound) {
                bound = curLevel;
                output = depth;
            }
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return output;
    }
};