# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
#
#
#
# Example 1:
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:
#
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:
#
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104
# Solution
# Python O(NlogN) O(1) Sorting Greedy
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count: int = 0
        cur_end: int = float('-inf')
        for interval in intervals:
            if interval[0] >= cur_end:
                cur_end = interval[1]
            else:
                count += 1
        return count

# C++ O(NlogN) O(1) Sorting Greedy
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](std::vector<int>& x, std::vector<int>& y){
            return x[1] < y[1];
        });
        int count = 0;
        int curEnd = INT32_MIN;
        for (int i = 0; i < intervals.size(); ++i) {
            if (intervals[i][0] >= curEnd) {
                curEnd = intervals[i][1];
            } else {
                ++count;
            }
        }
        return count;
    }
};