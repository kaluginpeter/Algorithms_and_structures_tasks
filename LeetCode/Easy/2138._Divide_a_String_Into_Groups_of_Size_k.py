# A string s can be partitioned into groups of size k using the following procedure:
#
# The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each character can be a part of exactly one group.
# For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
# Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.
#
# Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.
#
#
#
# Example 1:
#
# Input: s = "abcdefghi", k = 3, fill = "x"
# Output: ["abc","def","ghi"]
# Explanation:
# The first 3 characters "abc" form the first group.
# The next 3 characters "def" form the second group.
# The last 3 characters "ghi" form the third group.
# Since all groups can be completely filled by characters from the string, we do not need to use fill.
# Thus, the groups formed are "abc", "def", and "ghi".
# Example 2:
#
# Input: s = "abcdefghij", k = 3, fill = "x"
# Output: ["abc","def","ghi","jxx"]
# Explanation:
# Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
# For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
# Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s consists of lowercase English letters only.
# 1 <= k <= 100
# fill is a lowercase English letter.
# Solution 1
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            it = s[i:i+k]
            if len(it) == k:
                ans += [it]
            else:
                ans += [it + (k - len(it)) * fill]
        return ans
# Solution 2
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans, s = [], s + fill * (k - 1)
        for i in range(0, len(s) - len(s) % k, k):
            ans += [s[i:i+k]]
        return ans
# Solution 3
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans, so = [], s + fill * (k - 1)
        for i in range(0, len(s), k):
            ans += [so[i:i+k]]
        return ans


# Python O(N) O(N) Simulation
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output: list[str] = []
        word: list[str] = []
        for i in range(len(s)):
            word.append(s[i])
            if (i + 1) % k == 0:
                output.append(''.join(word))
                word.clear()
        if word:
            while len(word) < k: word.append(fill)
            output.append(''.join(word))
        return output

# C++ O(N) O(N) Simulation
class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        std::vector<std::string> output;
        std::string word = "";
        for (std::string::size_type i = 0; i < s.size(); ++i) {
            word.push_back(s[i]);
            if ((i + 1) % k == 0) {
                output.push_back(word);
                word.clear();
            }
        }
        if (!word.empty()) {
            while (word.size() < k) word.push_back(fill);
            output.push_back(word);
        }
        return output;
    }
};