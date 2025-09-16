# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
#
# We repeatedly make k duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
#
#
#
# Example 1:
#
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:
#
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation:
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:
#
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
#
#
# Constraints:
#
# 1 <= s.length <= 105
# 2 <= k <= 104
# s only contains lowercase English letters.
# Solution
# Python O(N) O(N) Stack
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n: int = len(s)
        left: int = 0
        right: int = n - 1
        st: list[tuple[int, int]] = []
        for right in range(n):
            if s[left] == s[right]: continue
            length: int = (right - left) % k
            if st and st[-1][-1] == ord(s[left]):
                length = (length + st.pop()[0]) % k
            left = right
            if not length: continue
            st.append((length, ord(s[left - 1])))
        length: int = (n - left) % k
        if st and st[-1][-1] == ord(s[left]):
            length = (length + st.pop()[0]) % k
        if length: st.append((length, ord(s[left])))
        output: list[str] = [chr(ch) * freq for freq, ch in st]
        return ''.join(output)

# C++ O(N) O(N) Stack
class Solution {
public:
    string removeDuplicates(string s, int k) {
        std::stack<std::pair<int, int>> st;
        size_t left = 0, n = s.size();
        for (size_t right = 0; right < n; ++right) {
            if (s[right] != s[left]) {
                size_t length = (right - left) % k;
                if (!st.empty() && st.top().second == s[left] - 'a') {
                    length = (length + st.top().first) % k;
                    st.pop();
                }
                left = right;
                if (!length) continue;
                else st.push(std::pair<int, int>(length, s[left - 1] - 'a'));
            }
        }
        size_t length = (n - left) % k;
        if (!st.empty() && st.top().second == s[left] - 'a') {
            length = (length + st.top().first) % k;
            st.pop();
        }
        if (length) st.push(std::pair<int, int>(length, s[left] - 'a'));
        std::string output = "";
        while (!st.empty()) {
            char ch = static_cast<char>(st.top().second + 'a');
            for (size_t i = 0; i < st.top().first; ++i) output.push_back(ch);
            st.pop();
        }
        std::reverse(output.begin(), output.end());
        return output;
    }
};