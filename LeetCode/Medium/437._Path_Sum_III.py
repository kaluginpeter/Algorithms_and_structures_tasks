# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
#
#
#
# Example 1:
#
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000
# Solution
# Python O(N) O(H) Tree Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output: int = 0
    def dfs(self, root: TreeNode, cur_sum: int, target_sum: int, hashmap: dict[int, int]) -> None:
        if not root: return
        cur_sum += root.val
        self.output += hashmap.get(cur_sum - target_sum, 0)
        hashmap[cur_sum] = hashmap.get(cur_sum, 0) + 1
        if root.left: self.dfs(root.left, cur_sum, target_sum, hashmap)
        if root.right: self.dfs(root.right, cur_sum, target_sum, hashmap)
        hashmap[cur_sum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.output = 0
        hashmap: dict[int, int] = dict()
        hashmap[0] = 1
        self.dfs(root, 0, targetSum, hashmap)
        return self.output

# C++ O(N) O(H) Tree Depth-First-Search
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
    void dfs(TreeNode *root, int targetSum, long long curSum, std::unordered_map<long long, int> &hashmap, int &output) {
        if (!root) return;
        curSum += root->val;
        output += hashmap[curSum - targetSum];
        ++hashmap[curSum];
        if (root->left) dfs(root->left, targetSum, curSum, hashmap, output);
        if (root->right) dfs(root->right, targetSum, curSum, hashmap, output);
        --hashmap[curSum];
    }

    int pathSum(TreeNode* root, int targetSum) {
        std::unordered_map<long long, int> hashmap;
        hashmap[0] = 1;
        int output = 0;
        dfs(root, targetSum, 0, hashmap, output);
        return output;
    }
};