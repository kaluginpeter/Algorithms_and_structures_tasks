# You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.
#
# In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.
#
# Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.
#
#
#
# Example 1:
#
# Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
# Output: ["word","note","wood"]
# Explanation:
# - Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
# - Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
# - It would take more than 2 edits for "ants" to equal a dictionary word.
# - "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
# Thus, we return ["word","note","wood"].
# Example 2:
#
# Input: queries = ["yes"], dictionary = ["not"]
# Output: []
# Explanation:
# Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.
#
#
# Constraints:
#
# 1 <= queries.length, dictionary.length <= 100
# n == queries[i].length == dictionary[j].length
# 1 <= n <= 100
# All queries[i] and dictionary[j] are composed of lowercase English letters.
# Solution
# Python O(NMK) O(N) String
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n: int = len(queries)
        m: int = len(dictionary)
        bound: int = len(queries[0])
        output: list[str] = []
        for i in range(n):
            for j in range(m):
                miss: int = 0
                for k in range(bound):
                    if queries[i][k] != dictionary[j][k]:
                        miss += 1
                        if miss > 2: break
                if miss <= 2:
                    output.append(queries[i])
                    break
        return output

# C++ O(NMK) O(N) String
class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        std::vector<std::string> output;
        size_t n = queries.size(), m = dictionary.size();
        size_t bound = queries.back().size();
        for (size_t i = 0; i < n; ++i) {
            for (size_t j = 0; j < m; ++j) {
                size_t miss = 0;
                for (size_t k = 0; k < bound; ++k) {
                    if (queries[i][k] != dictionary[j][k]) ++miss;
                    if (miss > 2) break;
                }
                if (miss <= 2) {
                    output.push_back(queries[i]);
                    break;
                }
            }
        }
        return output;
    }
};