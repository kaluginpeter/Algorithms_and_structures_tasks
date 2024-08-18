# Implement the method countIf (count_if in PHP and Python), which accepts
# a linked list (head) and a predicate function, and returns the number
# of elements which apply to the given predicate.
#
# For example: Given the list: 1 -> 2 -> 3, and the predicate x => x >= 2,
# countIf / count_if should return 2, since x >= 2 applies to both 2 and 3.
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
# LISTSFUNCTIONAL PROGRAMMINGFUNDAMENTALS
# Solution
def count_if(head, func):
    c = 0
    while head:
        c += func(head.data)
        head = head.next
    return c