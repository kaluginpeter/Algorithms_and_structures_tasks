# Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
#
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
# Return the root of the modified tree.
#
# Note that the depth of a node is the number of edges in the path from the root node to it.
#
#
#
# Example 1:
#
#
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
# Example 2:
#
#
# Input: root = [3,1,2]
# Output: [0,0,0]
# Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 104
# Solution
# Python O(N) O(N) HashMap Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_nodes: list[tuple[int, node]] = [(0, root)]
        next_nodes: list[tuple[int, node]] = []
        while current_nodes:
            hashmap: dict[int, int] = dict()
            level_sum: int = 0
            for idx in range(len(current_nodes)):
                parent, node = current_nodes[idx]
                if not node:
                    continue
                if node.left:
                    next_nodes.append((idx, node.left))
                    hashmap[idx] = hashmap.get(idx, 0) + node.left.val
                    level_sum += node.left.val
                if node.right:
                    next_nodes.append((idx, node.right))
                    hashmap[idx] = hashmap.get(idx, 0) + node.right.val
                    level_sum += node.right.val
            for pair in next_nodes:
                parent, node = pair
                node.val = level_sum - hashmap[parent]
            current_nodes = next_nodes
            next_nodes = []
        if root:
            root.val = 0
        return root

# C++ O(N) O(N) HashMap Breadth-First-Search
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
    TreeNode* replaceValueInTree(TreeNode* root) {
        std::vector<std::pair<int, TreeNode*>> current_nodes = {{0, root}};
        std::vector<std::pair<int, TreeNode*>> next_nodes;
        while (current_nodes.size()) {
            int levelSum = 0;
            std::unordered_map<int, int> hashmap;
            for (int index = 0; index < current_nodes.size(); ++index) {
                int parent = current_nodes[index].first;
                TreeNode* node = current_nodes[index].second;
                if (!node) {
                    continue;
                }
                if (node->left) {
                    levelSum += node->left->val;
                    next_nodes.push_back({index, node->left});
                    hashmap[index] += node->left->val;
                }
                if (node->right) {
                    levelSum += node->right->val;
                    next_nodes.push_back({index, node->right});
                    hashmap[index] += node->right->val;
                }
            }
            for (std::pair<int, TreeNode*>& pair : next_nodes) {
                int parent = pair.first;
                TreeNode* node = pair.second;
                node->val = levelSum - hashmap[parent];
            }
            current_nodes = next_nodes;
            next_nodes.clear();
        }
        if (root) {
            root->val = 0;
        }
        return root;
    }
};