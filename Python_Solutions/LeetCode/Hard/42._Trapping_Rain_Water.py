# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105
# Solution Two Pointers O(N) O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans: int = 0
        idx_mx: int = 0
        for i in range(len(height)):
            if height[i] > height[idx_mx]:
                idx_mx = i
        left, right = 0, idx_mx
        left_boundary, right_boundary = 0, height[idx_mx]
        while left <= right:
            if left_boundary < height[left]:
                left_boundary = height[left]
            ans += min(left_boundary, right_boundary) - height[left]
            left += 1
        right = len(height) - 1
        right_boundary = height[right]
        while right >= left:
            if right_boundary < height[right]:
                right_boundary = height[right]
            ans += min(left_boundary, right_boundary) - height[right]
            right += -1
        return ans