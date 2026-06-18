# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
#
# Answers within 10-5 of the actual value will be accepted as correct.
#
#
#
# Example 1:
#
#
# Input: hour = 12, minutes = 30
# Output: 165
# Example 2:
#
#
# Input: hour = 3, minutes = 30
# Output: 75
# Example 3:
#
#
# Input: hour = 3, minutes = 15
# Output: 7.5
#
#
# Constraints:
#
# 1 <= hour <= 12
# 0 <= minutes <= 59
# Solution
# Python O(1) O(1) Math
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        return min((diff:=(11 * (hour + minutes / 60)) % 12), 12 - diff) * 30

# C++ O(1) O(1) Math
class Solution {
public:
    double angleClock(int hour, int minutes) {
        double x = hour + minutes / 60.0;
        double diff = std::fmod(11.0 * x, 12.0);
        return std::min(diff, 12.0 - diff) * 30.0;
    }
};