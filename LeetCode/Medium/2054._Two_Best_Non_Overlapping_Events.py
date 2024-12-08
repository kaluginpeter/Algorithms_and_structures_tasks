# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.
#
# Return this maximum sum.
#
# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.
#
#
#
# Example 1:
#
#
# Input: events = [[1,3,2],[4,5,2],[2,4,3]]
# Output: 4
# Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
# Example 2:
#
# Example 1 Diagram
# Input: events = [[1,3,2],[4,5,2],[1,5,5]]
# Output: 5
# Explanation: Choose event 2 for a sum of 5.
# Example 3:
#
#
# Input: events = [[1,5,3],[1,5,1],[6,6,5]]
# Output: 8
# Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
#
#
# Constraints:
#
# 2 <= events.length <= 105
# events[i].length == 3
# 1 <= startTimei <= endTimei <= 109
# 1 <= valuei <= 106
# Solution
# Python O(NlogN) O(N) Binary Search Sorting
class Solution:
    def binary_search(self, start_time: int, times: list[list[int, int]]) -> int:
        """
        Search most profit event comes before given start_time otherwise return 0
        """
        left: int = 0
        right: int = len(times) - 1
        max_score: int = 0
        while left <= right:
            middle: int = left + (right - left) // 2
            if times[middle][0] < start_time:
                max_score = max(max_score, times[middle][1])
                left = middle + 1
            else:
                right = middle - 1
        return max_score

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort by end_time in ascending order: x0 <= x1 <= ... <= xn
        events.sort(key=lambda event: event[1])
        # Store list of <end_time, score>
        times: list[list[int, int]] = []
        local_max_score: int = 0
        prev_end_time: int = 0
        for event in events:
            start_time, end_time, score = event
            local_max_score = max(local_max_score, score)
            if prev_end_time == end_time: # Path compression
                times[-1][1] = local_max_score
            else:
                times.append([end_time, local_max_score])
            prev_end_time = end_time
        max_score: int = 0
        for event in events:
            start_time, end_time, score = event
            max_score = max(max_score, score + self.binary_search(start_time, times))
        return max_score

# C++ O(NlogN) O(N) Binary Search Sorting
class Solution {
public:
    int binarySearch(int& startTime, std::vector<std::pair<int, int>>& times) {
        /*
        Search most profit event comes before given startTime otherwise return 0
        */
        int left = 0;
        int right = times.size() - 1;
        int maxAdditionalTime = 0;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (times[middle].first < startTime) {
                maxAdditionalTime = std::max(maxAdditionalTime, times[middle].second);
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return maxAdditionalTime;
    }
    int maxTwoEvents(vector<vector<int>>& events) {
        // Sort by endTime in ascending order: x1 <= x2 <= ... <= xn
        std::sort(
            events.begin(), events.end(),
            [](const std::vector<int>& a, const std::vector<int>& b){
                return a[1] < b[1];
            }
        );
        int localMaxScore = 0;
        // Stores vector of <endTime, score>
        std::vector<std::pair<int, int>> times;
        int prevEndTime = 0;
        for (std::vector<int>& event : events) {
            int endTime = event[1];
            int currentScore = event[2];
            localMaxScore = std::max(localMaxScore, currentScore);
            if (prevEndTime == endTime) { // Path compression
                times[times.size() - 1].second = localMaxScore;
            } else {
                times.push_back({endTime, localMaxScore});
            }
            prevEndTime = endTime;
        }
        int maxScore = 0;
        for (std::vector<int>& event : events) {
            int startTime = event[0];
            int score = event[2];
            maxScore = std::max(maxScore, score + binarySearch(startTime, times));
        }
        return maxScore;
    }
};