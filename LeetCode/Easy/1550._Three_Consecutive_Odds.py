# Given an integer array arr, return true if there are three
# consecutive odd numbers in the array. Otherwise, return false.
#
# Example 1:
#
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:
#
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
#
# Constraints:
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# Solution
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0
        for i in arr:
            if i % 2 != 0:
                c += 1
                if c == 3: return True
            else: c = 0
        return False

# Solution Bitwise Manipulation O(N) O(1)
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        in_a_row: int = 0
        for num in arr:
            if num & 1:
                in_a_row += 1
                if in_a_row == 3: return True
            else: in_a_row = 0
        return False

# Python O(N) O(1) BitManipulation
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if (arr[i] & 1) + (arr[i + 1] & 1) + (arr[i + 2] & 1) == 3: return True
        return False

# C++ O(N) O(1) BitManipulation
class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        for (int i = 0; i < static_cast<int>(arr.size()) - 2; ++i) {
            if ((arr[i] & 1) + (arr[i + 1] & 1) + (arr[i + 2] & 1) == 3) {
                return true;
            }
        }
        return false;
    }
};