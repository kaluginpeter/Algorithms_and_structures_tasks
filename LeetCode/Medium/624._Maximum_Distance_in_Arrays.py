# You are given m arrays, where each array is sorted in ascending order.
#
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
#
# Return the maximum distance.
#
#
#
# Example 1:
#
# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Example 2:
#
# Input: arrays = [[1],[1]]
# Output: 0
#
#
# Constraints:
#
# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] is sorted in ascending order.
# There will be at most 105 integers in all the arrays.
# Solution
# Solution 1 - Two pass greedy based in logic
# General idea:
# We should choose two biggest element and two smallest element for avoiding case
# when biggest and lowest element are in the same array.
# Store value and index of each max and min element and at the and make some checks
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        first_max = idx_first_max = None
        second_max = idx_second_max = None
        for arr_idx in range(len(arrays)):
            if first_max is None or arrays[arr_idx][-1] > first_max:
                second_max, idx_second_max = first_max, idx_first_max
                first_max, idx_first_max = arrays[arr_idx][-1], arr_idx
            elif second_max is None or arrays[arr_idx][-1] > second_max:
                second_max, idx_second_max = arrays[arr_idx][-1], arr_idx

        first_min = idx_first_min = None
        second_min = idx_second_min = None
        for arr_idx in range(len(arrays)):
            if first_min is None or arrays[arr_idx][0] < first_min:
                second_min, idx_second_min = first_min, idx_first_min
                first_min, idx_first_min = arrays[arr_idx][0], arr_idx
            elif second_min is None or arrays[arr_idx][0] < second_min:
                second_min, idx_second_min = arrays[arr_idx][0], arr_idx

        distances: list[int] = []
        if idx_first_max != idx_first_min:
            distances.append(abs(first_max - first_min))
        if idx_first_max != idx_second_min:
            distances.append(abs(first_max - second_min))
        if idx_second_max != idx_first_min:
            distances.append(abs(second_max - first_min))
        if idx_second_max != idx_second_min:
            distances.append(abs(second_max - second_min))
        return max(distances)

# Solution 2 - OnePass greedy
# General idea:
# In the loop from entire arrays choose most long distance.
# For avoiding case when min and max element in same array,
# we start min and max elements in first array and our loop will be starting from second array
# Complexity
# Time complexity: O(N)
# Space complexity: O(1)
# Code
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_element, max_element = arrays[0][0], arrays[0][-1]
        max_distance: int = float('-inf')
        for arr_idx in range(1, len(arrays)):
            max_distance = max(
                max_distance,
                abs(arrays[arr_idx][-1] - min_element),
                abs(max_element - arrays[arr_idx][0])
            )
            min_element = min(min_element, arrays[arr_idx][0])
            max_element = max(max_element, arrays[arr_idx][-1])
        return max_distance