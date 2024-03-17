# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105
# Solution O(N) O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans: list = list()
        x, y = newInterval[0], newInterval[1]
        seen: bool = False
        added: bool = False
        for i in intervals:
            if i[0] > newInterval[1]: # Current interval more than newInterval
                if seen: # if we making overlap
                    ans.append([x, y])
                    seen = False
                    ans.append(i)
                else:
                    if not added: # if we not added newInterval
                        ans.append(newInterval)
                    ans.append(i)
                added = True
            elif i[0] < newInterval[0] and i[1] < newInterval[0]: # current interval less than newInterval
                ans.append(i)
            elif not added: # Current interval can make overlap with newInterval
                seen = True
                x, y = min(x, i[0]), max(y, i[1])
        if seen: # if we making overlap and overlap interval not adding in answer
            ans.append([x, y])
        elif not added: # if we not adding newInterval in answer
            ans.append([x, y])
        return ans