# You are given the head node of a singly-linked list. Write a method that swaps each pair of nodes in the list, then returns the head node of the list. You have to swap the nodes themselves, not their values.
#
# Example:
#
# (A --> B --> C --> D) => (B --> A --> D --> C)
#
# The swapping should be done left to right, so if the list has an odd length, the last node stays in place:
#
# (A --> B --> C) => (B --> A --> C)
#
# The list will be composed of Nodes of the following specification:
#
# class Node:
#     def __init__(self, next=None):
#         self.next = next
# ALGORITHMSDATA STRUCTURESLINKED LISTS
# Solution
from preloaded import Node

def swap_pairs(head):
    length: int = 0
    tmp: Node = head
    while tmp:
        length += 1
        tmp = tmp.next
    if length <= 1: return head
    first: Node = head
    second: Node = head.next
    first.next = second.next
    second.next = first
    head = second
    tmp = head.next
    while tmp:
        first: Node = tmp.next
        if not first: break
        second: Node = tmp.next.next
        if not second: break
        first.next = second.next
        second.next = first
        tmp.next = second
        tmp = tmp.next.next
    return head