/*
You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.



Example 1:

Input: s = "abba", k = 2

Output: "baab"

Explanation:

The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
Example 2:

Input: s = "aa", k = 2

Output: ""

Explanation:

There is only one palindromic rearrangement: "aa".
The output is an empty string since k = 2 exceeds the number of possible rearrangements.
Example 3:

Input: s = "bacab", k = 1

Output: "abcba"

Explanation:

The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
s is guaranteed to be palindromic.
1 <= k <= 106
*/
// Solution
// C++ O(Nphi(logK)) O(N) String Math
class Solution {
private:
    long long comb(long long n, long long m, long long k) {
        long long c = 1;
        m = std::min(m, n - m); // without repetitions
        for (long long i = 1; i <= m; ++i) {
            c = c * (n - i + 1) / i;
            if (c > k) return k + 1;
        }
        return c;
    }
    long long perm(int n, const long long& k, std::array<int, 26>& hashmap) {
        long long p = 1;
        for (size_t i = 0; i < 26; ++i) {
            if (!hashmap[i]) continue;
            p *= comb(n, hashmap[i], k);
            if (p > k) break;
            n -= hashmap[i];
        }
        return p;
    };
public:
    std::string smallestPalindrome(std::string s, long long k) {
        size_t bound = s.length() >> 1; // floor rounding
        std::array<int, 26> hashmap{};
        for (size_t i = 0; i < bound; ++i) ++hashmap[s[i] - 'a'];
        std::string left = "";
        long long start = 1;
        for (size_t pos = 0; pos < bound; ++pos) {
            for (size_t i = 0; i < 26; ++i) {
                if (!hashmap[i]) continue;
                --hashmap[i];
                long long perms = perm(bound - pos - 1, k, hashmap);
                if (start + perms > k) {
                    left += static_cast<char>(i + 'a');
                    break;
                }
                ++hashmap[i];
                start += perms;
            }
        }
        if (left.length() < bound) return "";
        return left + (s.length() & 1 ? std::string(1, s[bound]) : "") + std::string(left.rbegin(), left.rend());
    }
};