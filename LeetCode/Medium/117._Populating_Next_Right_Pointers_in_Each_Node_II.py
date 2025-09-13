# Given a binary tree
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
#
#
# Follow-up:
#
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
# Solution
# Python O(N) O(1) Tree Depth-First-Search
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node: 'Node' = root
        while node:
            dummy: 'Node' = Node()
            cur: 'Node' = dummy
            while node:
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                node = node.next
            node = dummy.next
        return root

# C++ O(N) O(1) Depth-First-Search Tree
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node* node = root;
        while (node) {
            Node* dummy = new Node();
            Node* cur = dummy;
            while (node) {
                if (node->left) {
                    cur->next = node->left;
                    cur = cur->next;
                }
                if (node->right) {
                    cur->next = node->right;
                    cur = cur->next;
                }
                node = node->next;
            }
            node = dummy->next;
        }
        return root;
    }
};