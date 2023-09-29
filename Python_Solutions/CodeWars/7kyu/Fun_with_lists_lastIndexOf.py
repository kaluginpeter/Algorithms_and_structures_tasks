# Implement the method lastIndexOf (last_index_of in PHP and Python), which accepts a linked list (head) and a value, and returns the index (zero based) of the last occurrence of that value if exists, or -1 otherwise.
#
# For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, lastIndexOf / last_index_of should return 3.
#
# The linked list is defined as follows:
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# Note: the list may be null/None and can hold any type of value.
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
def last_index_of(head, search_val):
    count = pos = -1
    while head:
        count += 1
        if head.data == search_val:
            pos = count
        head = head.next
    return pos