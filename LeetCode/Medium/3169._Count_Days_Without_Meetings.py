# You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
#
# Return the count of days when the employee is available for work but no meetings are scheduled.
#
# Note: The meetings may overlap.
#
#
#
# Example 1:
#
# Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
#
# Output: 2
#
# Explanation:
#
# There is no meeting scheduled on the 4th and 8th days.
#
# Example 2:
#
# Input: days = 5, meetings = [[2,4],[1,3]]
#
# Output: 1
#
# Explanation:
#
# There is no meeting scheduled on the 5th day.
#
# Example 3:
#
# Input: days = 6, meetings = [[1,6]]
#
# Output: 0
#
# Explanation:
#
# Meetings are scheduled for all working days.
#
#
#
# Constraints:
#
# 1 <= days <= 109
# 1 <= meetings.length <= 105
# meetings[i].length == 2
# 1 <= meetings[i][0] <= meetings[i][1] <= days
# Solution Sorting Two Pointers O(NlogN) O(1)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], -x[1]))
        start, end = meetings[0]
        for i in range(1, len(meetings)):
            if meetings[i][0] <= end:
                end = max(end, meetings[i][1])
            else:
                days -= end - start + 1
                start, end = meetings[i]
        days -= end - start + 1
        return days

# Python O(NlogN) O(1) Sorting
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        output: int = 0
        prev_end: int = 0
        for start, end in meetings:
            if start > prev_end:
                output += start - prev_end - 1
                prev_end = end
            else: prev_end = max(prev_end, end)
        if days - prev_end: output += days - prev_end
        return output

# C++ O(NlogN) O(1) Sorting
class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        int prevEnd = 0;
        int output = 0;
        for (vector<int>& meeting : meetings) {
            if (meeting[0] > prevEnd) {
                output += meeting[0] - prevEnd - 1;
                prevEnd = meeting[1];
            } else prevEnd = max(prevEnd, meeting[1]);
        }
        if (days - prevEnd > 0) output += days - prevEnd;
        return output;

    }
};