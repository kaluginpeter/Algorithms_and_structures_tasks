# You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.
#
# For example in the following picture the size of the dangling piece is 3 and the loop size is 12:
#
#
# # Use the `next' attribute to get the following node
# node.next
# Notes:
#
# do NOT mutate the nodes!
# in some cases there may be only a loop, with no dangling piece
# Thanks to shadchnev, I broke all of the methods from the Hash class.
#
# Don't miss dmitry's article in the discussion after you pass the Kata !!
#
# ALGORITHMSLINKED LISTSPERFORMANCE
# Solution 1 - Speed O(N) / Memory O(N)
def loop_size(node):
    d, top = {}, 0
    while node not in d:
        d[node] = top
        top += 1
        node = node.next
    return top - d[node]
# Solution 2 Speed O(N) / Memory O(1) FLoyd Algorithm
def loop_size(node):
    x, y = node.next, node.next.next
    while x != y:
        x, y = x.next, y.next.next
    count, y = 1, y.next
    while x != y:
        count += 1
        y = y.next
    return count