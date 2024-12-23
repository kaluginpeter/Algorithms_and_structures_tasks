# You are given the root of a binary tree with unique values.
#
# In one operation, you can choose any two nodes at the same level and swap their values.
#
# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.
#
# The level of a node is the number of edges along the path between it and the root node.
#
#
#
# Example 1:
#
#
# Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# Output: 3
# Explanation:
# - Swap 4 and 3. The 2nd level becomes [3,4].
# - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
# - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# Example 2:
#
#
# Input: root = [1,3,2,7,6,5,4]
# Output: 3
# Explanation:
# - Swap 3 and 2. The 2nd level becomes [2,3].
# - Swap 7 and 4. The 3rd level becomes [4,6,5,7].
# - Swap 6 and 5. The 3rd level becomes [4,5,6,7].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# Example 3:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 0
# Explanation: Each level is already sorted in increasing order so return 0.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 105
# All the values of the tree are unique.
# Solution
# Python O(h(NlogN)) O(N) BFS Sorting
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_swaps(self, nodes: list[TreeNode]) -> int:
        hashmap: dict[int, int] = dict()
        sorted_nodes: list[int] = []
        for idx in range(len(nodes)):
            hashmap[nodes[idx].val] = idx
            sorted_nodes.append(nodes[idx].val)
        sorted_nodes.sort()
        count: int = 0
        for idx in range(len(nodes)):
            if nodes[idx].val != sorted_nodes[idx]:
                count += 1
                valid_idx: int = hashmap[sorted_nodes[idx]]
                nodes[valid_idx].val = nodes[idx].val
                hashmap[nodes[idx].val] = valid_idx
        return count

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        cur_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        swaps: int = 0
        while cur_nodes:
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            swaps += self.get_swaps(next_nodes)
            cur_nodes = next_nodes
            next_nodes = []
        return swaps

# C++ O(h(NlogN)) O(N) BFS Sorting
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
    int getSwaps(std::vector<TreeNode*> nodes) {
        std::unordered_map<int, int> hashmap;
        std::vector<int> sortedNodes;
        for (int idx = 0; idx < nodes.size(); ++idx) {
            hashmap[nodes[idx]->val] = idx;
            sortedNodes.push_back(nodes[idx]->val);
        }
        std::sort(sortedNodes.begin(), sortedNodes.end());
        int count = 0;
        for (int idx = 0; idx < nodes.size(); ++idx) {
            if (sortedNodes[idx] != nodes[idx]->val) {
                ++count;
                int validIdx = hashmap[sortedNodes[idx]];
                nodes[validIdx]->val = nodes[idx]->val;
                hashmap[nodes[idx]->val] = validIdx;
            }
        }
        return count;
    }

    int minimumOperations(TreeNode* root) {
        std::vector<TreeNode*> curNodes = {root};
        std::vector<TreeNode*> nextNodes;
        int swaps = 0;
        while (curNodes.size()) {
            for (TreeNode* node : curNodes) {
                if (node->left) {
                    nextNodes.push_back(node->left);
                }
                if (node->right) {
                    nextNodes.push_back(node->right);
                }
            }
            swaps += getSwaps(nextNodes);
            curNodes = nextNodes;
            nextNodes = {};
        }
        return swaps;
    }
};