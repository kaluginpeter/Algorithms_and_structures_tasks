# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
#
# If there exist multiple answers, you can return any of them.
#
#
#
# Example 1:
#
#
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# Example 2:
#
# Input: preorder = [1], postorder = [1]
# Output: [1]
#
#
# Constraints:
#
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
# Solution
# Python O(N) O(H) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        levels: list[TreeNode] = []
        pre_idx: int = 0
        n: int = len(preorder)
        post_idx: int = 0
        m: int = len(postorder)
        depth: int = 0
        while pre_idx < n:
            cur_node_val: int = -1
            while pre_idx < n and cur_node_val != postorder[post_idx]:
                child: TreeNode = TreeNode(preorder[pre_idx])
                if depth == len(levels): levels.append(child)
                else: levels[depth] = child
                if depth:
                    parent: TreeNode = levels[depth - 1]
                    if not parent.left: parent.left = child
                    else: parent.right = child
                cur_node_val = child.val
                depth += 1
                pre_idx += 1
            while post_idx < m and levels[depth - 1].val == postorder[post_idx]:
                depth -= 1
                post_idx += 1

        return levels[0]

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
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        vector<TreeNode*> levels;
        int postIdx = 0, m = postorder.size();
        int preIdx = 0, n = preorder.size();;
        int depth = 0;
        while (preIdx < n) {
            int curNodeVal = -1;
            while (preIdx < n && curNodeVal != postorder[postIdx]) {
                TreeNode* child = new TreeNode(preorder[preIdx]);
                if (depth == levels.size()) levels.push_back(child);
                else levels[depth] = child;
                if (depth) {
                    TreeNode* parent = levels[depth - 1];
                    if (!parent->left) parent->left = child;
                    else parent->right = child;
                }
                curNodeVal = child->val;
                ++depth;
                ++preIdx;
            }
            while (postIdx < m && levels[depth - 1]->val == postorder[postIdx]) {
                --depth;
                ++postIdx;
            }
        }
        return levels[0];
    }
};