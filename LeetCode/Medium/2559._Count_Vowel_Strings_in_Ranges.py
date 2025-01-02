# You are given a 0-indexed array of strings words and a 2D array of integers queries.
#
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
#
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
#
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
#
#
#
# Example 1:
#
# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].
# Example 2:
#
# Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# Output: [3,2,1]
# Explanation: Every string satisfies the conditions, so we return [3,2,1].
#
#
# Constraints:
#
# 1 <= words.length <= 105
# 1 <= words[i].length <= 40
# words[i] consists only of lowercase English letters.
# sum(words[i].length) <= 3 * 105
# 1 <= queries.length <= 105
# 0 <= li <= ri < words.length
# Solution
# Python O(N) O(N) Prefix Sum
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels: set[str] = {'a', 'e', 'o', 'i', 'u'}
        prefix_sum: list[int] = []
        for word in words:
            score: int = prefix_sum[-1] if prefix_sum else 0
            if word[0] in vowels and word[-1] in vowels:
                score += 1
            prefix_sum.append(score)
        output: list[int] = []
        for query in queries:
            if query[0]:
                output.append(prefix_sum[query[1]] - prefix_sum[query[0] - 1])
            else:
                output.append(prefix_sum[query[1]])
        return output

# C++ O(N) O(N) Prefix Sum
class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        std::unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        std::vector<int> prefixSum;
        for (std::string& word : words) {
            int score = (prefixSum.size()? prefixSum[prefixSum.size() - 1] : 0);
            if (vowels.count(word[0]) && vowels.count(word[word.size() - 1])) {
                ++score;
            }
            prefixSum.push_back(score);
        }
        std::vector<int> output;
        for (std::vector<int>& query : queries) {
            if (query[0]) {
                output.push_back(prefixSum[query[1]] - prefixSum[query[0] - 1]);
            } else {
                output.push_back(prefixSum[query[1]]);
            }
        }
        return output;
    }
};