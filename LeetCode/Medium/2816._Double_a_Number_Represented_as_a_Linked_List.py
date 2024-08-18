# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
#
# Return the head of the linked list after doubling it.
#
#
#
# Example 1:
#
#
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
# Example 2:
#
#
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 104]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
# Solution Math O(N) O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Parse n
        n: int = 0
        tmp = head
        count: int = 0
        while tmp:
            count += 1
            n = n * 10 + tmp.val
            tmp = tmp.next
        n *= 2
        # Insert n in linked list
        out = head
        while n:
            out.val = n % 10
            n //= 10
            if out.next:
                out = out.next
            else:
                out.next = ListNode() if n else None
                out = out.next
        # Reverse list
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        return head