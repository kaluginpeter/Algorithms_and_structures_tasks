# Given the head of a singly linked list, return true if it is a
# palindrome or false otherwise.
#
# Example 1:
#
# Input: head = [1,2,2,1]
# Output: true
# Example 2:
#
# Input: head = [1,2]
# Output: false
#
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
# Follow up: Could you do it in O(n) time and O(1) space?
# Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def get_mid_node(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_ll(head):
            prev = None
            while head is not None:
                curr = head
                head = head.next
                curr.next = prev
                prev = curr
            return prev

        def is_ll_palindrome(L1, L2):
            while L1 and L2:
                if L1.val != L2.val:
                    return False
                L1, L2 = L1.next, L2.next
            return True

        mid_node = get_mid_node(head)
        L2 = reverse_ll(mid_node)
        return is_ll_palindrome(head, L2)


# Solution Stack and Two Pointers O(N) O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack: list = list()
        tmp, n = head, 0
        while tmp:
            stack.append(tmp.val)
            tmp, n = tmp.next, n+ 1
        left, right = 0, n - 1
        while left <= right:
            if stack[left] != stack[right]:
                return False
            left, right = left + 1, right - 1
        return True