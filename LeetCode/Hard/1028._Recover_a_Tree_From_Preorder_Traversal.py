# We run a preorder depth-first search (DFS) on the root of a binary tree.
#
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
#
# If a node has only one child, that child is guaranteed to be the left child.
#
# Given the output traversal of this traversal, recover the tree and return its root.
#
#
#
# Example 1:
#
#
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# Example 2:
#
#
# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# Example 3:
#
#
# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
#
#
# Constraints:
#
# The number of nodes in the original tree is in the range [1, 1000].
# 1 <= Node.val <= 109
# Solution
# Python O(N) O(H) Binary Tree Simulation Greedy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def parse_node(self, idx: int, traversal: str, n: int) -> tuple[int, int, int]:
        depth: int = 0
        while idx < n and traversal[idx] == '-':
            depth += 1
            idx += 1
        node_val: int = 0
        while idx < n and traversal[idx] != '-':
            node_val = node_val * 10 + int(traversal[idx])
            idx += 1
        return (idx, node_val, depth)

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels: list[TreeNode] = []
        n: int = len(traversal)
        idx: int = 0
        while idx < n:
            idx, node_val, depth = self.parse_node(idx, traversal, n)
            child: TreeNode = TreeNode(node_val)
            if not depth: # Root node
                levels.append(child)
                continue
            if depth == len(levels): # Child at new level
                levels.append(child)
            else: # Child at existing level
                levels[depth] = child
            parent: TreeNode = levels[depth - 1]
            if not parent.left:
                parent.left = child
            else:
                parent.right = child
        return levels[0]

# C++ O(N) O(H) BinaryTree Simulation Greedy
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
    tuple<int, int, int> parseNode(int& idx, const string& traversal, const int& n) {
        int depth = 0;
        while (idx < n && traversal[idx] == '-') {
            ++depth;
            ++idx;
        }
        int nodeVal = 0;
        while (idx < n && traversal[idx] != '-') {
            nodeVal = nodeVal * 10 + (traversal[idx] - '0');
            ++idx;
        }
        return {idx, nodeVal, depth};
    }

    TreeNode* recoverFromPreorder(string traversal) {
        vector<TreeNode*> levels;
        int idx = 0;
        int n = traversal.size();
        while (idx < n) {
            tuple<int, int, int> data = parseNode(idx, traversal, n);
            idx = get<0>(data);
            int nodeVal = get<1>(data), depth = get<2>(data);
            TreeNode* child = new TreeNode(nodeVal);
            if (!depth) { // Root node
                levels.push_back(child);
                continue;
            }
            if (depth == levels.size()) { // New level child
                levels.push_back(child);
            } else { // Existing level child
                levels[depth] = child;
            }
            TreeNode* parent = levels[depth - 1];
            if (!parent->left) parent->left = child;
            else parent->right = child;
        }
        return levels[0];
    }
};