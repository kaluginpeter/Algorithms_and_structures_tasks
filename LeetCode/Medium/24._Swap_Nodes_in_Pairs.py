# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#
#
# Example 1:
#
# Input: head = [1,2,3,4]
#
# Output: [2,1,4,3]
#
# Explanation:
#
#
#
# Example 2:
#
# Input: head = []
#
# Output: []
#
# Example 3:
#
# Input: head = [1]
#
# Output: [1]
#
# Example 4:
#
# Input: head = [1,2,3]
#
# Output: [2,1,3]
#
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# Solution
# C++ O(N) O(1) Linked List
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
    ListNode* swapPairs(ListNode* head) {
        // Count length of linked list
        int n = 0;
        ListNode* tmp = head;
        while(tmp) {
            tmp = tmp->next;
            ++n;
        };
        // Only even swaps needed
        if (n % 2 != 0) {
            n -= 1;
        };
        // If no needed swaps
        if (!n) {
            return head;
        };
        // Make swap with head and second node
        ListNode* second = head->next;
        head->next = second->next;
        second->next = head;
        head = second;
        // Continue swapping if needed
        int index = 2;
        ListNode* first = head->next;
        while (index + 2 <= n) {
            ListNode* second = first->next->next;
            first->next->next = second->next;
            second->next = first->next;
            first->next = second;
            first = first->next->next;
            index += 2;
        };
        return head;
    }
};

# Python O(N) O(1) Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Count length of linked list
        n: int = 0
        tmp: ListNode = head
        while tmp:
            n += 1
            tmp = tmp.next
        # Only need make even swaps
        if n & 1: n -= 1
        # If no needed swaps
        if not n: return head
        # Make swap head with second node
        second: ListNode = head.next
        head.next = second.next
        second.next = head
        head = second
        # Continue swaping for other nodes it it needed
        idx: int = 2
        first: ListNode = head.next
        while idx + 2 <= n:
            second: ListNode = first.next.next
            first.next.next = second.next
            second.next = first.next
            first.next = second
            idx += 2
            first = first.next.next
        return head