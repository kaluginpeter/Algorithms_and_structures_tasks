# You are given a string s consisting of lowercase English letters, and an integer k.
# First, convert s into an integer by replacing each letter with its position
# in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
# Then, transform the integer by replacing it with the sum of its digits.
# Repeat the transform operation k times in total.
# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.
#
# Example 1:
#
# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.
# Example 2:
#
# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.
# Example 3:
#
# Input: s = "zbax", k = 2
# Output: 8
#
# Constraints:
# 1 <= s.length <= 100
# 1 <= k <= 10
# s consists of lowercase English letters.
# Solution
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        al = 'abcdefghijklmnopqrstuvwxyz'
        w = ''.join(str(al.index(i)+1) for i in s)
        for i in range(k):
            w = sum(int(i) for i in str(w))
        return w

# Python
# Solution Simulation O(NK) O(N)
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numbers: str = ''.join(str(ord(char) - 96) for char in s)
        for _ in range(k):
            numbers = str(sum(int(num) for num in numbers))
        return int(numbers)

# C++ O(NK) O(N)
class Solution {
public:
    int getLucky(string s, int k) {
        string str_s = "";
        for (char char_s : s) {
            str_s += to_string(int(char_s) - 96);
        }
        for (int i = 0; i < k; i++) {
            int total_sum = 0;
            for (char char_s : str_s) {
                int diff = char_s - '0';
                total_sum += diff;
            }
            str_s = to_string(total_sum);
        }
        return stoi(str_s);
    }
};