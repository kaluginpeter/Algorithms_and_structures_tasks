# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
# Follow up: Could you do it in one pass?
# Solution
# Python O(N) O(1) TwoPointers LinkedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        size: int = 0
        output: ListNode = ListNode(next=head)
        tmp: ListNode = output
        l: ListNode = head
        r: ListNode = head
        while size < right:
            size += 1
            if size < left:
                tmp = tmp.next
                l = l.next
            r = r.next
        for _ in range(right - left):
            tmp.next = l.next
            l.next = r
            r = l
            l = tmp.next
        l.next = r
        return output.next

# C++ O(N) O(1) TwoPointers LinkedList
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (left == right) return head;
        ListNode* output = new ListNode();
        output->next = head;
        ListNode* tmp = output;
        ListNode* l = head;
        ListNode* r = head;
        size_t i = 0;
        while (i < right) {
            ++i;
            if (i < left) {
                tmp = tmp->next;
                l = l->next;
            }
            r = r->next;
        }
        for (size_t i = 0; i < right - left; ++i) {
            tmp->next = l->next;
            l->next = r;
            r = l;
            l = tmp->next;
        }
        l->next = r;
        return output->next;
    }
};