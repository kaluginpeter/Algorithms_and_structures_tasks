# Given a binary tree root and a linked list with head as the first node.
#
# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
#
# In this context downward path means a path that starts at some node and goes downwards.
#
#
#
# Example 1:
#
#
#
# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.
# Example 2:
#
#
#
# Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Example 3:
#
# Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
#
#
# Constraints:
#
# The number of nodes in the tree will be in the range [1, 2500].
# The number of nodes in the list will be in the range [1, 100].
# 1 <= Node.val <= 100 for each node in the linked list and binary tree.
# Solution Depth-First-Search, Two Pointers(for second simplify solution)
# Python O(N*M) where N is length of Tree and M is length of Linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_path_checker(self, root: Optional[TreeNode], tmp: Optional[ListNode]) -> bool:
        if not root: return False
        if root.val == tmp.val:
            tmp: Optional[ListNode] = tmp.next
            if not tmp: return True
            return self.dfs_path_checker(root.left, tmp) or self.dfs_path_checker(root.right, tmp)
        return False

    def dfs(self, root: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not root: return False
        if root.val == head.val:
            tmp: Optinal[ListNode] = head
            result: bool = self.dfs_path_checker(root, tmp)
            if result: return True
        return self.dfs(root.left, head) or self.dfs(root.right, head)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.dfs(root, head)
# C++ O(N*M)
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool pathChecker(TreeNode* root, ListNode* tmp) {
        if (not root) {
            return false;
        } else if (root->val == tmp->val) {
            tmp = tmp->next;
            if (not tmp) {
                return true;
            } else {
                return pathChecker(root->left, tmp) || pathChecker(root->right, tmp);
            }
        } else {
            return false;
        }
    };
    bool dfs(TreeNode* root, ListNode* tmp) {
        if (not root) {
            return false;
        } else if (root->val == tmp->val) {
            bool result = pathChecker(root, tmp);
            if (result) {
                return true;
            }
        }
        return dfs(root->left, tmp) || dfs(root->right, tmp);
    };

    bool isSubPath(ListNode* head, TreeNode* root) {
        return dfs(root, head);
    };
};

# Python simplify solution O(N*M) with Two Pointers
class Solution:
    def dfs(self, root: Optional[TreeNode], tmp: Optional[ListNode], head: Optional[TreeNode]) -> bool:
        if not tmp: return True
        if not root: return False

        if root.val == tmp.val:
            tmp = tmp.next
        elif root.val == head.val:
            head = head.next
        else:
            tmp = head
        return self.dfs(root.left, tmp, head) or self.dfs(root.right, tmp, head)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.dfs(root, head, head)
# C++ simplify solution O(N*M)
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    bool dfs(TreeNode* root, ListNode* tmp, ListNode* head) {
        if (not tmp) {
            return true;
        }
        if (not root) {
            return false;
        }
        if (root->val == tmp->val) {
            tmp = tmp->next;
        } else if (root->val == head->val) {
            head = head->next;
        } else {
            tmp = head;
        }
        return dfs(root->left, tmp, head) || dfs(root->right, tmp, head);
    };

    bool isSubPath(ListNode* head, TreeNode* root) {
        return dfs(root, head, head);
    };
};