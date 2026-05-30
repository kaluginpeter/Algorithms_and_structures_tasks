# Moser Streaming
# In geometry, if you place points on a circle and connect every pair of points with straight lines, the circle becomes divided into regions.
#
# The maximum number of regions created follows the famous Moser circle sequence:
#
# 1, 2, 4, 8, 16, 31, 57, 99, 163, 256, ...
# Task
# Your task is to create an infinite generator that yields the values of this sequence one by one.
#
# The sequence begins at n = 1.
#
# Implement a generator function:
#
# def moser():
# Which yields the values in the Moser circle sequence indefinitely.
#
# Example
# for i in moser():
#     print(i)
#
# # prints 1, 2, 4, 8, 16, 31, 57, 99, 163, 256, 386, 562, 794, 1093...
# GeometryFundamentals