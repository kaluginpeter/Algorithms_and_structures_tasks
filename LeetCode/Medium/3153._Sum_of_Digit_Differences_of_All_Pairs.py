# You are given an array nums consisting of positive integers where all integers have the same number of digits.
#
# The digit difference between two integers is the count of different digits that are in the same position in the two integers.
#
# Return the sum of the digit differences between all pairs of integers in nums.
#
#
#
# Example 1:
#
# Input: nums = [13,23,12]
#
# Output: 4
#
# Explanation:
# We have the following:
# - The digit difference between 13 and 23 is 1.
# - The digit difference between 13 and 12 is 1.
# - The digit difference between 23 and 12 is 2.
# So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.
#
# Example 2:
#
# Input: nums = [10,10,10,10]
#
# Output: 0
#
# Explanation:
# All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.
#
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# 1 <= nums[i] < 109
# All integers in nums have the same number of digits.