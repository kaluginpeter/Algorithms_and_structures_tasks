# Implement the method length, which accepts a linked list (head), and returns the length of the list.
#
# For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.
#
# The linked list is defined as follows:
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# Note: the list may be null and can hold any type of value.
#
# Good luck!
#
# This kata is part of fun with lists series:
#
# Fun with lists: length
# Fun with lists: indexOf
# Fun with lists: lastIndexOf
# Fun with lists: countIf
# Fun with lists: anyMatch + allMatch
# Fun with lists: filter
# Fun with lists: map
# Fun with lists: reduce
# LISTSFUNDAMENTALS
# Solution
def length(head):
    if head == None:
        return 0
    elif head:
        number = 1
        while head.next:
              head = head.next
              number += 1
        return number