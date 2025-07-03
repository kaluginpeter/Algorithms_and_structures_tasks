# Task
# Given a length, an offset, and a list, slide a window of that length, moving by that offset every step, over the list, returning a list of lists.
#
# The windows may overlap each other, or skip certain elements. All windows should be of the given length; if insufficient elements remain after a certain offset, end the list of lists. It is possible to take 0 elements from an empty list, so take care to handle window(0,offset,list) correctly.
#
# The length will always be non-negative; the offset will always be strictly positive.
#
# Examples
# for 2, 1, [0,1,2,3,4] return [ [0,1], [1,2], [2,3], [3,4] ]
# for 2, 2, [0,1,2,3,4] return [ [0,1], [2,3] ]
# for 2, 3, [0,1,2,3,4] return [ [0,1], [3,4] ]
# ListsArrays