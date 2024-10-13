# You are given the root of a binary tree and an integer k.
#
# Return an integer denoting the size of the kth largest perfect binary
# subtree
# , or -1 if it doesn't exist.
#
# A perfect binary tree is a tree where all leaves are on the same level, and every parent has two children.
#
#
#
# Example 1:
#
# Input: root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2
#
# Output: 3
#
# Explanation:
#
#
#
# The roots of the perfect binary subtrees are highlighted in black. Their sizes, in decreasing order are [3, 3, 1, 1, 1, 1, 1, 1].
# The 2nd largest size is 3.
#
# Example 2:
#
# Input: root = [1,2,3,4,5,6,7], k = 1
#
# Output: 7
#
# Explanation:
#
#
#
# The sizes of the perfect binary subtrees in decreasing order are [7, 3, 3, 1, 1, 1, 1]. The size of the largest perfect binary subtree is 7.
#
# Example 3:
#
# Input: root = [1,2,3,null,4], k = 3
#
# Output: -1
#
# Explanation:
#
#
#
# The sizes of the perfect binary subtrees in decreasing order are [1, 1]. There are fewer than 3 perfect binary subtrees.
#
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 2000].
# 1 <= Node.val <= 2000
# 1 <= k <= 1024
# Solution
# Python O(N) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], depth: int, trees: list[int]) -> int:
        if not root:
            return 0
        left_part = self.traverse(root.left, 1, trees)
        right_part = self.traverse(root.right, 1, trees)
        if left_part != right_part or min(left_part, right_part) == -1: return -1
        trees.append(left_part + right_part + 1)
        return right_part + left_part + 1

    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        trees = []
        self.traverse(root, 0, trees)
        trees.sort(reverse=True)
        return trees[k - 1] if k <= len(trees) else -1

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
    int traverse(TreeNode* root, int depth, std::vector<int>& roots) {
        if (!root) {
            return 0;
        }
        int left_part = traverse(root->left, 1, roots);
        int right_part = traverse(root->right, 1, roots);
        if (left_part != right_part || std::min(left_part, right_part) == -1) {
            return -1;
        }
        roots.push_back(left_part + right_part + 1);
        return left_part + right_part + 1;
    }

    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        std::vector<int> roots;
        traverse(root, 0, roots);
        std::sort(roots.begin(), roots.end(), std::greater<>());
        return (k > roots.size() ? -1 : roots[k - 1]);
    }
};