# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
#
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
#
# Return the head of the modified linked list.
#
#
#
# Example 1:
#
#
# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation:
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.
# Example 2:
#
#
# Input: head = [0,1,0,3,0,2,2,0]
# Output: [1,3,4]
# Explanation:
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 1 = 1.
# - The sum of the nodes marked in red: 3 = 3.
# - The sum of the nodes marked in yellow: 2 + 2 = 4.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [3, 2 * 105].
# 0 <= Node.val <= 1000
# There are no two consecutive nodes with Node.val == 0.
# The beginning and end of the linked list have Node.val == 0.
# Solution O(N) O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        inner_tmp = head
        top: int = 0
        while tmp.next:
            if tmp.val == 0 and tmp is not head:
                inner_tmp.val = top
                inner_tmp = inner_tmp.next
                top = 0
            top += tmp.val
            tmp = tmp.next
        inner_tmp.val = top
        inner_tmp.next = None
        return head


# Solution O(N) O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        accumulate: int = 0
        tmp = head
        local_tmp = tmp.next
        while local_tmp:
            while local_tmp and local_tmp.val != 0:
                accumulate += local_tmp.val
                local_tmp = local_tmp.next
            if accumulate:
                tmp.val = accumulate
                tmp.next = local_tmp if local_tmp.next else None
                accumulate = 0
                tmp = tmp.next
            local_tmp = local_tmp.next
        return head