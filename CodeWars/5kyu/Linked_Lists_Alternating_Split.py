# Linked Lists - Alternating Split
#
# Write an AlternatingSplit() function that takes one list and divides up its nodes to make two smaller lists. The sublists should be made from alternating elements in the original list. So if the original list is a -> b -> a -> b -> a -> null then one sublist should be a -> a -> a -> null and the other should be b -> b -> null.
#
# list = 1 -> 2 -> 3 -> 4 -> 5 -> None
# alternating_split(list).first == 1 -> 3 -> 5 -> None
# alternating_split(list).second == 2 -> 4 -> None
# For simplicity, we use a Context object to store and return the state of the two linked lists. A Context object containing the two mutated lists should be returned by AlternatingSplit().
#
# If the passed in head node is null/None/nil or a single node, throw an error.
#
# Related Kata in order of expected completion (increasing difficulty):
#  Linked Lists - Push & BuildOneTwoThree
#  Linked Lists - Length & Count
#  Linked Lists - Get Nth Node
# Linked Lists - Insert Nth Node
# Linked Lists - Sorted Insert
# Linked Lists - Insert Sort
# Linked Lists - Append
# Linked Lists - Remove Duplicates
# Linked Lists - Move Node
# Linked Lists - Move Node In-place
# Linked Lists - Alternating Split
# Linked Lists - Front Back Split
# Linked Lists - Shuffle Merge
# Linked Lists - Sorted Merge
# Linked Lists - Merge Sort
# Linked Lists - Sorted Intersect
# Linked Lists - Iterative Reverse
# Linked Lists - Recursive Reverse
#
# Inspired by Stanford Professor Nick Parlante's excellent Linked List teachings.
#
# Data StructuresLinked ListsFundamentals
# Solution
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def create(x: list[int]) -> Node:
    root: Node = Node()
    tmp: Node = root
    for val in x:
        tmp.next = Node(data=val)
        tmp = tmp.next
    return root.next


def alternating_split(head):
    if not head: raise ValueError()
    first: list[int] = []
    second: list[int] = []
    i: int = 1
    tmp: Node = head
    while tmp:
        if i & 1:
            first.append(tmp.data)
        else:
            second.append(tmp.data)
        tmp = tmp.next
        i += 1
    if i == 2: raise ValueError()
    f: Node = create(first)
    s: Node = create(second)
    return Context(f, s)