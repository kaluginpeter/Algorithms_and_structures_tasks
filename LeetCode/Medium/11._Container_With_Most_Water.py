# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
# Solution Two Pointers O(N) O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans: int = 0
        left, right = 0, len(height) - 1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

# Python O(N) O(1) Two Pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans: int = 0
        left, right = 0, len(height) - 1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

# C++ O(N) O(1) Two Pointers
class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_volume = 0;
        int left = 0;
        int right = height.size() - 1;
        while (left < right) {
            int current_volume = (right - left) * std::min(height[left], height[right]);
            max_volume = std::max(max_volume, current_volume);
            if (height[left] <= height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return max_volume;
    }
};