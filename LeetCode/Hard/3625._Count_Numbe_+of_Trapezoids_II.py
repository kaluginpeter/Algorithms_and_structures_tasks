# You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.
#
# Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.
#
# A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.
#
#
#
# Example 1:
#
# Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
#
# Output: 2
#
# Explanation:
#
#
#
# There are two distinct ways to pick four points that form a trapezoid:
#
# The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
# The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
# Example 2:
#
# Input: points = [[0,0],[1,0],[0,1],[2,1]]
#
# Output: 1
#
# Explanation:
#
#
#
# There is only one trapezoid which can be formed.
#
#
#
# Constraints:
#
# 4 <= points.length <= 500
# –1000 <= xi, yi <= 1000
# All points are pairwise distinct.
# Solution
# Python O(N^2) O(D) Geometry
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod: int = 10**9 + 7
        n: int = len(points)
        output: int = 0
        slope_to_intercept: dict[float, list[float]] = defaultdict(list)
        mid_to_slope: dict[int, list[int]] = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx: int = x1 - x2
                dy: int = y1 - y2
                k: int = ((y2 - y1) / (x2 - x1)) if x1 != x2 else mod
                b: int = ((y1 * dx - x1 * dy) / dx) if x1 != x2 else x1
                mid: int = (x1 + x2) * 10_000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)
        for _, sti in slope_to_intercept.items():
            if len(sti) == 1: continue
            cnt: dict[int, int] = defaultdict(int)
            for b in sti: cnt[b] += 1
            total: int = 0
            for b, freq in cnt.items():
                output += total * freq
                total += freq
        for mid, mts in mid_to_slope.items():
            if len(mts) == 1: continue
            cnt: dict[int, int] = defaultdict(int)
            for k in mts: cnt[k] += 1
            total: int = 0
            for k, freq in cnt.items():
                output -= total * freq
                total += freq
        return output

# C++ O(N^2) O(D) Geometry
constexpr int inf = 1000000007;
class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size(), output = 0;
        std::unordered_map<float, std::vector<float>> slopeToIntercept;
        std::unordered_map<int, std::vector<float>> midToSlope;
        for (int i = 0; i < n; ++i) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                int dx = x1 - x2;
                int dy = y1 - y2;
                float k, b;
                if (x2 == x1) {
                    k = inf;
                    b = x1;
                } else {
                    k = 1.0 * (y2 - y1) / (x2 - x1);
                    b = 1.0 * (y1 * dx - x1 * dy) / dx;
                }
                int mid = (x1 + x2) * 10000 + (y1 + y2);
                slopeToIntercept[k].push_back(b);
                midToSlope[mid].push_back(k);
            }
        }
        for (auto& [_, sti] : slopeToIntercept) {
            if (sti.size() == 1) continue;
            std::unordered_map<float, int> cnt;
            for (float b : sti) ++cnt[b];
            int sum = 0;
            for (auto& [_, count] : cnt) {
                output += sum * count;
                sum += count;
            }
        }
        for (auto& [_, mts] : midToSlope) {
            if (mts.size() == 1) continue;
            std::unordered_map<float, int> cnt;
            for (float k : mts) ++cnt[k];
            int sum = 0;
            for (auto& [_, count] : cnt) {
                output -= sum * count;
                sum += count;
            }
        }
        return output;
    }
};