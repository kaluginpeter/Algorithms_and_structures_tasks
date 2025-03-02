# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# Solution
# Python O(N) O(N) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent: dict[TreeNode, TreeNode] = dict()
        parent[root] = None
        depth: dict[TreeNode, int] = dict()
        cur_depth: int = -1
        cur_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        while cur_nodes:
            cur_depth += 1
            for node in cur_nodes:
                depth[node] = cur_depth
                if node.left:
                    parent[node.left] = node
                    next_nodes.append(node.left)
                if node.right:
                    parent[node.right] = node
                    next_nodes.append(node.right)
            cur_nodes = next_nodes
            next_nodes = []
        while depth[q] > depth[p]: q = parent[q]
        while depth[p] > depth[q]: p = parent[p]
        while p != q:
            p = parent[p]
            q = parent[q]
        return p

# C++ O(N) O(N) Breadth-First-Search
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        unordered_map<TreeNode*, TreeNode*> parent;
        unordered_map<TreeNode*, int> depth;
        int curDepth = -1;
        parent[root] = nullptr;
        vector<TreeNode*> curNodes;
        vector<TreeNode*> nextNodes;
        curNodes.push_back(root);
        while (!curNodes.empty()) {
            ++curDepth;
            for (TreeNode* node : curNodes) {
                depth[node] = curDepth;
                if (node->left) {
                    parent[node->left] = node;
                    nextNodes.push_back(node->left);
                }
                if (node->right) {
                    parent[node->right] = node;
                    nextNodes.push_back(node->right);
                }
            }
            curNodes = nextNodes;
            nextNodes.clear();
        }
        while (depth[q] > depth[p]) q = parent[q];
        while (depth[p] > depth[q]) p = parent[p];
        while (p != q) {
            q = parent[q];
            p = parent[p];
        }
        return q;
    }
};