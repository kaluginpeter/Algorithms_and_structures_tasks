# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
# Solution
# Python O(N) O(1) TwoPointers LinkedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return head
        prev: ListNode = ListNode(next=head)
        tmp: ListNode = prev
        prev_less_than: ListNode = prev
        less_than: ListNode = head
        while tmp:
            while less_than and less_than.val >= x:
                prev_less_than = prev_less_than.next
                less_than = less_than.next
            if not less_than: break
            elif tmp == prev_less_than:
                tmp = tmp.next
                prev_less_than = prev_less_than.next
                less_than = less_than.next
                continue
            prev_less_than.next = less_than.next
            tmp_next_copy: ListNode = tmp.next
            tmp.next = less_than
            less_than.next = tmp_next_copy
            tmp = tmp.next
            less_than = prev_less_than.next
        return prev.next

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
    ListNode* partition(ListNode* head, int x) {
        if (!head) return head;
        ListNode* prev = new ListNode();
        prev->next = head;

        ListNode* tmp = prev;
        ListNode* prevLessThan = prev;
        ListNode* lessThan = head;
        while (tmp) {
            while (lessThan && lessThan->val >= x) {
                prevLessThan = prevLessThan->next;
                lessThan = lessThan->next;
            }
            if (!lessThan) break;
            else if (tmp == prevLessThan) {
                tmp = tmp->next;
                prevLessThan = prevLessThan->next;
                lessThan = lessThan->next;
                continue;
            }
            prevLessThan->next = lessThan->next;
            ListNode *tmpNextCopy = tmp->next;
            tmp->next = lessThan;
            lessThan->next = tmpNextCopy;
            tmp = tmp->next;
            lessThan = prevLessThan->next;
        }
        return prev->next;
    }
};