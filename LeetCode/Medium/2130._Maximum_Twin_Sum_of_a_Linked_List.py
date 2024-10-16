# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
#
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.
#
#
#
# Example 1:
#
#
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6.
# Example 2:
#
#
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
# Example 3:
#
#
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
#
#
# Constraints:
#
# The number of nodes in the list is an even integer in the range [2, 105].
# 1 <= Node.val <= 105
# Solution 1 - Tortoise and Hare
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans: int = float('-inf')
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        left, right = head, prev
        while right:
            ans = max(ans, left.val + right.val)
            left, right = left.next, right.next
        return ans

# Solution 2 - List storing aka Stack
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes: list = list()
        n: int = 0
        tmp = head
        while tmp:
            nodes.append(tmp.val)
            tmp, n = tmp.next, n + 1
        ans: int = float('-inf')
        for i in range(n):
            ans = max(ans, nodes[i] + nodes[n - i - 1])
        return ans

# C++ O(N) O(1) Two Pointers
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
class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* prev = nullptr;
        while (slow) {
            ListNode* next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next;
        }
        int max_sum = 0;
        ListNode* left = head;
        ListNode* right = prev;
        while (right) {
            max_sum = std::max(max_sum, left->val + right->val);
            right = right->next;
            left = left->next;
        }
        return max_sum;
    }
};