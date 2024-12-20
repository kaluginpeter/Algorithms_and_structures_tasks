# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
#
# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
#
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
#
# The level of a node is the number of edges along the path between it and the root node.
#
#
#
# Example 1:
#
#
# Input: root = [2,3,5,8,13,21,34]
# Output: [2,5,3,8,13,21,34]
# Explanation:
# The tree has only one odd level.
# The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
# Example 2:
#
#
# Input: root = [7,13,11]
# Output: [7,11,13]
# Explanation:
# The nodes at level 1 are 13, 11, which are reversed and become 11, 13.
# Example 3:
#
# Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
# Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
# Explanation:
# The odd levels have non-zero values.
# The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
# The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 214].
# 0 <= Node.val <= 105
# root is a perfect binary tree.
# Solution
# Python O(N) O(h) DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, x: TreeNode, y: TreeNode, level: int = 0) -> None:
        if not x:
            return
        if level & 1:
            x.val, y.val = y.val, x.val
        self.dfs(x.left, y.right, level + 1)
        if level:
            self.dfs(x.right, y.left, level + 1)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root, root)
        return root

# C++ O(N) O(h) DFS
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
    void dfs(TreeNode* x, TreeNode* y, int level) {
        if (!x) {
            return;
        }
        if (level % 2 != 0) {
            int tmp = y->val;
            y->val = x->val;
            x->val = tmp;
        }
        dfs(x->left, y->right, level + 1);
        if (level) {
            dfs(x->right, y->left, level + 1);
        }
    }
    TreeNode* reverseOddLevels(TreeNode* root) {
        dfs(root, root, 0);
        return root;
    }
};

# Python BFS O(N) O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root: TreeNode) -> None:
        cur_nodes: list[TreeNode] = []
        if root:
            cur_nodes.append(root)
        next_nodes: list[TreeNode] = []
        level: int = 0
        while cur_nodes:
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            level += 1
            cur_nodes = next_nodes
            next_nodes = []
            if level & 1:
                left: int = 0
                right: int = len(cur_nodes) - 1
                while left < right:
                    cur_nodes[left].val, cur_nodes[right].val = cur_nodes[right].val, cur_nodes[left].val
                    left += 1
                    right -= 1

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.bfs(root)
        return root

# C++ O(N) O(h) BFS
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
    TreeNode* reverseOddLevels(TreeNode* root) {
        std::vector<TreeNode*> curNodes;
        std::vector<TreeNode*> nextNodes;
        if (root) {
            curNodes.push_back(root);
        }
        int level = 0;
        while (curNodes.size()) {
            for (TreeNode* node : curNodes) {
                if (node->left) {
                    nextNodes.push_back(node->left);
                    nextNodes.push_back(node->right);
                }
            }
            curNodes = nextNodes;
            nextNodes = {};
            ++level;
            if (level % 2 != 0) {
                int left = 0;
                int right = curNodes.size() - 1;
                while (left < right) {
                    int tmp = curNodes[right]->val;
                    curNodes[right]->val = curNodes[left]->val;
                    curNodes[left]->val = tmp;
                    ++left;
                    --right;
                }
            }
        }
        return root;
    }
};