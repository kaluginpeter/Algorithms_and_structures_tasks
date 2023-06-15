# Stuck? [Try this one](http://www.codewars.com/kata/remove-the-minimum).
# A Storm at Sea
# Jill the adventurer has seen everything, from the highest mountains,
# to the most dangerous animals. But today she sailed through a hideous storm and shipwrecked.
# Left with only a damaged life boat and some supplies, she has carefully balanced out the weight not to capsize.
# But the weight is too much for the small life boat, she has to get rid of some items.
#
# Beginning from one side of the boat, she starts to remove the n smallest items and hopes for the best…
#
# Task
# Given an array of integers, remove the n smallest. If there are multiple elements with the same value,
# remove the ones with a lower index first. If n is greater than the length of the array/list, return an
# empty list/array. If n is zero or less, return the original array/list.
#
# Don't change the order of the elements that are left.
#
# Examples
# remove_smallest ((-10), [1,2,3,4,5]) = [1,2,3,4,5]
# remove_smallest (0, [1,2,3,4,5]) = [1,2,3,4,5]
# remove_smallest (2, [5,3,2,1,4]) = [5,3,4]
# remove_smallest (3, [5,3,2,1,4]) = [5,4]
# remove_smallest (3, [1,2,3,4,5]) = [4,5]
# remove_smallest (5, [1,2,3,4,5]) = []
# remove_smallest (9, [1,2,3,4,5]) = []
#
# remove_smallest (2, [1,2,1,2,1]) = [2,2,1]
# LISTSARRAYSFUNDAMENTALS
# Solution
def remove_smallest(n, a):
    b = a[::]
    while n>0 and b: b.remove(min(b)); n -= 1
    return b