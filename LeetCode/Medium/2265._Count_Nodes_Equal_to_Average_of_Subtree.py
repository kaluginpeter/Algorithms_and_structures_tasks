# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
#
# Note:
#
# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.
#
#
# Example 1:
#
#
# Input: root = [4,8,5,0,1,null,6]
# Output: 5
# Explanation:
# For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
# For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
# For the node with value 0: The average of its subtree is 0 / 1 = 0.
# For the node with value 1: The average of its subtree is 1 / 1 = 1.
# For the node with value 6: The average of its subtree is 6 / 1 = 6.
# Example 2:
#
#
# Input: root = [1]
# Output: 1
# Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000
# Solution DFS O(N) O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    correct_nodes: int = 0

    def dfs(self, root):
        if root is None: return 0, 0
        left_nodes, left_sum_nodes = self.dfs(root.left)
        right_nodes, right_sum_nodes = self.dfs(root.right)
        current_nodes_count: int = 1 + left_nodes + right_nodes
        current_sum_nodes: int = root.val + left_sum_nodes + right_sum_nodes
        average: int = current_sum_nodes // current_nodes_count
        if root.val == average: self.correct_nodes += 1
        return current_nodes_count, current_sum_nodes

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.correct_nodes



# Go O(N) O(H) DepthFirstSearch
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func dfs(root *TreeNode, output *int) (int, int) {
    if root == nil {
        return 0, 0
    }
    var leftN, leftSum int = dfs(root.Left, output)
    var rightN, rightSum int = dfs(root.Right, output)
    var n int = leftN + rightN + 1
    var treeSum int = root.Val + leftSum + rightSum
    if treeSum / n == root.Val {
        (*output)++
    }
    return n, treeSum
}
func averageOfSubtree(root *TreeNode) int {
    var output int = 0
    dfs(root, &output)
    return output
}

# C++ O(N) O(H) DepthFirstSearch
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
    std::pair<size_t, size_t> dfs(TreeNode* root, size_t& output) {
        if (!root) return {0, 0};
        auto [leftSum, leftN] = dfs(root->left, output);
        auto [rightSum, rightN] = dfs(root->right, output);
        size_t totalSum = leftSum + rightSum + root->val;
        size_t n = leftN + rightN + 1;
        if (totalSum / n == root->val) ++output;
        return {totalSum, n};
    }
    int averageOfSubtree(TreeNode* root) {
        size_t output = 0;
        dfs(root, output);
        return output;
    }
};