# Implement the method indexOf (index_of in PHP), which accepts a linked list (head) and a value, and returns the index (zero based) of the first occurrence of that value if exists, or -1 otherwise.
#
# For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, indexOf / index_of should return 2.
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
def index_of(head, value):
    top = 0
    while head:
        if type(head.data) == type(value):
            if head.data == value:
                return top
        head = head.next
        top += 1
    return -1