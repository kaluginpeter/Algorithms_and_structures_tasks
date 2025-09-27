# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
#
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:
#
# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000
#
#
# Constraints:
#
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.
# Solution
# Python O(N^3) O(1) Math
class Solution:
    def get_area(self, i: int, j: int, k: int, points: list[list[int]]) -> float:
        x1: int = points[i][0] - points[j][0]
        y1: int = points[i][1] - points[j][1]
        x2: int = points[i][0] - points[k][0]
        y2: int = points[i][1] - points[k][1]
        area: float = abs(x1 * y2 - x2 * y1) / 2
        return area

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        output: float = 0.0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    output = max(output, self.get_area(i, j, k, points))
        return output

# C++ O(N^3) O(1) Math
class Solution {
public:
    double getArea(size_t& i, size_t& j, size_t& k, std::vector<std::vector<int>>& points) {
        int x1 = points[i][0] - points[j][0];
        int y1 = points[i][1] - points[j][1];
        int x2 = points[i][0] - points[k][0];
        int y2 = points[i][1] - points[k][1];
        double area = std::abs(x1 * y2 - x2 * y1) / 2.0;
        return area;
    }
    double largestTriangleArea(vector<vector<int>>& points) {
        double output = 0.0;
        for (size_t i = 0; i < points.size() - 2; ++i) {
            for (size_t j = i + 1; j < points.size() - 1; ++j) {
                for (size_t k = j + 1; k < points.size(); ++k) {
                    output = std::max(output, getArea(i, j, k, points));
                }
            }
        }
        return output;
    }
};