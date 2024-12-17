# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
#
#
#
# Example 1:
#
#
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:
#
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
#
#
# Constraints:
#
# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104
# Solution
# Python O(NlogN) O(N) Priority Queue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap: list[tuple[float, int, int]] = []
        for point in points:
            x, y = point
            heapq.heappush(min_heap, ((x**2 + y**2)**.5, x, y))
        output: list[list[int, int]] = []
        for _ in range(k):
            dist, x, y = heapq.heappop(min_heap)
            output.append([x, y])
        return output

# C++ O(NlogN) O(N) Priority Queue
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        std::priority_queue<std::pair<double, int>, std::vector<std::pair<double, int>>, std::greater<std::pair<double, int>>> minHeap;
        for (int idx = 0; idx < points.size(); ++idx) {
            std::vector<int>& point = points[idx];
            double x = static_cast<double>(point[0]);
            double y = static_cast<double>(point[1]);
            double dist = std::sqrt(std::pow(x, 2) + std::pow(y, 2));
            minHeap.push({dist, idx});
        }
        std::vector<std::vector<int>> output;
        for (int i = 0; i < k; ++i) {
            output.push_back(points[minHeap.top().second]);
            minHeap.pop();
        }
        return output;
    }
};