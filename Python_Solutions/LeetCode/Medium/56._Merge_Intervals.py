# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
# Solution
# Merging in extra array
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(N)
# Code
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output: list[list[int]] = []
        start, end = intervals[0]
        for idx in range(1, len(intervals)):
            next_start, next_end = intervals[idx]
            if end >= next_start:
                end = max(end, next_end)
            else:
                output.append([start, end])
                start, end = next_start, next_end
        output.append([start, end])
        return output

# Merging in place
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(M), where M represent total count of merged intervals and in worst case it can be O(N),
# but operation of adding merged pairs in array have a O(1) time
# Code
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        main_idx: int = 0
        start, end = intervals[0]
        for idx in range(1, len(intervals)):
            next_start, next_end = intervals[idx]
            if end >= next_start:
                end = max(end, next_end)
            else:
                intervals[main_idx] = [start, end]
                start, end = next_start, next_end
                main_idx += 1
        intervals[main_idx] = [start, end]
        main_idx += 1
        return intervals[:main_idx]