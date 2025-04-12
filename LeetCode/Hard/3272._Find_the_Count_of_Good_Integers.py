# You are given two positive integers n and k.
#
# An integer x is called k-palindromic if:
#
# x is a palindrome.
# x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.
#
# Return the count of good integers containing n digits.
#
# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.
#
#
#
# Example 1:
#
# Input: n = 3, k = 5
#
# Output: 27
#
# Explanation:
#
# Some of the good integers are:
#
# 551 because it can be rearranged to form 515.
# 525 because it is already k-palindromic.
# Example 2:
#
# Input: n = 1, k = 4
#
# Output: 2
#
# Explanation:
#
# The two good integers are 4 and 8.
#
# Example 3:
#
# Input: n = 5, k = 6
#
# Output: 2468
#
#
#
# Constraints:
#
# 1 <= n <= 10
# 1 <= k <= 9
# Solution
# Python O(NlogN * 10^M) O(N * 10^M) Math Combinatorics
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        hashset: set[str] = set()
        base: int = 10 ** ((n - 1) // 2)
        odd: int = n & 1
        for num in range(base, base * 10):
            str_num: str = str(num)
            str_num += str_num[-1 + -odd::-1]
            palindrom: int = int(str_num)
            if palindrom % k == 0:
                hashset.add(''.join(sorted(str_num)))
        prefix_sum: list[int] = [1] * (n + 1)
        count: int = 0
        for i in range(1, n + 1): prefix_sum[i] = prefix_sum[i - 1] * i
        for s in hashset:
            digits: list[int] = [0] * 10
            for d in s: digits[ord(d) - 48] += 1
            part: int = (n - digits[0]) * prefix_sum[n - 1]
            for d in digits: part //= prefix_sum[d]
            count += part
        return count

# C++ O(NlogN * 10^M) O(N * 10^M) Math Combinatorics
class Solution {
public:
    long long countGoodIntegers(int n, int k) {
        unordered_set<string> hashset;
        int base = pow(10, (n - 1) / 2);
        int odd = n & 1;
        for (int num = base; num < base * 10; ++num) {
            string strNum = to_string(num);
            strNum += string(strNum.rbegin() + odd, strNum.rend());
            long long palindrom = stoll(strNum);
            if (palindrom % k == 0) {
                sort(strNum.begin(), strNum.end());
                hashset.emplace(strNum);
            }
        }
        vector<long long> prefixSum(n + 1, 1);
        long long count = 0;
        for (int i = 1; i <= n; i++) prefixSum[i] = prefixSum[i - 1] * i;
        for (const string &s : hashset) {
            vector<int> digits(10);
            for (char d : s) ++digits[d - '0'];
            long long part = (n - digits[0]) * prefixSum[n - 1];
            for (int d : digits) part /= prefixSum[d];
            count += part;
        }
        return count;
    }
};