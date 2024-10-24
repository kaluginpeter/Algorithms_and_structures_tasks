# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
#
# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
#
#
#
# Example 1:
#
# Flipped Trees Diagram
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
# Example 2:
#
# Input: root1 = [], root2 = []
# Output: true
# Example 3:
#
# Input: root1 = [], root2 = [1]
# Output: false
#
#
# Constraints:
#
# The number of nodes in each tree is in the range [0, 100].
# Each tree will have unique node values in the range [0, 99].
# Solution
# General Idea
# By the Liskov Sustitution principle if node aren't equal only other node with same parent possible can match with node from other tree. ex
#
# x=          y=
#     1      |       1
# 2       3  |  3         2
# to make trees equal we only have flip nodes
# with same parent like in that case: x.left with x.right

# C++ O(N) O(N) Depth-First-Search
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
    bool checkEqual(TreeNode* x, TreeNode* y) {
        if (x && y) {
            return x->val == y->val;
        } else {
            return !x && !y;
        }
    }

    void flipTree(TreeNode* root) {
        TreeNode* rightPart = root->right;
        root->right = root->left;
        root->left = rightPart;
    }

    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if (!root1 || !root2) {
            return !root1 && !root2;
        }
        if (!checkEqual(root1, root2)) {
            return false;
        }
        if (!checkEqual(root1->left, root2->left)) {
            flipTree(root1);
            if (!checkEqual(root1->left, root2->left)) {
                return false;
            }
            if (!checkEqual(root1->right, root2->right)) {
            return false;
        } else {
            if (!checkEqual(root1->right, root2->right)) {
                flipTree(root1);
            }
            if (!checkEqual(root1->right, root2->right)) {
                return false;
            }
            if (!checkEqual(root1->left, root2->left)) {
                return false;
            }
        }
        }

        bool leftPart = flipEquiv(root1->left, root2->left);
        bool rightPart = flipEquiv(root1->right, root2->right);
        return leftPart && rightPart;
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
    def check_equal(self, x: TreeNode, y: TreeNode) -> bool:
        if not x or not y:
            return not x and not y
        return x.val == y.val

    def flip_tree(self, root: TreeNode) -> None:
        root.left, root.right = root.right, root.left

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False
        if not self.check_equal(root1.left, root2.left):
            self.flip_tree(root1)
            if not self.check_equal(root1.left, root2.left):
                return False
            if not self.check_equal(root1.right, root2.right):
                return False
        else:
            if not self.check_equal(root1.right, root2.right):
                self.flip_tree(root1)
            if not self.check_equal(root1.right, root2.right):
                return False
            if not self.check_equal(root1.left, root2.left):
                return False
        left_part: bool = self.flipEquiv(root1.left, root2.left)
        right_part: bool = self.flipEquiv(root1.right, root2.right)
        return left_part and right_part