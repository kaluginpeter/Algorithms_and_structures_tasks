# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
#
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
#
# Return the minimum time Bob needs to make the rope colorful.
#
#
#
# Example 1:
#
#
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.
# Example 2:
#
#
# Input: colors = "abc", neededTime = [1,2,3]
# Output: 0
# Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.
# Example 3:
#
#
# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
#
#
# Constraints:
#
# n == colors.length == neededTime.length
# 1 <= n <= 105
# 1 <= neededTime[i] <= 104
# colors contains only lowercase English letters.
# Solution 1 - O(N) O(1)
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
        count, s, top = 0, 0, 0
        for i in range(1, len(colors)):
            s += neededTime[i-1]
            top = max(top, neededTime[i-1])
            if colors[i-1] != colors[i]:
                count += s - top
                s, top = 0, 0
        if colors[-2] == colors[-1]:
            s += neededTime[-1]
            top = max(top, neededTime[-1])
            count += s - top
        return count
# Solution 2 - O(N) O(1) But shorter than solution above
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        sm, mx = 0, 0
        for i in range(len(colors)):
            if colors[i-1] != colors[i]:
                mx = 0
            sm += min(mx, neededTime[i])
            mx = max(mx, neededTime[i])
        return sm


# Python O(N) O(1) Greedy
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        output: int = 0
        prev: int = 0
        for i in range(1, len(colors)):
            if colors[i] != colors[prev]: prev = i
            elif neededTime[i] <= neededTime[prev]: output += neededTime[i]
            else:
                output += neededTime[prev]
                prev = i
        return output

# C++ O(N) O(1) Greedy
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int output = 0, prev = 0;
        for (size_t i = 1; i < colors.size(); ++i) {
            if (colors[i] != colors[prev]) prev = i;
            else if (neededTime[prev] <= neededTime[i]) {
                output += neededTime[prev];
                prev = i;
            }
            else output += neededTime[i];
        }
        return output;
    }
};