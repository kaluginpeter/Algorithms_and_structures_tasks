# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
#
# For a given query word, the spell checker handles two categories of spelling mistakes:
#
# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
# In addition, the spell checker operates under the following precedence rules:
#
# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
#
#
#
# Example 1:
#
# Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
# Example 2:
#
# Input: wordlist = ["yellow"], queries = ["YellOw"]
# Output: ["yellow"]
#
#
# Constraints:
#
# 1 <= wordlist.length, queries.length <= 5000
# 1 <= wordlist[i].length, queries[i].length <= 7
# wordlist[i] and queries[i] consist only of only English letters.
# Solution
# Python O(N + M) O(N) HashMap String
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        common: set[str] = set()
        lower: dict[str, str] = dict()
        without: dict[str, str] = dict()
        for word in wordlist:
            common.add(word)
            x = word.lower()
            if x not in lower: lower[x] = word
            x = ''.join('*' if ch in 'aeoiu' else ch for ch in x)
            if x not in without: without[x] = word
        output: list[str] = []
        for q in queries:
            if q in common:
                output.append(q)
                continue
            q = q.lower()
            if q in lower:
                output.append(lower[q])
                continue
            q = ''.join('*' if ch in 'aeoiu' else ch for ch in q)
            if q in without: output.append(without[q])
            else: output.append('')
        return output

# C++ O(N + M) O(N) HashMap String
class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        std::unordered_set<std::string> common;
        std::unordered_map<std::string, std::string> usual, without;
        std::string vowels = "aeoiuAEOIU";
        for (std::string &w : wordlist) {
            common.insert(w);
            std::string x = w;
            std::transform(w.begin(), w.end(), x.begin(), ::tolower);
            if (!usual.count(x)) usual[x] = w;
            x = "";
            for (char &ch : w) {
                if (vowels.find(ch) != std::string::npos) x.push_back('*');
                else x.push_back(std::tolower(ch));
            }
            if (!without.count(x)) without[x] = w;
        }
        std::vector<std::string> output;
        for (std::string &q : queries) {
            if (common.count(q)) {
                output.push_back(q);
                continue;
            }
            std::transform(q.begin(), q.end(), q.begin(), ::tolower);
            if (usual.count(q)) {
                output.push_back(usual[q]);
                continue;
            }
            for (size_t i = 0; i < q.size(); ++i) {
                if (vowels.find(q[i]) == std::string::npos) continue;
                q[i] = '*';
            }
            if (without.count(q)) {
                output.push_back(without[q]);
                continue;
            } else output.push_back("");
        }
        return output;
    }
};