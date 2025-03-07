# Given two positive integers left and right, find the two integers num1 and num2 such that:
#
# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
#
#
#
# Example 1:
#
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.
# Example 2:
#
# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
#
#
# Constraints:
#
# 1 <= left <= right <= 106
# Solution
# Python O(R**.5 * R + 2M) O(R) Number Theory Math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve: list[bool] = [True] * (right + 1)
        bound: int = int(right**.5) + 1
        for d in range(2, bound):
            if not sieve[d]: continue
            for p in range(d + d, right + 1, d):
                sieve[p] = False
        output: list[int, int] = [-1, -1]
        a = b = -1
        min_diff: int = float('inf')
        for p in range(max(2, left), right + 1):
            if not sieve[p]: continue
            a, b = b, a
            b = p
            if a != -1 and b - a < min_diff:
                min_diff = b - a
                output = [a, b]
        return output

# C++ O(R**.5 * R + 2M) O(R) NumberTheory Math
class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<bool> sieve (right + 1, true);
        int bound = sqrt(right) + 1;
        for (int d = 2; d <= bound; ++d) {
            if (!sieve[d]) continue;
            for (int p = d + d; p <= right; p += d) {
                sieve[p] = false;
            }
        }
        int minDiff = INT32_MAX;
        vector<int> output = {-1, -1};
        int a = -1, b = -1;
        for (int p = max(2, left); p <= right; ++p) {
            if (sieve[p]) {
                swap(a, b);
                b = p;
                if (a != -1 && b - a < minDiff) {
                    minDiff = b - a;
                    output[0] = a;
                    output[1] = b;
                }
            }
        }
        return output;
    }
};