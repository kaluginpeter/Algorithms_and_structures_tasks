/*
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.
*/
// Solution
// Go O(NK) O(1) TwoPointers Greedy
func isPalindrom(s *string, left int, right int) bool {
    for left < right {
        if (*s)[left] != (*s)[right] {
            return false;
        }
        left++
        right--
    }
    return true
}
func maxPalindromes(s string, k int) int {
    var output, n, i int = 0, len(s), 0
    for i + k <= n {
        if isPalindrom(&s, i, i + k - 1) {
            output++
            i += k
        } else if i + k + 1 <= n && isPalindrom(&s, i, i + k) {
            output++
            i += k + 1
        } else { i++ }
    }
    return output
}

// C++ O(NK) O(1) Greedy TwoPointers
class Solution {
public:
    bool f(std::string& s, size_t i, size_t j) {
        while (i < j) {
            if (s[i] != s[j]) return false;
            ++i;
            --j;
        }
        return true;
    }
    int maxPalindromes(string s, int k) {
        size_t n = s.size(), i = 0, output = 0;
        while (i + k <= n) {
            if (f(s, i, i + k - 1)) {
                ++output;
                i += k;
            } else if (i + k + 1 <= n && f(s, i, i + k)) {
                ++output;
                i += k + 1;
            } else ++i;
        }
        return output;
    }
};