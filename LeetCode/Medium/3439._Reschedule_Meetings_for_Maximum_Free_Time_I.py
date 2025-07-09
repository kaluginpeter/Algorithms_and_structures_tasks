# You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.
#
# You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].
#
# You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
#
# The relative order of all the meetings should stay the same and they should remain non-overlapping.
#
# Return the maximum amount of free time possible after rearranging the meetings.
#
# Note that the meetings can not be rescheduled to a time outside the event.
#
#
#
# Example 1:
#
# Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
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
# Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]
#
# Output: 6
#
# Explanation:
#
#
#
# Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].
#
# Example 3:
#
# Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
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
# 1 <= k <= n
# 0 <= startTime[i] < endTime[i] <= eventTime
# endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
# Solution
# Python O(N + K) O(N) SlidingWindow
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n: int = len(startTime)
        segments: list[int] = []
        segments.append(startTime[0])
        for i in range(n - 1):
            segments.append(startTime[i + 1] - endTime[i])
        segments.append(eventTime - endTime[-1])
        output: int = 0
        window_sum: int = 0
        for i in range(k): window_sum += segments[i]
        for i in range(k, n + 1):
            if i > k: window_sum -= segments[i - k - 1]
            window_sum += segments[i]
            output = max(output, window_sum)
        return output

# C++ O(N + K) O(N) SlidingWindow
class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        std::vector<int> segments;
        segments.push_back(startTime[0] - 0);
        for (int i = 0; i < n - 1; ++i) {
            segments.push_back(startTime[i + 1] - endTime[i]);
        }
        segments.push_back(eventTime - endTime.back());
        int output = 0, windowSum = 0;
        for (int i = 0; i < k; ++i) windowSum += segments[i];
        for (int i = k; i < segments.size(); ++i) {
            if (i > k) windowSum -= segments[i - k - 1];
            windowSum += segments[i];
            output = std::max(output, windowSum);
        }
        return output;
    }
};