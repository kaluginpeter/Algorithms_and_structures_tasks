# Task
# In an integer array, gap means the difference between two adjacent elements.
#
# Maximum gap means the maximum value of all gaps.
#
# Given a sorted integer array arr. Then, we remove an element arbitrarily from the inner part of an array(inner part means that not include the first and last elements).
#
# Your task is to find the minimum possible maximum gap after the remove operation.
#
# Example
# For arr = [1,2,5,7,8], the output should be 3.
#
# In this case, we can remove one element of 2,5,7
# If remove 2, the maximum gap of [1,5,7,8] is 4
# (The deffrence between 1 and 5)
# If remove 5, the maximum gap of [1,2,7,8] is 5
# (The deffrence between 2 and 7)
# If remove 2, the maximum gap of [1,2,5,8] is 3
# (The deffrence between 2 and 5, or 5 and 8)
# So, the minimum possible maximum gap is 3
# For arr = [1,4,6], the output should be 5.
#
# We can only remove 4 from the array. So, 6 - 1 = 5
#
# For arr = [1,2,3,4,5], the output should be 2.
#
# We can remove one element of 2,3,4. Whichever element is removed, the maximum gap always be 2.
#
# Algorithms
# Solution
def min_max_gap(arr):
    return max(min(arr[i + 1] - arr[i - 1] for i in range(1, len(arr) - 1)), max(arr[i] - arr[i - 1] for i in range(1, len(arr))))
