# When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said
#
# Description:
# Given an unsorted array arr that contains some positive integers. It may be one of the following:
#
# 1. There are numbers 1 to n, only one number is
#    duplicate(repeated two times), the other numbers are unique.
#    That is, there are n+1 elements in the array.
#    e.g. [1,2,3,6,5,4,1]
#
# 2. There are numbers 1 to n, only one number is
#    unique, the other numbers are repeated two times.
#    That is, there are 2*n-1 elements in the array.
#    e.g. [1,2,3,1,2,3,4]
# Your task is to determine the type of the array, if it is the first type, to return the duplicate; if it is second type, return the unique.
#
# Note:
# All numbers are positive integers that from 1 to n;
# The length of array always more than 5;
# Please pay attention to optimizing the code to avoid time out.
# Some Examples
# input                                output
# [1,2,3,6,5,4,1]                      1
# [1,2,3,1,2,3,4]                      4
# [3,6,9,2,5,8,1,4,8,7]                8
# [9,8,7,1,2,3,9,7,1,2,3,4,4,5,5,6,6]  8
# AlgorithmsPuzzles