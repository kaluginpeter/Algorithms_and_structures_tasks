# Given the root of a binary tree, the depth of each node is the shortest distance to the root.
#
# Return the smallest subtree such that it contains all the deepest nodes in the original tree.
#
# A node is called the deepest if it has the largest depth possible among any node in the entire tree.
#
# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
#
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
# Example 2:
#
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
# Example 3:
#
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
#
#
# Constraints:
#
# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.
#
#
# Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Solution
# Python O(N) O(N) BreadthFirstSearch HashMap
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        path: list[int] = [-1] * 1001
        while cur_nodes:
            for vertex in cur_nodes:
                if vertex.left:
                    next_nodes.append(vertex.left)
                    path[vertex.left.val] = vertex
                if vertex.right:
                    next_nodes.append(vertex.right)
                    path[vertex.right.val] = vertex
            if not next_nodes: break
            cur_nodes = next_nodes
            next_nodes = []
        while len(cur_nodes) > 1:
            parents: list[TreeNode] = []
            for child in cur_nodes:
                if not parents or parents[-1] != path[child.val]:
                    parents.append(path[child.val])
            cur_nodes = parents
        return cur_nodes[0]

# C++ O(N) O(N) BreadthFirstSearch HashMap
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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        vector<TreeNode *> curNodes;
        vector<TreeNode *> nextNodes;
        vector<TreeNode*> path (1001, nullptr);
        curNodes.push_back(root);
        while (!curNodes.empty()) {
            for (TreeNode *vertex : curNodes) {
                if (vertex->left){
                    nextNodes.push_back(vertex->left);
                    path[vertex->left->val] = vertex;
                }
                if (vertex->right) {
                    nextNodes.push_back(vertex->right);
                    path[vertex->right->val] = vertex;
                }
            }
            if (nextNodes.empty()) break;
            curNodes = nextNodes;
            nextNodes.clear();
        }
        while (curNodes.size() > 1) {
            vector<TreeNode *> parents;
            for (TreeNode *child : curNodes) {
                if (parents.empty() || parents.back() != path[child->val]) {
                    parents.push_back(path[child->val]);
                }
            }
            curNodes = parents;
        }
        return curNodes[0];
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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur_nodes: list[TreeNode] = [root]
        next_nodes: list[TreeNode] = []
        parent: list[TreeNode] = [None] * 501
        while cur_nodes:
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                    parent[node.left.val] = node
                if node.right:
                    next_nodes.append(node.right)
                    parent[node.right.val] = node
            if not next_nodes: break
            cur_nodes = next_nodes.copy()
            next_nodes.clear()
        while len(cur_nodes) > 1:
            next_nodes.clear()
            for node in cur_nodes:
                if not next_nodes or next_nodes[-1] != parent[node.val]:
                    next_nodes.append(parent[node.val])
            cur_nodes = next_nodes.copy()
        return cur_nodes[-1]

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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        std::vector<TreeNode*> curNodes = {root}, nextNodes, parent(501, nullptr);
        while (!curNodes.empty()) {
            for (TreeNode* node : curNodes) {
                if (node->left) {
                    nextNodes.push_back(node->left);
                    parent[node->left->val] = node;
                }
                if (node->right) {
                    nextNodes.push_back(node->right);
                    parent[node->right->val] = node;
                }
            }
            if (nextNodes.empty()) break;
            curNodes = nextNodes;
            nextNodes.clear();
        }
        while (curNodes.size() > 1) {
            nextNodes.clear();
            for (TreeNode* node : curNodes) {
                if (nextNodes.empty() || nextNodes.back() != parent[node->val]) {
                    nextNodes.push_back(parent[node->val]);
                }
            }
            curNodes = nextNodes;
        }
        return curNodes.back();
    }
};