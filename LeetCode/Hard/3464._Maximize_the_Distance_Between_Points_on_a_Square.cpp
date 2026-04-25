/*
You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.

You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.

Return the maximum possible minimum Manhattan distance between the selected k points.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.



Example 1:

Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4

Output: 2

Explanation:



Select all four points.

Example 2:

Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4

Output: 1

Explanation:



Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

Example 3:

Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5

Output: 1

Explanation:



Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).



Constraints:

1 <= side <= 109
4 <= points.length <= min(4 * side, 15 * 103)
points[i] == [xi, yi]
The input is generated such that:
points[i] lies on the boundary of the square.
All points[i] are unique.
4 <= k <= min(25, points.length)
*/
// Solution
// C++ Sorting BinarySearch O(NKlogMlogN) O(N)
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        std::vector<long long> arr;
        for (auto& p : points) {
            int x = p[0], y = p[1];
            if (!x) arr.push_back(y);
            else if (y == side) arr.push_back(side + x);
            else if (x == side) arr.push_back(side * 3LL - y);
            else arr.push_back(side * 4LL - x);
        }
        std::sort(arr.begin(), arr.end());
        auto check = [&](long long limit) -> bool {
            for (long long start : arr) {
                long long end = start + side * 4LL - limit;
                long long cur = start;
                for (int i = 0; i < k - 1; i++) {
                    auto it = ranges::lower_bound(arr, cur + limit);
                    if (it == arr.end() || *it > end) {
                        cur = -1;
                        break;
                    }
                    cur = *it;
                }
                if (cur >= 0) return true;
            }
            return false;
        };
        long long left = 1, right = side;
        int output = 0;
        while (left <= right) {
            long long mid = left + ((right - left) >> 1);
            if (check(mid)) {
                left = mid + 1;
                output = mid;
            } else right = mid - 1;
        }
        return output;
    }
};