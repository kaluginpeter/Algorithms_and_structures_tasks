# When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said
#
# Description:
# Give an 2D integer array arr that contains some integers. Array arr has the following properties:
#
# Integers in each row are sorted from left to right.
# Integers in each column are sorted from up to bottom.
# No duplicate integers in each row or column.
# For example:
#
# arr = [
#  [1, 3, 5, 7],
#  [2, 4, 7, 8],
#  [3, 5, 9, 10]
#  ]
# Then give a target number num, your task is to count how many num in arr.
#
# arr = [...see above]
# num=3
# count_number(arr,num) == 2
#
# arr = [
#  [62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],
#  [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
#  [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],
#  [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],
#  [66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],
#  [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]],
# num=81
# count_number(arr,num) == 5
# Note:
# Arguments arr always be an 2D array;
# Please pay attention to optimizing the code to avoid time out.
# In the performance test(5000x5000 elements x 100 testcases), the time consuming of each test case should be within 5ms. This means, Your algorithm should be faster than O(mn), your code should run as fast as a rocket ;-)
# AlgorithmsPuzzles