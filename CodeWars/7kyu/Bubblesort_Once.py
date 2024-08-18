# Overview
# Bubblesort is an inefficient sorting algorithm that is simple to understand and therefore often taught in introductory computer science courses as an example how not to sort a list. Nevertheless, it is correct in the sense that it eventually produces a sorted version of the original list when executed to completion.
#
# At the heart of Bubblesort is what is known as a pass. Let's look at an example at how a pass works.
#
# Consider the following list:
#
# 9, 7, 5, 3, 1, 2, 4, 6, 8
# We initiate a pass by comparing the first two elements of the list. Is the first element greater than the second? If so, we swap the two elements. Since 9 is greater than 7 in this case, we swap them to give 7, 9. The list then becomes:
#
# 7, 9, 5, 3, 1, 2, 4, 6, 8
# We then continue the process for the 2nd and 3rd elements, 3rd and 4th elements ... all the way up to the last two elements. When the pass is complete, our list becomes:
#
# 7, 5, 3, 1, 2, 4, 6, 8, 9
# Notice that the largest value 9 "bubbled up" to the end of the list. This is precisely how Bubblesort got its name.
#
# Task
# Given an array of integers, your function bubblesortOnce/bubblesort_once/BubblesortOnce (or equivalent, depending on your language's naming conventions) should return a new array equivalent to performing exactly 1 complete pass on the original array. Your function should be pure, i.e. it should not mutate the input array.
#
# ALGORITHMSTUTORIALSSORTING
# Solution
def bubblesort_once(l):
    l = l.copy()
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            l[i-1], l[i] = l[i], l[i-1]
    return l