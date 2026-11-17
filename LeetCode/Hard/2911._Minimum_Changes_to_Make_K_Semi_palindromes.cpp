/*
Given a string s and an integer k, partition s into k substrings such that the letter changes needed to make each substring a semi-palindrome are minimized.

Return the minimum number of letter changes required.

A semi-palindrome is a special type of string that can be divided into palindromes based on a repeating pattern. To check if a string is a semi-palindrome:​

Choose a positive divisor d of the string's length. d can range from 1 up to, but not including, the string's length. For a string of length 1, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.
For a given divisor d, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length d. Specifically, the first group consists of characters at positions 1, 1 + d, 1 + 2d, and so on; the second group includes characters at positions 2, 2 + d, 2 + 2d, etc.
The string is considered a semi-palindrome if each of these groups forms a palindrome.
Consider the string "abcabc":

The length of "abcabc" is 6. Valid divisors are 1, 2, and 3.
For d = 1: The entire string "abcabc" forms one group. Not a palindrome.
For d = 2:
Group 1 (positions 1, 3, 5): "acb"
Group 2 (positions 2, 4, 6): "bac"
Neither group forms a palindrome.
For d = 3:
Group 1 (positions 1, 4): "aa"
Group 2 (positions 2, 5): "bb"
Group 3 (positions 3, 6): "cc"
All groups form palindromes. Therefore, "abcabc" is a semi-palindrome.
 

Example 1:

Input: s = "abcac", k = 2

Output: 1

Explanation: Divide s into "ab" and "cac". "cac" is already semi-palindrome. Change "ab" to "aa", it becomes semi-palindrome with d = 1.

Example 2:

Input: s = "abcdef", k = 2

Output: 2

Explanation: Divide s into substrings "abc" and "def". Each needs one change to become semi-palindrome.

Example 3:

Input: s = "aabbaa", k = 3

Output: 0

Explanation: Divide s into substrings "aa", "bb" and "aa". All are already semi-palindromes.

 

Constraints:

2 <= s.length <= 200
1 <= k <= s.length / 2
s contains only lowercase English letters.
 

*/
// Solution
// C++ O(N^2Msqrt(M) + N^2K) O(NK) DynamicProgramming TwoPointers Math
constexpr int bound = INT32_MAX;
class Solution {
public:
    int getPalindromOps(std::string&s, size_t& pivot, size_t d, size_t& n) {
        int score = 0;
        for (size_t start = 0; start < d; ++start) {
            std::string tmp = "";
            for (size_t ptr = 0; ptr * d < n; ++ptr) {
                tmp.push_back(s[pivot + start + ptr * d]);
            }
            size_t left = 0, right = tmp.size() - 1;
            while (left < right) {
                if (tmp[left] != tmp[right]) ++score;
                ++left;
                --right;
            }
        }
        return score;
    }
    int getMinOps(std::string& s, size_t i, size_t j) {
        size_t n = j - i + 1;
        int output = bound;
        for (size_t d = 1; d <= (size_t)std::sqrt(n) + 1; ++d) {
            if (n % d != 0) continue;
            if (d != n) output = std::min(output, getPalindromOps(s, i, d, n));
            if (n / d != n) output = std::min(output, getPalindromOps(s, i, n / d, n));
        }
        return output;
    }

    int minimumChanges(string s, int K) {
        size_t N = s.size();
        std::vector<std::vector<int>> dp = std::vector<std::vector<int>>(N + 1, std::vector<int>(K + 1, bound));
        dp[0][0] = 0; // this is a start point at which we will join our partitions
        for (size_t i = 1; i <= N; ++i) {
            for (size_t j = i + 1; j <= N; ++j) {
                int cost = getMinOps(s, i - 1, j - 1);
                for (size_t k = 1; k <= K; ++k) {
                    if (dp[i - 1][k - 1] == bound) continue;
                    // try to concatenate current partition with previous one
                    dp[j][k] = std::min(dp[j][k], cost + dp[i - 1][k - 1]);
                }
            }

        }
        return dp[N][K];
    }
};

// We need to split string s on k substirngs such that
// each substring is greater than 1 and overall operations
// needed to from a semi-palindrom substring is minimized

// Let's look at the constraints: 2 <= |S| <= 200 and 1 <= K <= 100
// We cannot just to try all possible partitions since 2^100 will lead to TLE

// The approach is to try all possibilities without repetitions
// Dynamic programming can work here
// So what is the state?

// The size of constraints allow as to write O(N^3 * K) algorithm
// Let's image dp[j][k], where  "j" is the end of the current substring
// and "k" is the current partition
// The for current partition the cost will be the operations needed to transfrom
// a substring from s[i:j] and plus the cost of dp[i - 1][k - 1] where
// (i - 1) - x + 1 > 1
// Then the answer will be dp[N][K] 1 <= i < N

// Let's consider the substring s[i:j], what is the smallest number of operations
// that needed to transform it into semi-palindrom?
// We can greedily try all possibilities groups for a sqrt(j - i) and
// write O(Msqrt(M)) solution where the M is denotes the size of a substring

// Then the overall complexity will be O(N^2Nsqrt(N) + N^2K)
// The memory complexity is O(NK)