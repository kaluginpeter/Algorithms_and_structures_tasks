# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday,
# he will put in $1 more than the day before. On every subsequent Monday,
# he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
#
# Example 1:
#
# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
# Example 2:
#
# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37.
# Notice that on the 2nd Monday, Hercy only puts in $2.
# Example 3:
#
# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8)
# + (3 + 4 + 5 + 6 + 7 + 8) = 96.
#
# Constraints:
# 1 <= n <= 1000
# Solution
class Solution:
    def totalMoney(self, n: int) -> int:
        count, start, weeks, inp = 0, 1, 0, -1
        for i in range(n):
            if weeks == 7:
                start += 1
                weeks, inp = 0, 0
                count += start
                weeks += 1
                continue
            inp += 1
            count += start + inp
            weeks += 1
        return count

# Solution 2 O(7), O(1)
class Solution(object):
    def totalMoney(self, n):
        if n % 7 == 0:
            return sum((1 + 7 + i * 2) * 7 / 2 for i in range(n // 7))
        x = sum((1 + 7 + i * 2) * 7 / 2 for i in range(n // 7))
        return x + sum(i + n // 7 for i in range(1, n % 7 + 1))


class Solution {
public:
    int totalMoney(int n) {
       int output = 0, week = 1;
       for (int day = 0; day < n; ++day) {
        if (day && day % 7 == 0) ++week;
        output += week + day % 7;
       }
       return output;
    }
};