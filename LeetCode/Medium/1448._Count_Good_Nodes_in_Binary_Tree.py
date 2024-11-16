# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
#
#
#
# Example 1:
#
#
#
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:
#
#
#
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:
#
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
#
#
# Constraints:
#
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].
# Solution
# C++ O(N) O(N) Depth-First-Search
class Solution {
public:
    int good_nodes;
    void dfs(TreeNode* root, int ancestorValue) {
        if (root->val >= ancestorValue) {
            ++good_nodes;
        }
        if (root->left) {
            dfs(root->left, std::max(root->val, ancestorValue));
        }
        if (root->right) {
            dfs(root->right, std::max(root->val, ancestorValue));
        }
    };

    int goodNodes(TreeNode* root) {
        good_nodes = 0;
        dfs(root, root->val);
        return good_nodes;
    }
};
# Python O(N) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good_nodes: int
    def dfs(self, root: TreeNode, ancestor_value: int) -> None:
        if root.val >= ancestor_value:
            self.good_nodes += 1
        if root.left:
            self.dfs(root.left, max(root.val, ancestor_value))
        if root.right:
            self.dfs(root.right, max(root.val, ancestor_value))

    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        self.dfs(root, root.val)
        return self.good_nodes

# Python O(N) O(h) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes: int = 0
        cur_nodes: list[tuple[TreeNode, int]] = [(root, root.val)]
        next_nodes: list[tuple[TreeNode, int]] = []
        while cur_nodes:
            for node, ancestor_value in cur_nodes:
                if node.val >= ancestor_value:
                    good_nodes += 1
                if node.left:
                    next_nodes.append((node.left, max(node.val, ancestor_value)))
                if node.right:
                    next_nodes.append((node.right, max(node.val, ancestor_value)))
            cur_nodes = next_nodes
            next_nodes = []
        return good_nodes

# C++ O(N) O(h) Breadth-First-Search
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
    int goodNodes(TreeNode* root) {
        int good_nodes = 0;
        std::vector<std::pair<TreeNode*, int>> curNodes = {{root, root->val}};
        std::vector<std::pair<TreeNode*, int>> nextNodes;
        while (curNodes.size()) {
            for (std::pair<TreeNode*, int>& p : curNodes) {
                TreeNode* node = p.first;
                int ancestorValue = p.second;
                if (ancestorValue <= node->val) {
                    ++good_nodes;
                }
                if (node->left) {
                    nextNodes.push_back({node->left, std::max(ancestorValue, node->val)});
                }
                if (node->right) {
                    nextNodes.push_back({node->right, std::max(ancestorValue, node->val)});
                }
            }
            curNodes = nextNodes;
            nextNodes.clear();
        }
        return good_nodes;
    }
};