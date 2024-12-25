# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
#
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:
#
# Input: root = [1,2,3]
# Output: [1,3]
#
#
# Constraints:
#
# The number of nodes in the tree will be in the range [0, 104].
# -231 <= Node.val <= 231 - 1
# Solution
# Python O(N) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], depth: int, output: list[int]) -> None:
        if not root: return
        if depth >= len(output):
            output.append(root.val)
        else:
            output[depth] = max(output[depth], root.val)
        self.dfs(root.left, depth + 1, output)
        self.dfs(root.right, depth + 1, output)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        output: list[int] = []
        self.dfs(root, 0, output)
        return output

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
    void dfs(TreeNode* root, int depth, std::vector<int>& output) {
        if (!root) {
            return;
        }
        if (depth >= output.size()) {
            output.push_back(root->val);
        } else {
            output[depth] = std::max(output[depth], root->val);
        }
        dfs(root->left, depth + 1, output);
        dfs(root->right, depth + 1, output);
    }
    vector<int> largestValues(TreeNode* root) {
        std::vector<int> output;
        int depth = 0;
        dfs(root, depth, output);
        return output;
    }
};

# Python O(N) O(N) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        output: list[int] = []
        cur_nodes: list[TreNode] = []
        if root:
            cur_nodes.append(root)
        next_nodes: list[TreeNode] = []
        while cur_nodes:
            cur_max: int = float('-inf')
            for node in cur_nodes:
                cur_max = max(cur_max, node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            output.append(cur_max)
            cur_nodes = next_nodes
            next_nodes = []
        return output

# C++ O(N) O(N) Breadth-First-Search
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
    vector<int> largestValues(TreeNode* root) {
        std::vector<int> output;
        std::vector<TreeNode*> curNodes;
        if (root) {
            curNodes.push_back(root);
        }
        std::vector<TreeNode*> nextNodes;
        while (curNodes.size()) {
            int curMax = INT32_MIN;
            for (TreeNode* node : curNodes) {
                curMax = std::max(curMax, node->val);
                if (node->left) {
                    nextNodes.push_back(node->left);
                }
                if (node->right) {
                    nextNodes.push_back(node->right);
                }
            }
            output.push_back(curMax);
            curNodes = nextNodes;
            nextNodes = {};
        }
        return output;
    }
};