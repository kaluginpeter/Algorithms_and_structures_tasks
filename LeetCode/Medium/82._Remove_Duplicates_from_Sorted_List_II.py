# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
# Solution
# Python O(N) O(N) TwoPointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: ListNode = ListNode(next=head)
        tmp: ListNdoe = prev
        while tmp:
            tmp_next: ListNode = tmp.next
            tmp_next_copy: ListNode = tmp_next
            size: int = 0
            while tmp_next and (tmp_next.val == tmp_next_copy.val):
                size += 1
                tmp_next = tmp_next.next
            if size > 1: tmp.next = tmp_next
            else: tmp = tmp.next
        return prev.next

# C++ O(N) O(N) TwoPointers
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *prev = new ListNode();
        prev->next = head;
        ListNode *tmp = prev;
        while (tmp) {
            size_t size = 0;
            ListNode *tmpNext = tmp->next;
            ListNode *tmpNextCopy = tmpNext;
            while (tmpNext && tmpNext->val == tmpNextCopy->val) {
                ++size;
                tmpNext = tmpNext->next;
            }
            if (size > 1) tmp->next = tmpNext;
            else tmp = tmp->next;
        }
        return prev->next;
    }
};