# Task
# You are given a positive integer n. Your objective is to transform this number into another number with all digits identical, while minimizing the number of changes. Each step in the transformation involves incrementing or decrementing a digit by one.
#
# For example, if the given number is 399, it can be transformed into 999 in 6 steps by incrementing the first digit by 6. Converting to any other identical digits number would take more than 6 steps.
#
# If n already consists of identical digits, the function should return 0, as no changes are needed. Wrapping, which means moving from 9 to 0 or 0 to 9 in one step, is not allowed.
#
# Examples
# 399 ➞ 6
# # 399 transformed to 999 in 6 steps.
#
# 1234 ➞ 4
# # there are two possible transformations with identical digits: 2222 and 3333.
# # The function should return 4 as it takes 4 steps to transform 1234 into either 2222 or 3333.
# # The steps involved could be either incrementing or decrementing a digit by one at a time until all digits become the same.
#
# 900 ➞ 9
# # 900 can be transformed to 000 after decrementing first digit 9 times to `0`.
#
# 7777 ➞ 0
# AlgorithmsMathematics