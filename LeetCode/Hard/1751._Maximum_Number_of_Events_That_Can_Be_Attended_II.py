# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
#
# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
#
# Return the maximum sum of values that you can receive by attending events.
#
#
#
# Example 1:
#
#
#
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
# Example 2:
#
#
#
# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# Output: 10
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
# Example 3:
#
#
#
# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# Output: 9
# Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
#
#
# Constraints:
#
# 1 <= k <= events.length
# 1 <= k * events.length <= 106
# 1 <= startDayi <= endDayi <= 109
# 1 <= valuei <= 106
# Solution
# Python O(KNlogN) O(KN) DynamicPrograming Sorting BinarySearch
class Solution:
    def get_leftmost_event(self, start: int, events: list[list[int]]) -> int:
        left: int = 0
        right: int = len(events) - 1
        output: int = -1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if events[middle][1] >= start:
                right = middle - 1
            else:
                output = middle
                left = middle + 1
        return output

    def maxValue(self, events: List[List[int]], k: int) -> int:
        n: int = len(events)
        dp: list[list[int]] = [[0] * (n + 1) for _ in range(k + 1)]
        events.sort(key=lambda event: (event[1], event[0]))
        for i in range(1, k + 1):
            for event in range(1, n + 1):
                dp[i][event] = dp[i - 1][event]
                leftmost_event: int = self.get_leftmost_event(events[event - 1][0], events)
                dp[i][event] = max(
                    dp[i][event - 1],
                    events[event - 1][2] + [dp[i - 1][leftmost_event + 1], 0][leftmost_event == -1]
                )
        return dp[k][n]

# C++ O(KNlogN) O(KN) DynamicProgramming BinarySearch Sorting
class Solution {
public:
    int getLeftmostEvent(int&start, std::vector<std::vector<int>> &events) {
        int left = 0, right = events.size() - 1;
        int output = -1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (events[middle][1] >= start) right = middle - 1;
            else {
                output = middle;
                left = middle + 1;
            }
        }
        return output;
    }

    int maxValue(vector<vector<int>>& events, int k) {
        int n = events.size();
        std::sort(events.begin(), events.end(), [](const std::vector<int> &x, const std::vector<int> &y){
            if (x[1] != y[1]) return x[1] < y[1];
            return x[0] < y[0];
        });
        std::vector<std::vector<int>> dp(k + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= k; ++i) {
            for (int event = 1; event <= n; ++event) {
                dp[i][event] = dp[i - 1][event];
                int leftMostEvent = getLeftmostEvent(events[event - 1][0], events);
                dp[i][event] = std::max(
                    dp[i][event - 1], // previous move
                    events[event - 1][2] + (leftMostEvent == -1 ? 0 : dp[i - 1][leftMostEvent + 1]) // current move
                );
            }
        }
        return dp[k][n];
    }
};