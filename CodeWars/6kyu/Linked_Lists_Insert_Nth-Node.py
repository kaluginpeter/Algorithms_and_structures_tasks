# Linked Lists - Insert Nth
#
# Implement an InsertNth() function (insert_nth() in PHP) which can insert a new node at any index within a list.
#
# InsertNth() is a more general version of the Push() function that we implemented in the first kata listed below. Given a list, an index 'n' in the range 0..length, and a data element, add a new node to the list so that it has the given index. InsertNth() should return the head of the list.
#
# insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
# insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
# insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)
# You must throw/raise an exception (ArgumentOutOfRangeException in C#, InvalidArgumentException in PHP) if the index is too large.
#
# The push() and buildOneTwoThree() (build_one_two_three() in PHP) functions do not need to be redefined. The Node class is also preloaded for you in PHP.
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
# LINKED LISTSDATA STRUCTURESFUNDAMENTALS
# Solution
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_nth(head, index, data):
    tmp = head
    if not tmp:
        head = Node(data)
        return head
    if index == 0:
        nxt = tmp
        head = Node(data)
        head.next = nxt
        return head
    for i in range(index - 1):
        tmp = tmp.next
    nxt = tmp.next
    tmp.next = Node(data)
    tmp.next.next = nxt
    return head