# There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.
#
# You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.
#
#
#
# Example 1:
#
#
# Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
#
# Output: 1
#
# Explanation:
#
# A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.
#
# Example 2:
#
#
# Input: bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]
#
# Output: 4
#
# Explanation:
#
# A square with side length 2 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 2 * 2 = 4. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.
#
# Example 3:
#
#
# Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]
#
# Output: 1
#
# Explanation:
#
# A square with side length 1 can fit inside the intersecting region of any two rectangles. Also, no larger square can, so the maximum area is 1. Note that the region can be formed by the intersection of more than 2 rectangles.
#
# Example 4:
#
#
# Input: bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]
#
# Output: 0
#
# Explanation:
#
# No pair of rectangles intersect, hence, the answer is 0.
#
#
#
# Constraints:
#
# n == bottomLeft.length == topRight.length
# 2 <= n <= 103
# bottomLeft[i].length == topRight[i].length == 2
# 1 <= bottomLeft[i][0], bottomLeft[i][1] <= 107
# 1 <= topRight[i][0], topRight[i][1] <= 107
# bottomLeft[i][0] < topRight[i][0]
# bottomLeft[i][1] < topRight[i][1]
# Solution
# Python O(N^2) O(1) Math
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        output: int = 0
        for i in range(len(bottomLeft)):
            fl, fr = bottomLeft[i], topRight[i]
            for j in range(i + 1, len(bottomLeft)):
                sl, sr = bottomLeft[j], topRight[j]
                if sl[0] >= fr[0] or sr[0] <= fl[0]: continue
                elif sr[1] <= fl[1] or sl[1] >= fr[1]: continue
                width: int = min(fr[0], sr[0]) - max(fl[0], sl[0])
                height: int = min(fr[1], sr[1]) - max(fl[1], sl[1])
                output = max(output, min(width, height))
        return output * output

# C++ O(N^2) O(1) Math
class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int output = 0;
        for (size_t i = 0; i < bottomLeft.size(); ++i) {
            std::vector<int> &fl = bottomLeft[i];
            std::vector<int> &fr = topRight[i];
            for (size_t j = i + 1; j < bottomLeft.size(); ++j) {
                std::vector<int> &sl = bottomLeft[j];
                std::vector<int> &sr = topRight[j];
                if (sl[0] >= fr[0] || sr[0] <= fl[0]) continue;
                else if (sr[1] <= fl[1] || sl[1] >= fr[1]) continue;
                int width = std::min(fr[0], sr[0]) - std::max(fl[0], sl[0]);
                int height = std::min(fr[1], sr[1]) - std::max(fl[1], sl[1]);
                output = std::max(output, std::min(width, height));
            }
        }
        return static_cast<long long>(output) * output;
    }
};