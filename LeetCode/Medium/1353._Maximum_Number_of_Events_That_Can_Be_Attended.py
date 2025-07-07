# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
#
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
#
# Return the maximum number of events you can attend.
#
#
#
# Example 1:
#
#
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# Example 2:
#
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
#
#
# Constraints:
#
# 1 <= events.length <= 105
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 105
# Solution
# Python O(N + T + NlogN) O(N) PriorityQueue SweepLine
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        min_heap: list[int] = []
        events.sort()
        i: int = 0
        n: int = len(events)
        min_heap: list[int] = []
        max_day: int = max(event[1] for event in events)
        attended: int = 0
        for day in range(max_day + 1):
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            if min_heap:
                attended += 1
                heapq.heappop(min_heap)
            while min_heap and min_heap[0] <= day: heapq.heappop(min_heap)
        return attended

# C++ O(N + T + NlogN) O(N) PriorityQueue SweepLine
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
        int maxDay = 0;
        for (std::vector<int> &event : events) {
            maxDay = std::max(maxDay, event[1]);
        }
        std::sort(events.begin(), events.end());
        int attended = 0, i = 0, n = events.size();
        for (int day = 0; day <= maxDay; ++day) {
            while (i < n && events[i][0] <= day) {
                minHeap.push(events[i][1]);
                ++i;
            }
            if (!minHeap.empty()) {
                ++attended;
                minHeap.pop();
            }
            while (!minHeap.empty() && minHeap.top() <= day) minHeap.pop();
        }
        return attended;
    }
};