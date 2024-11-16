# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:
#
# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output: list[int] = []
        cur_nodes: list[TreeNode] = []
        if root:
            cur_nodes.append(root)
        next_nodes: list[TreeNode] = []
        while cur_nodes:
            rightmost_node: Optional[TreeNode] = None
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
                rightmost_node = node
            output.append(rightmost_node.val)
            cur_nodes = next_nodes
            next_nodes = []
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
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> output;
        std::vector<TreeNode*> curNodes;
        if (root) {
            curNodes.push_back(root);
        }
        std::vector<TreeNode*> nextNodes;
        while (curNodes.size()) {
            TreeNode* rightmostNode = nullptr;
            for (TreeNode* node : curNodes) {
                if (node->left) {
                    nextNodes.push_back(node->left);
                }
                if (node->right) {
                    nextNodes.push_back(node->right);
                }
                rightmostNode = node;
            }
            output.push_back(rightmostNode->val);
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return output;
    }
};