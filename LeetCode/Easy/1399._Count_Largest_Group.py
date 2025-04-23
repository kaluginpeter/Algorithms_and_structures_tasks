# You are given an integer n.
#
# Each number from 1 to n is grouped according to the sum of its digits.
#
# Return the number of groups that have the largest size.
#
#
#
# Example 1:
#
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
# Example 2:
#
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
#
#
# Constraints:
#
# 1 <= n <= 104
# Solution
# Python O(NlogN) O(logN) Hashmap
class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap: dict[int, int] = dict()
        max_group: int = 0
        for num in range(1, n + 1):
            digit_sum: int = 0
            while num:
                digit_sum += num % 10
                num //= 10
            hashmap[digit_sum] = hashmap.get(digit_sum, 0) + 1
            max_group = max(max_group, hashmap[digit_sum])
        return sum(group == max_group for digit_sum, group in hashmap.items())

# C++ O(NlogN) O(logN) HashMap
class Solution {
public:
    int countLargestGroup(int n) {
        unordered_map<int, int> hashmap;
        int maxSum = 0;
        for (int num = 1; num <= n; ++num) {
            int digitSum = 0, cnum = num;
            while (cnum) {
                digitSum += cnum % 10;
                cnum /= 10;
            }
            ++hashmap[digitSum];
            maxSum = max(maxSum, hashmap[digitSum]);
        }
        int output = 0;
        for (auto & p : hashmap) {
            if (p.second == maxSum) ++output;
        }
        return output;
    }
};