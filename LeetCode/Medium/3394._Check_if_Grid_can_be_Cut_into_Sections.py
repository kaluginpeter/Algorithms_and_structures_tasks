# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:
#
# (startx, starty): The bottom-left corner of the rectangle.
# (endx, endy): The top-right corner of the rectangle.
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:
#
# Each of the three resulting sections formed by the cuts contains at least one rectangle.
# Every rectangle belongs to exactly one section.
# Return true if such cuts can be made; otherwise, return false.
#
#
#
# Example 1:
#
# Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
#
# Output: true
#
# Explanation:
#
#
#
# The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.
#
# Example 2:
#
# Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
#
# Output: true
#
# Explanation:
#
#
#
# We can make vertical cuts at x = 2 and x = 3. Hence, output is true.
#
# Example 3:
#
# Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
#
# Output: false
#
# Explanation:
#
# We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.
#
#
#
# Constraints:
#
# 3 <= n <= 109
# 3 <= rectangles.length <= 105
# 0 <= rectangles[i][0] < rectangles[i][2] <= n
# 0 <= rectangles[i][1] < rectangles[i][3] <= n
# No two rectangles overlap.
# Solution
# Python O(NlogN) O(N) Monotonic Stack Sorting
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort(key=lambda rect: rect[2])  # Sort by end of x axis
        x_axis: list[list[int]] = []
        for rect in rectangles:
            while x_axis and rect[0] < x_axis[-1][2]:
                x_axis.pop()
            x_axis.append(rect)

        rectangles.sort(key=lambda rect: rect[3])  # Sort by end of y axis
        y_axis: list[list[int]] = []
        for rect in rectangles:
            while y_axis and rect[1] < y_axis[-1][3]:
                y_axis.pop()
            y_axis.append(rect)

        return len(x_axis) >= 3 or len(y_axis) >= 3

# C++ O(NlogN) O(N) Monotonic Stack Sorting
class Solution {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        std::sort(rectangles.begin(), rectangles.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[2] < b[2];
        }); // Sort by end of x axis
        std::vector<int> xAxis;
        for (std::vector<int>& rectangle : rectangles) {
            while (xAxis.size() && rectangle[0] < xAxis[xAxis.size() - 1]) {
                xAxis.pop_back();
            }
            xAxis.push_back(rectangle[2]);
        }
        std::sort(rectangles.begin(), rectangles.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[3] < b[3];
        }); // Sort by end of y axis
        std::vector<int> yAxis;
        for (std::vector<int>& rectangle : rectangles) {
            while (yAxis.size() && rectangle[1] < yAxis[yAxis.size() - 1]) {
                yAxis.pop_back();
            }
            yAxis.push_back(rectangle[3]);
        }
        return xAxis.size() >= 3 || yAxis.size() >= 3;
    }
};

# Python O(NlogN) O(1) Array Sorting
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort()
        vertical_cuts: int = 0
        prev_end: int = rectangles[0][2]
        for i in range(1, len(rectangles)):
            if rectangles[i][0] >= prev_end:
                vertical_cuts += 1
            prev_end = max(prev_end, rectangles[i][2])
        if vertical_cuts >= 2: return True
        rectangles.sort(key=lambda x: (x[1], x[3]))
        prev_end = rectangles[0][3]
        horizontal_cuts: int = 0
        for i in range(1, len(rectangles)):
            if rectangles[i][1] >= prev_end:
                horizontal_cuts += 1
            prev_end = max(prev_end, rectangles[i][3])
        return horizontal_cuts >= 2

# C++ O(NlogN) O(1) Array Sorting Greedy
class Solution {
public:
    static bool horizontalComp(const vector<int>& left, const vector<int>& right) {
        if (left[1] != right[1]) return left[1] < right[1];
        return left[3] < right[3];
    }
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        std::sort(rectangles.begin(), rectangles.end());
        int verticalCuts = 0;
        int prevEnd = rectangles[0][2];
        for (int i = 1; i < rectangles.size(); ++i) {
            if (rectangles[i][0] >= prevEnd) ++verticalCuts;
            prevEnd = std::max(prevEnd, rectangles[i][2]);
        }
        if (verticalCuts >= 2) return true;
        std::sort(rectangles.begin(), rectangles.end(), horizontalComp);
        int horizontalCuts = 0;
        prevEnd = rectangles[0][3];
        for (int i = 1; i < rectangles.size(); ++i) {
            if (rectangles[i][1] >= prevEnd) ++horizontalCuts;
            prevEnd = std::max(prevEnd, rectangles[i][3]);
        }
        return horizontalCuts >= 2;
    }
};