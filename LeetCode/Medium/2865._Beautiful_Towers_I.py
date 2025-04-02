# You are given an array heights of n integers representing the number of bricks in n consecutive towers. Your task is to remove some bricks to form a mountain-shaped tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.
#
# Return the maximum possible sum of heights of a mountain-shaped tower arrangement.
#
#
#
# Example 1:
#
# Input: heights = [5,3,4,1,1]
#
# Output: 13
#
# Explanation:
#
# We remove some bricks to make heights = [5,3,3,1,1], the peak is at index 0.
#
# Example 2:
#
# Input: heights = [6,5,3,9,2,7]
#
# Output: 22
#
# Explanation:
#
# We remove some bricks to make heights = [3,3,3,9,2,2], the peak is at index 3.
#
# Example 3:
#
# Input: heights = [3,2,5,5,2,3]
#
# Output: 18
#
# Explanation:
#
# We remove some bricks to make heights = [2,2,5,5,2,2], the peak is at index 2 or 3.
#
#
#
# Constraints:
#
# 1 <= n == heights.length <= 103
# 1 <= heights[i] <= 109
# Solution
# Python O(N) O(N) Monotonic Stack Stack
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n: int = len(heights)
        cur_sum: int = 0
        left_part: list[int] = []
        left_mountain: list[int] = []
        for right in range(n):
            while left_part and heights[left_part[-1]] > heights[right]:
                if len(left_part) > 1:
                    cur_sum -= (left_part[-1] - left_part[-2]) * heights[left_part[-1]]
                else:
                    cur_sum -= (left_part[-1] + 1) * heights[left_part[-1]]
                left_part.pop()
            if left_part:
                cur_sum += (right - left_part[-1]) * heights[right]
            else:
                cur_sum += (right + 1) * heights[right]
            left_part.append(right)
            left_mountain.append(cur_sum)

        max_sum: int = 0
        cur_sum = 0
        right_part: list[int] = []
        for left in range(n - 1, -1, -1):
            max_sum = max(max_sum, left_mountain[left] + cur_sum)
            while right_part and heights[right_part[-1]] > heights[left]:
                if len(right_part) > 1:
                    cur_sum -= (right_part[-2] - right_part[-1]) * heights[right_part[-1]]
                else:
                    cur_sum -= (n - right_part[-1]) * heights[right_part[-1]]
                right_part.pop()
            if right_part:
                cur_sum += (right_part[-1] - left) * heights[left]
            else:
                cur_sum += (n - left) * heights[left]
            right_part.append(left)
        return max_sum

# C++ O(N) O(N) MonotonicStack Stack
class Solution {
public:
    long long maximumSumOfHeights(vector<int>& heights) {
        long long maxSum = 0, curSum = 0;
        vector<int> leftPart;
        vector<long long> leftMountain;
        int n = heights.size();
        for (int right = 0; right < n; ++right) {
            while (!leftPart.empty() && heights[leftPart.back()] > heights[right]) {
                if (leftPart.size() > 1) {
                    curSum -= (leftPart.back() - leftPart[leftPart.size() - 2]) * static_cast<long long>(heights[leftPart.back()]);
                } else {
                    curSum -= heights[leftPart.back()] * static_cast<long long>(leftPart.back() + 1);
                }
                leftPart.pop_back();
            }
            if (!leftPart.empty()) {
                curSum += heights[right] * static_cast<long long>(right - leftPart.back());
            } else {
                curSum += heights[right] * static_cast<long long>(right + 1);
            }
            leftPart.push_back(right);
            leftMountain.push_back(curSum);
        }
        curSum = 0;
        vector<int> rightPart;
        for (int left = n - 1; left >= 0; --left) {
            maxSum = max(maxSum, leftMountain[left] + curSum);
            while (!rightPart.empty() && heights[rightPart.back()] > heights[left]) {
                if (rightPart.size() > 1) {
                    curSum -= (rightPart[rightPart.size() - 2] - rightPart.back()) * static_cast<long long>(heights[rightPart.back()]);
                } else {
                    curSum -= (n - rightPart.back()) * static_cast<long long>(heights[rightPart.back()]);
                }
                rightPart.pop_back();
            }
            if (!rightPart.empty()) {
                curSum += (rightPart.back() - left) * static_cast<long long>(heights[left]);
            } else {
                curSum += (n - left) * static_cast<long long>(heights[left]);
            }
            rightPart.push_back(left);
        }
        return maxSum;
    }
};