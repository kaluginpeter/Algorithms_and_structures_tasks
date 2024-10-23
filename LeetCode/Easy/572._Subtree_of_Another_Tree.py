# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104
# General idea
# The main concept is that we need to ensure that both trees are the same.
# Similar problem is 100. Same Tree and we need just use solution from that problem to solve this problem.
# Make a DFS for a root and for avoiding redundancy computations
# we start SameTree function only when our root.value match with subRoot.value.
# If any of the calls SameTree fuction ends with a True, so we need to return True.
# For this Statement use OR operator between recursive calls

# C++ O(NM) O(N) Depth-First-Search
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
    bool checkMatch(TreeNode* x, TreeNode* y) {
        if (!x || !y) {
            return !x && !y;
        }
        if (x->val != y->val) {
            return false;
        }
        return checkMatch(x->left, y->left) && checkMatch(x->right, y->right);
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) {
            return false;
        }
        bool isEqual = false;
        if (root->val == subRoot->val) {
            isEqual = checkMatch(root, subRoot);
        }
        return isEqual || isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};

# Python O(NM) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_match(self, x: Optional[TreeNode], y: Optional[TreeNode]) -> bool:
        if not x or not y:
            return not x and not y
        if x.val != y.val:
            return False
        return self.check_match(x.left, y.left) and self.check_match(x.right, y.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        is_equal: bool = False
        if root.val == subRoot.val:
            is_equal = self.check_match(root, subRoot)
        return is_equal or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)