# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
#
# if the ith character is 'Y', it means that customers come at the ith hour
# whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
#
# For every hour when the shop is open and no customers come, the penalty increases by 1.
# For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.
#
# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
#
#
#
# Example 1:
#
# Input: customers = "YYNY"
# Output: 2
# Explanation:
# - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
# Example 2:
#
# Input: customers = "NNNNN"
# Output: 0
# Explanation: It is best to close the shop at the 0th hour as no customers arrive.
# Example 3:
#
# Input: customers = "YYYY"
# Output: 4
# Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
#
#
# Constraints:
#
# 1 <= customers.length <= 105
# customers consists only of characters 'Y' and 'N'.
# Solution
class Solution(object):
    def bestClosingTime(self, customers):
        score, top, time = 0, 0, -1
        for i in range(len(customers)):
            top += 1 if customers[i] == "Y" else -1
            if top > score:
                score = top
                time = i
        return time + 1


# Python O(N) O(1) Greedy
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty: int = float('inf')
        hour: int = 0
        income: int = customers.count('Y')
        outcome: int = 0
        for i in range(len(customers)):
            if income + outcome < penalty:
                penalty = income + outcome
                hour = i
            if customers[i] == 'Y':
                income -= 1
            else:
                outcome += 1
        if outcome < penalty: hour = len(customers)
        return hour

# C++ O(N) O(1) Greedy
class Solution {
public:
    int bestClosingTime(string customers) {
        int penalty = INT32_MAX, hour = 0;
        int income = std::count(customers.begin(), customers.end(), 'Y'), outcome = 0;
        for (int i = 0; i < customers.size(); ++i) {
            if (income + outcome < penalty) {
                penalty = income + outcome;
                hour = i;
            }
            if (customers[i] == 'Y') --income;
            else ++outcome;
        }
        if (outcome < penalty) hour = customers.size();
        return hour;
    }
};