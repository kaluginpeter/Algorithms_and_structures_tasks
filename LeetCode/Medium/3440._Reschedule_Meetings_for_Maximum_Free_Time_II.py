# You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.
#
# These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].
#
# You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.
#
# Return the maximum amount of free time possible after rearranging the meetings.
#
# Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.
#
# Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.
#
#
#
# Example 1:
#
# Input: eventTime = 5, startTime = [1,3], endTime = [2,5]
#
# Output: 2
#
# Explanation:
#
#
#
# Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].
#
# Example 2:
#
# Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]
#
# Output: 7
#
# Explanation:
#
#
#
# Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].
#
# Example 3:
#
# Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]
#
# Output: 6
#
# Explanation:
#
#
#
# Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].
#
# Example 4:
#
# Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
#
# Output: 0
#
# Explanation:
#
# There is no time during the event not occupied by meetings.
#
#
#
# Constraints:
#
# 1 <= eventTime <= 109
# n == startTime.length == endTime.length
# 2 <= n <= 105
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
# Solution
# Python O(N) O(N) Prefix Suffix Array
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n: int = len(startTime)
        segments: list[int] = [startTime[0]]
        prefix_segments: list[int] = [startTime[0]]
        for i in range(n - 1):
            segments.append(startTime[i + 1] - endTime[i])
            prefix_segments.append(max(prefix_segments[-1], startTime[i + 1] - endTime[i]))
        segments.append(eventTime - endTime[-1])
        prefix_segments.append(max(prefix_segments[-1], eventTime - endTime[-1]))

        suffix_segments: list[int] = [0] * (n + 2)
        suffix_segments[n + 1] = eventTime - endTime[-1]
        for i in range(n - 1, 0, -1):
            suffix_segments[i + 1] = max(suffix_segments[i + 2], startTime[i] - endTime[i - 1])
        suffix_segments[0] = max(startTime[0], suffix_segments[1])

        output: int = 0
        for i in range(1, n + 1):
            event_length: int = endTime[i - 1] - startTime[i - 1]
            extra_space: int = segments[i - 1] + segments[i]
            if max(
                    prefix_segments[i - 2] if i - 2 >= 0 else 0,
                    suffix_segments[i + 2] if i + 2 < n + 2 else 0
            ) >= event_length: extra_space += event_length
            output = max(output, extra_space)
        return output

# C++ O(N) O(N) Prefix Suffix Array
class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        std::vector<int> prefixSegments, segments;
        prefixSegments.push_back(startTime[0]);
        segments.push_back(startTime[0]);
        for (int i = 0; i < n - 1; ++i) {
            prefixSegments.push_back(std::max(prefixSegments.back(), startTime[i + 1] - endTime[i]));
            segments.push_back(startTime[i + 1] - endTime[i]);
        }
        prefixSegments.push_back(std::max(prefixSegments.back(), eventTime - endTime.back()));
        segments.push_back(eventTime - endTime.back());

        std::vector<int> suffixSegments(n + 2, 0);
        suffixSegments[n + 1] = eventTime - endTime.back();
        for (int i = n - 1; i > 0; --i) {
            suffixSegments[i + 1] = std::max(suffixSegments[i + 2], startTime[i] - endTime[i - 1]);
        }
        suffixSegments[0] = std::max(suffixSegments[1], startTime[0]);
        int output = 0;
        for (int i = 1; i <= n; ++i) {
            int currentEventLength = endTime[i - 1] - startTime[i - 1];
            int extraSpace = segments[i - 1] + segments[i];
            if (std::max(
                (i - 2 >= 0 ? prefixSegments[i - 2] : 0),
                (i + 2 <= n + 1 ? suffixSegments[i + 2] : 0)
            ) >= currentEventLength) extraSpace += currentEventLength;
            output = std::max(output, extraSpace);
        }
        return output;
    }
};