# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:
#
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
# Solution
# C++ O(N) O(N) Least Common Path Depth-First-Search
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
    bool dfsTraverse(TreeNode* root, TreeNode* x, std::vector<TreeNode*>& path) {
        if (!root) {
            return false;
        }
        path.push_back(root);
        if (root->val == x->val) {
            return true;
        }
        bool leftPart = dfsTraverse(root->left, x, path);
        bool rightPart = dfsTraverse(root->right, x, path);
        if (!leftPart && !rightPart) {
            path.pop_back();
        }
        return leftPart || rightPart;

    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::vector<TreeNode*> pPath;
        dfsTraverse(root, p, pPath);
        std::vector<TreeNode*> qPath;
        dfsTraverse(root, q, qPath);
        int index = 0;
        while (index < std::min(pPath.size(), qPath.size()) && pPath[index]->val == qPath[index]->val) {
            ++index;
        }
        --index;
        return pPath[index];
    }
};

# Python O(N) O(N) Lowest Common Path Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_path(self, root: TreeNode, target: TreeNode, path: list[TreeNode]) -> bool:
        if not root:
            return False
        path.append(root)
        if root.val == target.val:
            return True
        left_part: bool = self.find_path(root.left, target, path)
        right_part: bool = self.find_path(root.right, target, path)
        if not left_part and not right_part:
            path.pop()
        return left_part or right_part

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path: list[TreeNode] = []
        self.find_path(root, p, p_path)
        q_path: list[TreeNode] = []
        self.find_path(root, q, q_path)
        idx: int = 0
        while idx < min(len(p_path), len(q_path)) and p_path[idx] == q_path[idx]:
            idx += 1
        idx -= 1
        return p_path[idx]


# C++ O(h) O(h) BST Least Common Path Depth-First-Search
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
        if (root->val > std::max(p->val, q->val)) {
            return lowestCommonAncestor(root->left, p, q);
        } else if (root->val < std::min(p->val, q->val)) {
            return lowestCommonAncestor(root->right, p, q);
        } else {
            return root;
        }
    }
};

# Python O(h) O(h) BST Least Common Path Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        return root