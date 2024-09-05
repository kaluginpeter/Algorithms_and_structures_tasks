# You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.
#
# You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.
#
# Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.
#
# The average value of a set of k numbers is the sum of the numbers divided by k.
#
# Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.
#
#
#
# Example 1:
#
# Input: rolls = [3,2,4,3], mean = 4, n = 2
# Output: [6,6]
# Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
# Example 2:
#
# Input: rolls = [1,5,6], mean = 3, n = 4
# Output: [2,3,2,2]
# Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
# Example 3:
#
# Input: rolls = [1,2,3,4], mean = 6, n = 4
# Output: []
# Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
#
#
# Constraints:
#
# m == rolls.length
# 1 <= n, m <= 105
# 1 <= rolls[i], mean <= 6
# Solution
# Python O(N + M) O(N)
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m: int = len(rolls)
        N: int = m + n
        n_dolls: list[int] = []
        total_sum: int = sum(rolls)
        for _ in range(n):
            candidate: int = None
            for doll in range(1, 7):
                if (total_sum + doll + (n - 1)) / N <= mean:
                    candidate = doll

            if candidate:
                total_sum += candidate
                n -= 1
                n_dolls.append(candidate)
        return n_dolls if total_sum / N == mean else []

# C++ O(N + M) O(N)
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int total_sum = mean * (m + n);
        int current_sum = accumulate(rolls.begin(), rolls.end(), 0);
        int missing_sum = total_sum - current_sum;
        if (missing_sum < n || missing_sum > 6 * n) {
            return {};
        }
        vector<int> n_rolls(n, 1);
        missing_sum -= n;

        for (int i = 0; i < n && missing_sum > 0; ++i) {
            int add = min(missing_sum, 5);
            n_rolls[i] += add;
            missing_sum -= add;
        }

        return n_rolls;
    }
};