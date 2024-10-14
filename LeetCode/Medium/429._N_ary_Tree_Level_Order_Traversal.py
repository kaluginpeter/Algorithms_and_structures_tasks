# Given an n-ary tree, return the level order traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
#
#
#
# Example 1:
#
#
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# Example 2:
#
#
#
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
#
#
# Constraints:
#
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 104]
# Solution
# Python O(N) O(N) Depth-First-Search
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, root: 'Node', depth: int, levels: list[list[int]]) -> None:
        if not root:
            return
        if depth > len(levels) - 1:
            levels.append([root.val])
        else:
            levels[depth].append(root.val)
        for child in root.children:
            self.traverse(child, depth + 1, levels)

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output: list[list[int]] = []
        self.traverse(root, 0, output)
        return output

# C++ O(N) O(N) Depth-First-Search
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    void traverse(Node* root, int depth, std::vector<std::vector<int>>& levels) {
        if (!root) {
            return;
        }
        if (depth >= levels.size()) {
            levels.push_back({root->val});
        } else {
            levels[depth].push_back(root->val);
        }
        for (Node* child : root->children) {
            if (child) {
                traverse(child, depth + 1, levels);
            }
        }
    }

    vector<vector<int>> levelOrder(Node* root) {
        std::vector<std::vector<int>> output;
        traverse(root, 0, output);
        return output;
    }
};

# Python O(N) O(N) Breadth-First-Search
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output: list[list[int]] = []
        if root:
            output.append([root.val])
        current_nodes: list[Node] = [root]
        next_nodes: list[Node] = []
        while current_nodes:
            level_output: list[int] = []
            for node in current_nodes:
                if not node: continue
                for child in node.children:
                    next_nodes.append(child)
                    if child:
                        level_output.append(child.val)
            if level_output:
                output.append(level_output)
            current_nodes = next_nodes
            next_nodes = []
        return output

# C++ O(N) O(N) Breadth-First-Search
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        std::vector<std::vector<int>> output;
        if (root) {
            output.push_back({root->val});
        }
        std::vector<Node*> current_nodes = {root};
        std::vector<Node*> next_nodes;
        while (current_nodes.size()) {
            std::vector<int> output_level;
            for (Node* node : current_nodes) {
                if (!node) {
                    continue;
                }
                for (Node* child : node->children) {
                    next_nodes.push_back(child);
                }
            }
            for (Node* node : next_nodes) {
                if (node) {
                    output_level.push_back(node->val);
                }
            }
            if (output_level.size()) {
                output.push_back(output_level);
            }
            current_nodes = next_nodes;
            next_nodes.clear();
        }
        return output;
    }
};