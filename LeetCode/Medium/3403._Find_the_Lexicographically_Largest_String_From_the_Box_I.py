# You are given a string word, and an integer numFriends.
#
# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
#
# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the
# lexicographically largest
#  string from the box after all the rounds are finished.
#
#
#
# Example 1:
#
# Input: word = "dbca", numFriends = 2
#
# Output: "dbc"
#
# Explanation:
#
# All possible splits are:
#
# "d" and "bca".
# "db" and "ca".
# "dbc" and "a".
# Example 2:
#
# Input: word = "gggg", numFriends = 4
#
# Output: "g"
#
# Explanation:
#
# The only possible split is: "g", "g", "g", and "g".
#
#
#
# Constraints:
#
# 1 <= word.length <= 5 * 103
# word consists only of lowercase English letters.
# 1 <= numFriends <= word.length
# Solution
# Python O(NM) O(M) Greedy
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        output: str = ''
        n: int = len(word)
        max_length: int = n - numFriends + 1
        for idx in range(n):
            output = max(output, word[idx:idx + max_length])
        return output

# C++ O(NM) O(M) Greedy
class Solution {
public:
    string answerString(string word, int numFriends) {
        if (numFriends == 1) {
            return word;
        }
        std::string output = "";
        int n = word.size();
        int maxLength = n - numFriends + 1;
        for (int idx = 0; idx < n; ++idx) {
            output = std::max(output, word.substr(idx, maxLength));
        }
        return output;
    }
};

# Python O(N^2) O(N) String Greedy
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n: int = len(word)
        if numFriends == 1: return word
        candidates: list[int] = [0]
        for i in range(1, n):
            if word[i] > word[candidates[0]]:
                candidates.clear()
                candidates.append(i)
            elif word[i] == word[candidates[0]]: candidates.append(i)
        output: str = word[candidates[0]:candidates[0] + (n - max(0, numFriends - 1 - candidates[0]) - candidates[0])]
        for i in range(1, len(candidates)):
            candidate: str = word[candidates[i]:candidates[i] + (n - max(0, numFriends - 1 - candidates[i]) - candidates[i])]
            if candidate > output: output = candidate
        return output

# C++ O(N^2) O(N) String Greedy
class Solution {
public:
    string answerString(string word, int numFriends) {
        int n = word.size();
        if (numFriends == 1) return word;
        vector<int> candidates = {0};
        for (int i = 1; i < n; ++i) {
            if (word[i] > word[candidates[0]]) {
                candidates.clear();
                candidates.push_back(i);
            } else if (word[i] == word[candidates[0]]) candidates.push_back(i);
        }
        string output = word.substr(candidates[0], n - max(0, numFriends - 1 - candidates[0]) - candidates[0]);
        for (int i = 1; i < candidates.size(); ++i) {
            string candidate = word.substr(candidates[i], n - max(0, numFriends - 1 - candidates[i]) - candidates[i]);
            if (candidate > output) output = candidate;
        }
        return output;
    }
};