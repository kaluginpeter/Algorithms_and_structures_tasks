# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# Output: [8, 9, 9, 9, 0, 0, 0, 1]
#
# Constraints:
#
# The number of nodes in each linked list is in the range[1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
# Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        carry = 0
        while l1 is not None or l2 is not None:
            sum_value = carry
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next
            node = ListNode(sum_value % 10)
            carry = sum_value // 10
            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next
        if carry > 0:
            temp.next = ListNode(carry)
        return head