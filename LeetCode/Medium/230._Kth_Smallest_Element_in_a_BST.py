# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
# Solution
# Follow up
# How to optimize?
# Answer
# Since naive solution uses the entire traversing through the tree,
# complexity is simple O(N), but if we add number of childrens for each parent at BST structure,
# we can decrease complexity to O(H),
# where H is the length of tree, simply "cut of" brach by brach until we find appropriate node
# Python O(N) O(H) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    position: int = 0
    def dfs(self, root: TreeNode, k: int) -> TreeNode:
        if not root: return root
        left: TreeNode = self.dfs(root.left, k)
        if left: return left
        self.position += 1
        if self.position == k: return root
        return self.dfs(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.position = 0
        return self.dfs(root, k).val

# C++ O(N) O(H) Depth-First-Search
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
    TreeNode* dfs(TreeNode* root, int& position, const int &k) {
        if (!root) return root;
        TreeNode* left = dfs(root->left, position, k);
        if (left) return left;
        ++position;
        if (position == k) return root;
        return dfs(root->right, position, k);
    }
    int kthSmallest(TreeNode* root, int k) {
        int position = 0;
        return dfs(root, position, k)->val;
    }
};