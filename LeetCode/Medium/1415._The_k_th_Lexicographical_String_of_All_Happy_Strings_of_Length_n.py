# A happy string is a string that:
#
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
#
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
#
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
#
#
#
# Example 1:
#
# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
# Example 2:
#
# Input: n = 1, k = 4
# Output: ""
# Explanation: There are only 3 happy strings of length 1.
# Example 3:
#
# Input: n = 3, k = 9
# Output: "cab"
# Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
#
#
# Constraints:
#
# 1 <= n <= 10
# 1 <= k <= 100
# Solution
# Python O(2**N) O(N) Backtracking
class Solution:
    cur_k: int = 0
    answer: list[str] = []
    def backtrack(self, cursub: list[str], n: int, k: int) -> bool:
        if len(cursub) == n:
            if self.cur_k == k:
                self.answer = cursub
                return True
            return False
        for letter in 'abc':
            if cursub and cursub[-1] == letter: continue
            cursub.append(letter)
            if len(cursub) == n: self.cur_k += 1
            if self.backtrack(cursub, n, k): return True
            cursub.pop()
        return False

    def getHappyString(self, n: int, k: int) -> str:
        self.cur_k = 0
        self.answer = []
        cursub: list[str] = []
        self.backtrack(cursub, n, k)
        return ''.join(self.answer)

# C++ O(2**N) O(N) Backtracking
class Solution {
private:
    int curK = 0;
public:
    bool backtrack(std::string& substr, int& n, int& k) {
        if ((curK == k) || (substr.size() == n)) {
            if (curK == k && substr.size() == n) return true;
            return false;
        } else if (curK > k) return false;

        for (int idx = 97; idx < 97 + 3; ++idx) {
            if (substr.size() && substr.back() - 'a' == idx - 97) continue;
            else if (substr.size() + 1 > n) continue;
            substr.push_back((char)idx);
            if (substr.size() == n) ++curK;
            if (backtrack(substr, n, k)) return true;
            substr.pop_back();
        }
        return false;
    };

    string getHappyString(int n, int k) {
        std::vector<bool> used (n, false);
        std::string substr = "";
        curK = 0;
        backtrack(substr, n, k);
        return substr;
    }
};