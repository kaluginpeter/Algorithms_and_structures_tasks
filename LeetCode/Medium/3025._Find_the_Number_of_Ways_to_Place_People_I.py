# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].
#
# Count the number of pairs of points (A, B), where
#
# A is on the upper left side of B, and
# there are no other points in the rectangle (or line) they make (including the border).
# Return the count.
#
#
#
# Example 1:
#
# Input: points = [[1,1],[2,2],[3,3]]
#
# Output: 0
#
# Explanation:
#
#
#
# There is no way to choose A and B so A is on the upper left side of B.
#
# Example 2:
#
# Input: points = [[6,2],[4,4],[2,6]]
#
# Output: 2
#
# Explanation:
#
#
#
# The left one is the pair (points[1], points[0]), where points[1] is on the upper left side of points[0] and the rectangle is empty.
# The middle one is the pair (points[2], points[1]), same as the left one it is a valid pair.
# The right one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0], but points[1] is inside the rectangle so it's not a valid pair.
# Example 3:
#
# Input: points = [[3,1],[1,3],[1,1]]
#
# Output: 2
#
# Explanation:
#
#
#
# The left one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0] and there are no other points on the line they form. Note that it is a valid state when the two points form a line.
# The middle one is the pair (points[1], points[2]), it is a valid pair same as the left one.
# The right one is the pair (points[1], points[0]), it is not a valid pair as points[2] is on the border of the rectangle.
#
#
# Constraints:
#
# 2 <= n <= 50
# points[i].length == 2
# 0 <= points[i][0], points[i][1] <= 50
# All points[i] are distinct.
#
# Solution
# Python O(NlogN + N^2) O(1) Sorting Geometry
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: (point[0], -point[1]))
        output: int = 0
        for i in range(len(points)):
            upper_y: int = -1
            for j in range(i + 1, len(points)):
                if points[i][1] < points[j][1] or points[j][1] <= upper_y: continue
                upper_y = max(upper_y, points[j][1])
                output += 1
        return output

# C++ O(NlogN + N^2) O(1) Sorting Geometry
class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int output = 0;
        std::sort(points.begin(), points.end(), [](const std::vector<int> &x, const std::vector<int> &y) {
            if (x[0] != y[0]) return x[0] < y[0];
            return x[1] >= y[1];
        });
        size_t n = points.size();
        for (size_t i = 0; i < n; ++i) {
            int lowerY = -1;
            for (size_t j = i + 1; j < n; ++j) {
                if (points[i][1] < points[j][1]) continue;
                else if (points[j][1] <= lowerY) continue;
                lowerY = std::max(lowerY, points[j][1]);
                ++output;
            }
        }
        return output;
    }
};