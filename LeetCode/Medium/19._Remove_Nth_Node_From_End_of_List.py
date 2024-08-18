# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
# Follow up: Could you do this in one pass?
# Solution O(N) O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        ln: int = 0
        while tmp:
            ln += 1
            tmp = tmp.next
        if ln == 1 or ln - n == 0:
            head = head.next
            return head
        tmp = head
        for i in range(ln - n - 1):
            tmp = tmp.next
        tmp.next = tmp.next.next if tmp.next else tmp.next
        return head
# Solution Two Pointers O(N) O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode('new_head', head)
        fast, slow = new_head, new_head
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return new_head.next