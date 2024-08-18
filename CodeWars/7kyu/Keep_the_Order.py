# Task:
# Your job here is to write a function (keepOrder in JS/CoffeeScript, keep_order in Ruby/Crystal/Python, keeporder in Julia), which takes a sorted array ary and a value val, and returns the lowest index where you could insert val to maintain the sorted-ness of the array. The input array will always be sorted in ascending order. It may contain duplicates.
#
# Do not modify the input.
#
# Some examples:
# keep_order([1, 2, 3, 4, 7], 5) #=> 4
#                       ^(index 4)
# keep_order([1, 2, 3, 4, 7], 0) #=> 0
#           ^(index 0)
# keep_order([1, 1, 2, 2, 2], 2) #=> 2
#                 ^(index 2)
# Also check out my other creations — Naming Files, Elections: Weighted Average, Identify Case, Split Without Loss, Adding Fractions, Random Integers, Implement String#transpose, Implement Array#transpose!, Arrays and Procs #1, and Arrays and Procs #2.
#
# If you notice any issues or have any suggestions/comments whatsoever, please don't hesitate to mark an issue or just comment. Thanks!
#
# FUNDAMENTALS
# Solution
def keep_order(ary, val):
    l, r = 0, len(ary) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if ary[mid] >= val:
            r = mid - 1
        else:
            l = mid + 1
    return l