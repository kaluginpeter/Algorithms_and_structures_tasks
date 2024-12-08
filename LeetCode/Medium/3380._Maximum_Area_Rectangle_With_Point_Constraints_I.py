# You are given an array points where points[i] = [xi, yi] represents the coordinates of a point on an infinite plane.
#
# Your task is to find the maximum area of a rectangle that:
#
# Can be formed using four of these points as its corners.
# Does not contain any other point inside or on its border.
# Has its edges parallel to the axes.
# Return the maximum area that you can obtain or -1 if no such rectangle is possible.
#
#
#
# Example 1:
#
# Input: points = [[1,1],[1,3],[3,1],[3,3]]
#
# Output: 4
#
# Explanation:
#
# Example 1 diagram
#
# We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.
#
# Example 2:
#
# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
#
# Output: -1
#
# Explanation:
#
# Example 2 diagram
#
# There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1.
#
# Example 3:
#
# Input: points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
#
# Output: 2
#
# Explanation:
#
# Example 3 diagram
#
# The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3], which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area.
#
#
#
# Constraints:
#
# 1 <= points.length <= 10
# points[i].length == 2
# 0 <= xi, yi <= 100
# All the given points are unique.
# Solution
# C++ O(N**5) O(1) Simulation
class Solution {
public:
    bool check(int& ll, int& lr, int& ul, int& ur, std::vector<std::vector<int>>& points) {
        for (int idx = 0; idx < points.size(); ++idx) {
            if (idx == ll || idx == lr || idx == ul || idx == ur) continue;
            int& x = points[idx][0];
            int& y = points[idx][1];
            if (x >= points[ll][0] && x <= points[lr][0] && y <= points[ul][1] && y >= points[ll][1]) {
                return false;
            }
        }
        return true;
    }
    int maxRectangleArea(vector<vector<int>>& points) {
        int maxArea = -1;
        int n = points.size();
        int ll, lr, ul, ur;
        for (ll = 0; ll < n; ++ll) {
            for (lr = 0; lr < n; ++lr) {
                if (lr == ll) continue;
                for (ul = 0; ul < n; ++ul) {
                    if (ul == ll || ul == lr) continue;
                    for (ur = 0; ur < n; ++ur) {
                        if (ur == ll || ur == lr || ur == ul) continue;
                        if (
                            points[ll][1] == points[lr][1] // same y-axis for lower points
                            && points[ul][1] == points[ur][1] // same y-axis for upper points
                            && points[ll][0] == points[ul][0] // same x-asis for lower points
                            && points[lr][0] == points[ur][0] // same x-asis for right points
                            && points[ll][0] <= points[lr][0] // left point comes before right point
                            && check(ll, lr, ul, ur, points) // not points lays inside rectangle
                            ) {
                                std::cout << ll << " " << lr << " " << ul << " " << ur << "\n";
                            maxArea = std::max(maxArea, (points[lr][0] - points[ll][0]) * (points[ul][1] - points[ll][1]));
                        }
                    }
                }
            }
        }
        return maxArea;
    }
};

# Python O(N**5) O(1) Simulation
class Solution:
    def check(self, a: int, b: int, c: int, d: int, points: list[list[int]]) -> bool:
        for f in points:
            if f in (a, b, c, d):
                continue
            elif (a[0] <= f[0] <= b[0]) and (c[1] >= f[1] and f[1] >= a[1]):
                return False
        return True

    def maxRectangleArea(self, points: List[List[int]]) -> int:
        max_area: int = -1
        n: int = len(points)
        for lower_left in range(n):
            for lower_right in range(n):
                if lower_right == lower_left: continue
                for upper_left in range(n):
                    if upper_left in (lower_left, lower_right): continue
                    for upper_right in range(n):
                        if upper_right in (upper_left, lower_right, lower_left): continue
                        a, b, c, d = points[lower_left], points[lower_right], points[upper_left], points[upper_right]
                        if a[1] == b[1] and a[0] < b[0] and c[1] == d[1] and a[0] == c[0] and b[0] == d[0]:
                            if self.check(a, b, c, d, points):
                                max_area = max(max_area, (b[0] - a[0]) * (c[1] - a[1]))
        return max_area