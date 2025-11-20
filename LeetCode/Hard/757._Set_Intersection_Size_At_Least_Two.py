# You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.
#
# A containing set is an array nums where each interval from intervals has at least two integers in nums.
#
# For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
# Return the minimum possible size of a containing set.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[3,7],[8,9]]
# Output: 5
# Explanation: let nums = [2, 3, 4, 8, 9].
# It can be shown that there cannot be any containing array of size 4.
# Example 2:
#
# Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
# Output: 3
# Explanation: let nums = [2, 3, 4].
# It can be shown that there cannot be any containing array of size 2.
# Example 3:
#
# Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
# Output: 5
# Explanation: let nums = [1, 2, 3, 4, 5].
# It can be shown that there cannot be any containing array of size 4.
#
#
# Constraints:
#
# 1 <= intervals.length <= 3000
# intervals[i].length == 2
# 0 <= starti < endi <= 108
# Solution
# Python O(NlogN) O(1) Sorting
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda point: (point[1], -point[0]))
        output: int = 2
        R: int = intervals[0][1]
        L: int = R - 1
        for start, end in intervals[1:]:
            if L >= start: continue
            if start > R: output += 1
            output += 1
            L = R if start <= R else end - 1
            R = end
        return output

# C++ O(NlogN) O(1) Sorting
class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [&](const std::vector<int>& x, const std::vector<int>& y) {
            if (x[1] != y[1]) return x[1] < y[1];
            return x[0] > y[0];
        });
        int R = intervals[0][1], L = R - 1, output = 2;
        for (size_t i = 1; i < intervals.size(); ++i) {
            if (L >= intervals[i][0]) continue;
            if (intervals[i][0] > R) ++output;
            ++output;
            L = (intervals[i][0] > R ? intervals[i][1] - 1 : R);
            R = intervals[i][1];
        }
        return output;
    }
};