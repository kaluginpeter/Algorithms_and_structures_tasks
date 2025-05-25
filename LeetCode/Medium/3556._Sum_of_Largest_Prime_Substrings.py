# Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.
#
# Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return 0.
#
# A prime number is a natural number greater than 1 with only two factors, 1 and itself.
#
# A substring is a contiguous sequence of characters within a string.
#
# Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.
#
#
#
# Example 1:
#
# Input: s = "12234"
#
# Output: 1469
#
# Explanation:
#
# The unique prime numbers formed from the substrings of "12234" are 2, 3, 23, 223, and 1223.
# The 3 largest primes are 1223, 223, and 23. Their sum is 1469.
# Example 2:
#
# Input: s = "111"
#
# Output: 11
#
# Explanation:
#
# The unique prime number formed from the substrings of "111" is 11.
# Since there is only one prime number, the sum is 11.
#
#
# Constraints:
#
# 1 <= s.length <= 10
# s consists of only digits.
# Solution
# Python O(|S|^2 + |P|sqrt(max(P)) + |P|log|P|) O(|P|) Math Sorting Greedy
class Solution:
    def is_prime(self, x: int) -> bool:
        if x % 2 == 0 and x != 2: return False
        bound: int = int(x**.5) + 1
        for d in range(3, bound, 2):
            if x % d == 0: return False
        return True

    def sumOfLargestPrimes(self, s: str) -> int:
        primes: list[int] = []
        seen: set[int] = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                number: int = int(s[i:j + 1])
                if self.is_prime(number) and number != 1 and number not in seen:
                    seen.add(number)
                    primes.append(number)
        if len(primes) < 3: return sum(primes)
        primes.sort()
        return sum(primes[-3:])

# C++ O(|S|^2 + |P|sqrt(max(P)) + |P|log|P|) O(|P|) Math Sorting Greedy
class Solution {
public:
    bool isPrime(long long x) {
        if (x % 2 == 0 && x != 2) return false;
        long long bound = sqrt(x) + 1;
        for (long long d = 3; d < bound; d += 2) {
            if (x % d == 0) return false;
        }
        return true;
    }

    long long sumOfLargestPrimes(string s) {
        vector<long long> primes;
        unordered_set<long long> seen;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                long long number = stoll(s.substr(i, j - i + 1));
                if (isPrime(number) && number != 1 && !seen.count(number)) {
                    primes.push_back(number);
                    seen.insert(number);
                }
            }
        }
        if (primes.size() < 3) return accumulate(primes.begin(), primes.end(), 0LL);
        sort(primes.begin(), primes.end());
        return accumulate(primes.begin() + (primes.size() - 3), primes.end(), 0LL);
    }
};