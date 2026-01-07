# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
#
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
#
# Note that you need to maximize the answer before taking the mod and not after taking it.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:
#
#
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104
#
# Solution
# Python O(N) O(H) Depth-Frist-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
mod: int = 10 ** 9 + 7


class Solution:
    output: int = 0

    def get_sum(self, root: TreeNode) -> int:
        if not root: return 0
        return root.val + self.get_sum(root.left) + self.get_sum(root.right)

    def dfs(self, root: TreeNode, tree_sum: int) -> int:
        if not root: return 0
        cur_sum: int = root.val + self.dfs(root.left, tree_sum) + self.dfs(root.right, tree_sum)
        if cur_sum * (tree_sum - cur_sum) > self.output:
            self.output = cur_sum * (tree_sum - cur_sum)
        return cur_sum

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.output: int = 0
        tree_sum: int = self.get_sum(root)
        self.dfs(root, tree_sum)
        return self.output % mod

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
constexpr int mod = 1000000007;
class Solution {
public:
    void getSum(TreeNode* root, long long& treeSum) {
        if (!root) return;
        treeSum += root->val;
        getSum(root->left, treeSum);
        getSum(root->right, treeSum);
    }
    long long dfs(TreeNode* root, const long long& treeSum, long long& output) {
        if (!root) return 0;
        long long left = dfs(root->left, treeSum, output);
        long long right = dfs(root->right, treeSum, output);
        long long curSum = left + right + root->val;
        if (curSum * (treeSum - curSum) > output) output = curSum * (treeSum - curSum);
        return curSum;
    }
    int maxProduct(TreeNode* root) {
        long long output = 0, treeSum = 0;
        getSum(root, treeSum);
        dfs(root, treeSum, output);
        return output % mod;
    }
};