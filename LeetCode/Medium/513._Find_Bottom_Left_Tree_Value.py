# Given the root of a binary tree, return the leftmost value in the last row of the tree.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: 1
# Example 2:
#
#
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
# Solution
# Python O(N) O(N) Breadth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        leftmost_value: int = root.val
        current_nodes: list[Optional[TreeNode]] = [root]
        next_nodes: list[Optional[TreeNode]] = []
        while current_nodes:
            for node in current_nodes:
                if not node:
                    continue
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:
                leftmost_value = next_nodes[0].val
            current_nodes = next_nodes
            next_nodes = []
        return leftmost_value

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
    int findBottomLeftValue(TreeNode* root) {
        int leftmost_value_ = root->val;
        std::vector<TreeNode*> current_nodes = {root};
        std::vector<TreeNode*> next_nodes;
        while (current_nodes.size()) {
            for (TreeNode* node : current_nodes) {
                if (!node) {
                    continue;
                }
                if (node->left) {
                    next_nodes.push_back(node->left);
                }
                if (node->right) {
                    next_nodes.push_back(node->right);
                }
            }
            if (!next_nodes.size()) {
                break;
            }
            leftmost_value_ = next_nodes[0]->val;
            current_nodes = next_nodes;
            next_nodes.clear();
        }
        return leftmost_value_;
    }
};

# Python O(N) O(N) Depth-First-Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.max_depth: int = -1
        self.leftmost_value: int = -1

    def traverse(self, root: Optional[TreeNode], depth: int) -> None:
        if not root:
            return
        if depth > self.max_depth:
            self.max_depth = depth
            self.leftmost_value = root.val
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -1
        self.leftmost_value = -1
        self.traverse(root, 0)
        return self.leftmost_value

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
    void traverse(TreeNode* root, int depth) {
        if (!root) {
            return;
        }
        if (depth > height_of_leftmost_value_) {
            height_of_leftmost_value_ = depth;
            leftmost_value_ = root->val;
        }
        traverse(root->left, depth + 1);
        traverse(root->right, depth + 1);
    }
    int findBottomLeftValue(TreeNode* root) {
        traverse(root, 0);
        return leftmost_value_;
    }
private:
    int height_of_leftmost_value_ = -1;
    int leftmost_value_ = -1;
};