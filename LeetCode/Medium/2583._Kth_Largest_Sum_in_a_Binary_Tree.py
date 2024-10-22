# You are given the root of a binary tree and a positive integer k.
#
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
#
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
#
# Note that two nodes are on the same level if they have the same distance from the root.
#
#
#
# Example 1:
#
#
# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
# Explanation: The level sums are the following:
# - Level 1: 5.
# - Level 2: 8 + 9 = 17.
# - Level 3: 2 + 1 + 3 + 7 = 13.
# - Level 4: 4 + 6 = 10.
# The 2nd largest level sum is 13.
# Example 2:
#
#
# Input: root = [1,2,null,3], k = 1
# Output: 3
# Explanation: The largest level sum is 3.
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 2 <= n <= 105
# 1 <= Node.val <= 106
# 1 <= k <= n
# Solution
# C++ O(NlogN) O(N) Breadth-First-Search Sorting
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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        std::vector<long long> levelSums;
        std::vector<TreeNode*> currentNodes = {root};
        std::vector<TreeNode*> nextNodes;
        while (currentNodes.size()) {
            long long levelSum = 0;
            for (TreeNode* node : currentNodes) {
                if (!node) {
                    continue;
                }
                if (node->left) {
                    nextNodes.push_back(node->left);
                }
                if (node->right) {
                    nextNodes.push_back(node->right);
                }
                levelSum += node->val;
            }
            levelSums.push_back(levelSum);
            currentNodes = nextNodes;
            nextNodes.clear();
        }
        if (levelSums.size() < k) {
            return -1;
        }
        std::sort(levelSums.begin(), levelSums.end());
        return levelSums[levelSums.size() - k];
    }
};

# Python O(NlogN) O(N) Breadth-First-Search Sorting
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums: list[int] = []
        current_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        while current_nodes:
            level_sum: int = 0
            for node in current_nodes:
                if not node:
                    continue
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
                level_sum += node.val
            level_sums.append(level_sum)
            current_nodes = next_nodes
            next_nodes = []
        if len(level_sums) < k:
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k - 1]