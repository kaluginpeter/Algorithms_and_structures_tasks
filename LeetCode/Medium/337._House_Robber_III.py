# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
#
# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
#
#
#
# Example 1:
#
#
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#
#
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 104
# Solution
# Python O(N) O(H) DynamicProgramming Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode) -> list[int]:
        if not root: return [0, 0]
        left: list[int] = self.dfs(root.left)
        right: list[int] =  self.dfs(root.right)
        take: int = left[1] + right[1] + root.val
        not_take: int = max(left) + max(right)
        return [take, not_take]

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))

# C++ O(N) O(H) DynamicProgramming Depth-First-Search
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
    std::vector<int> dfs(TreeNode* root) {
        if (!root) return std::vector<int>(2, 0);
        std::vector<int> left = dfs(root->left);
        std::vector<int> right = dfs(root->right);
        int take = root->val + left[1] + right[1];
        int notTake = *std::max_element(left.begin(), left.end()) + *std::max_element(right.begin(), right.end());
        return std::vector<int>({take, notTake});
    }
    int rob(TreeNode* root) {
        std::vector<int> output = dfs(root);
        return *std::max_element(output.begin(), output.end());
    }
};