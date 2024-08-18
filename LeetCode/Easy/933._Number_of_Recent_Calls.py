# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
#
# Implement the RecentCounter class:
#
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
#
#
#
# Example 1:
#
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]
#
# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
#
#
# Constraints:
#
# 1 <= t <= 109
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.
# Solution

# Binary Search
# Complexity
# Time complexity: O(NlogN)
# Space complexity: O(N)
# Code
class RecentCounter:
    def __init__(self):
        self.requests: list[int] = []

    def leftmost_binary_search(self, target: int) -> int:
        left: int = 0
        right: int = len(self.requests)
        while left <= right:
            middle: int = left + (right - left) // 2
            if self.requests[middle] >= target:
                right = middle - 1
            else: left = middle + 1
        return right + 1

    def ping(self, t: int) -> int:
        self.requests.append(t)
        lower_idx: int = self.leftmost_binary_search(t - 3_000)
        return len(self.requests) - lower_idx



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Two pointers aka Sliding Window
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)
# Code
class RecentCounter:
    def __init__(self):
        self.requests: list[int] = []
        self.left: int = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.left] < t - 3_000:
            self.left += 1
        return len(self.requests) - self.left



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)