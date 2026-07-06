# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
#
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
#
# Return the number of remaining intervals.
#
#
#
# Example 1:
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:
#
# Input: intervals = [[1,4],[2,3]]
# Output: 1
#
#
# Constraints:
#
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= li < ri <= 105
# All the given intervals are unique.
#
# Solution
# Python O(NlogN) O(1) Greedy Sorting
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: (pair[0], -pair[1]))
        ptr: int = 0
        output: int = 1
        for i in range(1, len(intervals)):
            if intervals[ptr][1] >= intervals[i][1]: continue
            output += 1
            ptr = i
        return output

# C++ O(NlogN) O(1) Sorting Greedy
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& x, const std::vector<int>& y){
            if (x[0] != y[0]) return x[0] < y[0];
            return -x[1] < -y[1];
        });
        size_t output = 1;
        auto cur = intervals.begin();
        for (auto it = ++intervals.begin(); it < intervals.end(); ++it) {
            if ((*cur)[1] >= (*it)[1]) continue;
            else {
                ++output;
                cur = it;
            }
        }
        return output;
    }
};