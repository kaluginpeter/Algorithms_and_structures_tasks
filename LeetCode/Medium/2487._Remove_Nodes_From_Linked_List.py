# You are given the head of a linked list.
#
# Remove every node which has a node with a greater value anywhere to the right side of it.
#
# Return the head of the modified linked list.
#
#
#
# Example 1:
#
#
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
# Example 2:
#
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
#
#
# Constraints:
#
# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105
# Solution O(N) O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse O(N) O(1)
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        # Removing O(N) O(1)
        tmp = head
        check: int = tmp.val
        while tmp:
            if tmp.next and tmp.next.val < check:
                tmp.next = tmp.next.next if tmp.next.next else None
            elif tmp.next and tmp.next.val > check:
                check = tmp.next.val
            else:
                tmp = tmp.next
        # Vice versa reversing O(N) O(1)
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        return head